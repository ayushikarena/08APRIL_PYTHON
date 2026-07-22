from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    path('', views.home, name='home'),
    path('book-ticket/', views.book_ticket, name='book_ticket'),
    path('payment-callback/', views.payment_callback, name='payment_callback'),
    path('food-order/', views.food_order, name='food_order'),
    path('stripe/success/', views.stripe_success, name='stripe_success'),
    path('stripe/cancel/',  views.stripe_cancel,  name='stripe_cancel'),
    path('paypal/',         views.paypal_pay,     name='paypal_pay'),
    path('paypal/success/', views.paypal_success, name='paypal_success'),
    path('paypal/cancel/',  views.paypal_cancel,  name='paypal_cancel'),
]
