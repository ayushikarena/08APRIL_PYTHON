# seed_data.py
# Extended sample dataset script populating diverse food varieties and restaurants.

import os
import django

# Setup Django Environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant_project.settings')
django.setup()

from restaurants.models import Restaurant

def populate_food_varieties():
    extended_sample_data = [
        # Indian Varieties
        {
            "name": "Royal Spice Biryani House",
            "cuisine": "Indian",
            "location": "Downtown",
            "rating": 4.9,
            "description": "Hyderabadi Dum Biryani, Paneer Tikka Masala, Tandoori Roti, and Butter Chicken.",
            "image_url": "https://images.unsplash.com/photo-1585937421612-70a008356fbe?auto=format&fit=crop&w=600&q=80"
        },
        {
            "name": "South Junction Dosa Corner",
            "cuisine": "Indian",
            "location": "Westside",
            "rating": 4.7,
            "description": "Crispy Masala Dosa, Idli Sambar, Medu Vada, and Filter Coffee.",
            "image_url": "https://images.unsplash.com/photo-1610192244261-3f33de3f55e4?auto=format&fit=crop&w=600&q=80"
        },
        # Italian Varieties
        {
            "name": "Bella Italia Pizzeria",
            "cuisine": "Italian",
            "location": "Westside",
            "rating": 4.8,
            "description": "Wood-fired Neapolitan pizza, Creamy Alfredo Pasta, and homemade Tiramisu.",
            "image_url": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&w=600&q=80"
        },
        {
            "name": "Trattoria Pasta & Wine",
            "cuisine": "Italian",
            "location": "Uptown",
            "rating": 4.6,
            "description": "Handcrafted Ravioli, Lasagna Bolognese, Garlic Bread, and Gelato.",
            "image_url": "https://images.unsplash.com/photo-1551183053-bf91a1d81141?auto=format&fit=crop&w=600&q=80"
        },
        # Japanese Varieties
        {
            "name": "Sakura Sushi Bar & Ramen",
            "cuisine": "Japanese",
            "location": "Downtown",
            "rating": 4.9,
            "description": "Salmon Nigiri, Dragon Rolls, Tonkotsu Pork Ramen, and Matcha Ice Cream.",
            "image_url": "https://images.unsplash.com/photo-1579871494447-9811cf80d66c?auto=format&fit=crop&w=600&q=80"
        },
        {
            "name": "Tokyo Tempura & Bento",
            "cuisine": "Japanese",
            "location": "Eastside",
            "rating": 4.5,
            "description": "Shrimp Tempura Bento, Teriyaki Chicken Rice Bowl, Miso Soup, and Gyoza.",
            "image_url": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?auto=format&fit=crop&w=600&q=80"
        },
        # Mexican Varieties
        {
            "name": "El Taco Loco & Grill",
            "cuisine": "Mexican",
            "location": "Eastside",
            "rating": 4.6,
            "description": "Carne Asada Tacos, Loaded Cheesy Burritos, Fresh Guacamole, and Churros.",
            "image_url": "https://images.unsplash.com/photo-1565299585323-38d6b0865b47?auto=format&fit=crop&w=600&q=80"
        },
        {
            "name": "Fiesta Quesadilla Club",
            "cuisine": "Mexican",
            "location": "Downtown",
            "rating": 4.4,
            "description": "Sizzling Fajitas, Chicken Quesadillas, Nachos Supreme, and Sangria.",
            "image_url": "https://images.unsplash.com/photo-1513456852971-30c0b8199d4d?auto=format&fit=crop&w=600&q=80"
        },
        # American Varieties
        {
            "name": "Burger Craft & Smokehouse",
            "cuisine": "American",
            "location": "Uptown",
            "rating": 4.7,
            "description": "Double Smash Cheeseburgers, Truffle Loaded Fries, BBQ Pulled Pork, and Thick Milkshakes.",
            "image_url": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=600&q=80"
        },
        {
            "name": "The American Diner 1950",
            "cuisine": "American",
            "location": "Westside",
            "rating": 4.5,
            "description": "Crispy Buffalo Wings, Club Sandwich, Mac & Cheese, and Apple Pie.",
            "image_url": "https://images.unsplash.com/photo-1550547660-d9450f859349?auto=format&fit=crop&w=600&q=80"
        },
        # Chinese Varieties
        {
            "name": "Golden Dragon Wok",
            "cuisine": "Chinese",
            "location": "Uptown",
            "rating": 4.6,
            "description": "Schezwan Hakka Noodles, Kung Pao Chicken, Steamed Dim Sum, and Manchow Soup.",
            "image_url": "https://images.unsplash.com/photo-1525755662778-989d0524087e?auto=format&fit=crop&w=600&q=80"
        },
        # Thai Varieties
        {
            "name": "Bangkok Street Thai",
            "cuisine": "Thai",
            "location": "Downtown",
            "rating": 4.8,
            "description": "Authentic Pad Thai Noodles, Spicy Green Curry, Tom Yum Soup, and Mango Sticky Rice.",
            "image_url": "https://images.unsplash.com/photo-1559314809-0d155014e29e?auto=format&fit=crop&w=600&q=80"
        },
        # Mediterranean Varieties
        {
            "name": "Olive Tree Mediterranean",
            "cuisine": "Mediterranean",
            "location": "Eastside",
            "rating": 4.7,
            "description": "Fresh Hummus & Pita, Crispy Falafel Wraps, Chicken Shawarma, and Baklava.",
            "image_url": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=600&q=80"
        },
        # Desserts & Beverages
        {
            "name": "Sweet Delights Bakery & Cafe",
            "cuisine": "Desserts",
            "location": "Westside",
            "rating": 4.9,
            "description": "Chocolate Fudge Cake, Belgian Waffles, French Macarons, and Iced Caramel Latte.",
            "image_url": "https://images.unsplash.com/photo-1551024709-8f23befc6f87?auto=format&fit=crop&w=600&q=80"
        }
    ]

    print("Seeding database with expanded food varieties and restaurants...")
    for item in extended_sample_data:
        restaurant, created = Restaurant.objects.get_or_create(
            name=item["name"],
            defaults=item
        )
        if not created:
            restaurant.cuisine = item["cuisine"]
            restaurant.location = item["location"]
            restaurant.rating = item["rating"]
            restaurant.description = item["description"]
            restaurant.image_url = item["image_url"]
            restaurant.save()
            print(f"Updated: {restaurant.name}")
        else:
            print(f"Created: {restaurant.name}")

    print("All food varieties successfully populated!")

if __name__ == "__main__":
    populate_food_varieties()
