import json
import requests
import stripe
import paypalrestsdk
import paytmchecksum
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Booking, FoodOrder, Payment
from .models import generate_order_id

# Configure Stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

# Configure PayPal
paypalrestsdk.configure({
    "mode": settings.PAYPAL_MODE,
    "client_id": settings.PAYPAL_CLIENT_ID,
    "client_secret": settings.PAYPAL_CLIENT_SECRET
})

# Paytm Helpers
def generate_paytm_checksum(param_dict):
    return paytmchecksum.generateSignature(param_dict, settings.PAYTM_MERCHANT_KEY)

def verify_paytm_checksum(param_dict, checksum):
    return paytmchecksum.verifySignature(param_dict, settings.PAYTM_MERCHANT_KEY, checksum)

def get_paytm_transaction_url():
    if settings.PAYTM_ENVIRONMENT == 'STAGING':
        return "https://securegw-stage.paytm.in/order/process"
    return "https://securegw.paytm.in/order/process"

def get_paytm_token_url():
    mid = settings.PAYTM_MERCHANT_ID
    if settings.PAYTM_ENVIRONMENT == 'STAGING':
        return f"https://securegw-stage.paytm.in/theia/api/v1/initiateTransaction?mid={mid}&orderId="
    return f"https://securegw.paytm.in/theia/api/v1/initiateTransaction?mid={mid}&orderId="

# Home Page View
def home(request):
    return render(request, 'home.html')

# Paytm Payment - Ticket Booking View
def book_ticket(request):
    if request.method == 'GET':
        return render(request, 'book_ticket.html')
    
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name', '').strip()
        email = request.POST.get('email', '').strip()
        mobile = request.POST.get('mobile', '').strip()
        match_name = request.POST.get('match_name', '').strip()
        num_tickets = int(request.POST.get('num_tickets', 1))
        amount = request.POST.get('amount', '0').strip()

        # Save booking details
        booking = Booking.objects.create(
            customer_name=customer_name,
            email=email,
            mobile=mobile,
            match_name=match_name,
            num_tickets=num_tickets,
            amount=amount,
            status='PENDING'
        )

        # Paytm request params
        paytm_params = {
            "body": {
                "requestType": "Payment",
                "mid": settings.PAYTM_MERCHANT_ID,
                "websiteName": settings.PAYTM_WEBSITE,
                "orderId": booking.order_id,
                "callbackUrl": settings.PAYTM_CALLBACK_URL,
                "txnAmount": {
                    "value": str(amount),
                    "currency": "INR"
                },
                "userInfo": {
                    "custId": email,
                    "mobile": mobile,
                    "email": email,
                    "firstName": customer_name,
                }
            }
        }

        checksum = generate_paytm_checksum(paytm_params["body"])
        paytm_params["head"] = {"signature": checksum}
        
        token_url = get_paytm_token_url() + booking.order_id
        
        try:
            response = requests.post(
                url=token_url,
                data=json.dumps(paytm_params),
                headers={"Content-type": "application/json"}
            )
            response_dict = response.json()
            txn_token = response_dict.get('body', {}).get('txnToken', '')
        except Exception as e:
            print(f"Paytm Token Error: {e}")
            txn_token = ''

        context = {
            'booking': booking,
            'txn_token': txn_token,
            'merchant_id': settings.PAYTM_MERCHANT_ID,
            'amount': amount,
            'order_id': booking.order_id,
            'callback_url': settings.PAYTM_CALLBACK_URL,
            'paytm_url': get_paytm_transaction_url(),
        }
        return render(request, 'paytm_redirect.html', context)

