import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FoodDeliveryAPI.settings')
django.setup()

from foodapp.models import City, Restaurant, MenuItem

def seed():
    print("Seeding database...")
    
    cities_data = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
    cities = {}
    
    for c_name in cities_data:
        city, _ = City.objects.get_or_create(name=c_name)
        cities[c_name] = city

    restaurants_data = [
        {
            'name': 'Joe\'s Pizza',
            'cuisine': 'Italian',
            'address': '7 Carmine St, New York',
            'city': cities['New York'],
        },
        {
            'name': 'Katz\'s Delicatessen',
            'cuisine': 'American',
            'address': '205 E Houston St, New York',
            'city': cities['New York'],
        },
        {
            'name': 'In-N-Out Burger',
            'cuisine': 'Fast Food',
            'address': '9149 S Sepulveda Blvd, Los Angeles',
            'city': cities['Los Angeles'],
        },
        {
            'name': 'Lou Malnati\'s Pizzeria',
            'cuisine': 'Pizza',
            'address': '439 N Wells St, Chicago',
            'city': cities['Chicago'],
        },
    ]

    restaurants = {}
    for r_data in restaurants_data:
        restaurant, _ = Restaurant.objects.get_or_create(
            name=r_data['name'], 
            defaults={'cuisine': r_data['cuisine'], 'address': r_data['address'], 'city': r_data['city']}
        )
        restaurants[r_data['name']] = restaurant

    menu_items_data = [
        {'restaurant': 'Joe\'s Pizza', 'name': 'Cheese Slice', 'description': 'Classic NY cheese slice', 'price': 3.50},
        {'restaurant': 'Joe\'s Pizza', 'name': 'Pepperoni Slice', 'description': 'Classic NY pepperoni slice', 'price': 4.50},
        {'restaurant': 'Katz\'s Delicatessen', 'name': 'Pastrami on Rye', 'description': 'Legendary pastrami sandwich', 'price': 25.95},
        {'restaurant': 'In-N-Out Burger', 'name': 'Double-Double', 'description': 'Two patties, two slices of cheese', 'price': 5.50},
        {'restaurant': 'Lou Malnati\'s Pizzeria', 'name': 'Deep Dish Classic', 'description': 'Chicago deep dish with sausage', 'price': 28.00},
    ]

    for item_data in menu_items_data:
        MenuItem.objects.get_or_create(
            restaurant=restaurants[item_data['restaurant']],
            name=item_data['name'],
            defaults={'description': item_data['description'], 'price': item_data['price']}
        )

    print("Database seeded successfully!")

if __name__ == '__main__':
    seed()