# Paytm Callback Handler
@csrf_exempt
def payment_callback(request):
    if request.method == 'POST':
        callback_data = dict(request.POST)
        flat_data = {key: values[0] for key, values in callback_data.items()}
        
        checksum_received = flat_data.pop('CHECKSUMHASH', '')
        is_valid = verify_paytm_checksum(flat_data, checksum_received)
        
        if not is_valid:
            return HttpResponse("Checksum Verification Failed", status=400)
            
        order_id = flat_data.get('ORDERID', '')
        transaction_id = flat_data.get('TXNID', '')
        status_code = flat_data.get('STATUS', '')
        response_msg = flat_data.get('RESPMSG', '')
        payment_mode = flat_data.get('PAYMENTMODE', '')
        amount = flat_data.get('TXNAMOUNT', '0')
        
        if status_code == 'TXN_SUCCESS':
            booking_status = 'SUCCESS'
            payment_status = 'SUCCESS'
        else:
            booking_status = 'FAILED'
            payment_status = 'FAILED'
            
        try:
            booking = Booking.objects.get(order_id=order_id)
            booking.status = booking_status
            booking.save()
        except Booking.DoesNotExist:
            booking = None
            
        payment = Payment.objects.create(
            customer_name=booking.customer_name if booking else 'Unknown',
            email=booking.email if booking else '',
            order_id=order_id,
            transaction_id=transaction_id,
            amount=amount,
            gateway='PAYTM',
            status=payment_status,
            payment_mode=payment_mode,
            raw_response=json.dumps(flat_data)
        )
        
        context = {
            'payment': payment,
            'booking': booking,
            'status': payment_status,
            'response_msg': response_msg,
            'flat_data': flat_data,
        }
        return render(request, 'transaction_detail.html', context)
        
    return redirect('home')

# Stripe Payment - Food Ordering View
def food_order(request):
    menu_items = [
        {'id': 'paneer',  'name': 'Paneer Tikka Masala', 'price': 249},
        {'id': 'dal',     'name': 'Dal Makhani',         'price': 199},
        {'id': 'biryani', 'name': 'Veg Dum Biryani',     'price': 299},
        {'id': 'dosa',    'name': 'Masala Dosa',         'price': 149},
        {'id': 'chole',   'name': 'Chole Bhature',       'price': 179},
        {'id': 'jamun',   'name': 'Gulab Jamun',         'price': 99},
    ]
    
    if request.method == 'GET':
        return render(request, 'food_order.html', {'menu_items': menu_items})
        
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name', '').strip()
        email = request.POST.get('email', '').strip()
        food_name = request.POST.get('food_name', '').strip()
        quantity = int(request.POST.get('quantity', 1))
        price_per_item = float(request.POST.get('price_per_item', 0))
        total_amount = quantity * price_per_item
        
        food_order_obj = FoodOrder.objects.create(
            customer_name=customer_name,
            email=email,
            food_name=food_name,
            quantity=quantity,
            price_per_item=price_per_item,
            total_amount=total_amount,
            status='PENDING'
        )
        
        try:
            amount_in_paise = int(total_amount * 100)
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'inr',
                        'product_data': {
                            'name': food_name,
                            'description': f"Quantity: {quantity}",
                        },
                        'unit_amount': amount_in_paise,
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url=f"http://127.0.0.1:8000/stripe/success/?session_id={{CHECKOUT_SESSION_ID}}&order_id={food_order_obj.order_id}",
                cancel_url=f"http://127.0.0.1:8000/stripe/cancel/?order_id={food_order_obj.order_id}",
                metadata={'order_id': food_order_obj.order_id},
                customer_email=email,
            )
            
            food_order_obj.stripe_session_id = checkout_session.id
            food_order_obj.save()
            return redirect(checkout_session.url)
            
        except stripe.error.StripeError as e:
            print(f"Stripe Error: {e}")
            context = {
                'error': f"Stripe payment failed: {str(e)}",
                'menu_items': menu_items
            }
            return render(request, 'food_order.html', context)

# Stripe Success handler
def stripe_success(request):
    session_id = request.GET.get('session_id', '')
    order_id = request.GET.get('order_id', '')
    
    try:
        session = stripe.checkout.Session.retrieve(session_id)
        if session.payment_status == 'paid':
            food_order_obj = FoodOrder.objects.get(order_id=order_id)
            food_order_obj.status = 'SUCCESS'
            food_order_obj.save()
            
            payment = Payment.objects.create(
                customer_name=food_order_obj.customer_name,
                email=food_order_obj.email,
                order_id=order_id,
                transaction_id=session.payment_intent,
                amount=food_order_obj.total_amount,
                gateway='STRIPE',
                status='SUCCESS',
                payment_mode='Card',
                raw_response=str(session)
            )
            
            context = {
                'payment': payment,
                'food_order': food_order_obj,
                'gateway': 'Stripe',
            }
            return render(request, 'payment_success.html', context)
    except Exception as e:
        print(f"Stripe Success Error: {e}")
        
    return render(request, 'payment_failed.html', {'error': 'Verification failed.'})

# Stripe Cancel handler
def stripe_cancel(request):
    order_id = request.GET.get('order_id', '')
    try:
        food_order_obj = FoodOrder.objects.get(order_id=order_id)
        food_order_obj.status = 'FAILED'
        food_order_obj.save()
    except FoodOrder.DoesNotExist:
        pass
    return render(request, 'payment_failed.html', {'error': 'Payment cancelled.'})

# PayPal Payment View
def paypal_pay(request):
    if request.method == 'GET':
        return render(request, 'paypal_pay.html')
        
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name', '').strip()
        email = request.POST.get('email', '').strip()
        amount = request.POST.get('amount', '10').strip()
        description = request.POST.get('description', 'Payment').strip()
        
        request.session['paypal_customer'] = customer_name
        request.session['paypal_email'] = email
        request.session['paypal_amount'] = amount
        request.session['paypal_desc'] = description
        
        paypal_payment = paypalrestsdk.Payment({
            "intent": "sale",
            "payer": {
                "payment_method": "paypal"
            },
            "redirect_urls": {
                "return_url": settings.PAYPAL_RETURN_URL,
                "cancel_url": settings.PAYPAL_CANCEL_URL,
            },
            "transactions": [{
                "item_list": {
                    "items": [{
                        "name": description,
                        "sku": "001",
                        "price": amount,
                        "currency": "USD",
                        "quantity": 1
                    }]
                },
                "amount": {
                    "total": amount,
                    "currency": "USD"
                },
                "description": description
            }]
        })
        
        if paypal_payment.create():
            request.session['paypal_payment_id'] = paypal_payment.id
            for link in paypal_payment.links:
                if link.rel == 'approval_url':
                    return redirect(link.href)
        else:
            print(f"PayPal Create Error: {paypal_payment.error}")
            return render(request, 'paypal_pay.html', {'error': paypal_payment.error})

# PayPal Success Handler
def paypal_success(request):
    payment_id = request.GET.get('paymentId', '')
    payer_id = request.GET.get('PayerID', '')
    
    if not payment_id or not payer_id:
        return render(request, 'payment_failed.html', {'error': 'Missing payment credentials.'})
        
    try:
        paypal_payment = paypalrestsdk.Payment.find(payment_id)
        if paypal_payment.execute({"payer_id": payer_id}):
            customer_name = request.session.get('paypal_customer', 'Unknown')
            email = request.session.get('paypal_email', '')
            amount = request.session.get('paypal_amount', '0')
            description = request.session.get('paypal_desc', 'PayPal Payment')
            
            our_order_id = generate_order_id()
            
            payment = Payment.objects.create(
                customer_name=customer_name,
                email=email,
                order_id=our_order_id,
                transaction_id=paypal_payment.id,
                amount=amount,
                gateway='PAYPAL',
                status='SUCCESS',
                payment_mode='PayPal',
                raw_response=str(paypal_payment)
            )
            
            # Clear session
            for key in ['paypal_customer', 'paypal_email', 'paypal_amount', 'paypal_desc', 'paypal_payment_id']:
                request.session.pop(key, None)
                
            context = {
                'payment': payment,
                'gateway': 'PayPal',
                'description': description,
            }
            return render(request, 'payment_success.html', context)
        else:
            print(f"PayPal Execute Error: {paypal_payment.error}")
            return render(request, 'payment_failed.html', {'error': paypal_payment.error})
    except Exception as e:
        print(f"PayPal Success Exception: {e}")
        return render(request, 'payment_failed.html', {'error': str(e)})

# PayPal Cancel Handler
def paypal_cancel(request):
    return render(request, 'payment_failed.html', {'error': 'PayPal payment cancelled.'})
