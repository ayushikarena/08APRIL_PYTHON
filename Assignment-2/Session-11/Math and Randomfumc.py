import math
import random


# --------------------------------------------------
# Task 1: Square roots using math.sqrt()
# --------------------------------------------------

numbers = [16, 49, 81]

print("Task 1 - Square Roots:")

for number in numbers:
    print("Square root of", number, "=", math.sqrt(number))


# --------------------------------------------------
# Task 2: Flipkart-style price rounder
# Using math.ceil()
# --------------------------------------------------

prices = [199.1, 349.8, 599.3]

print("\nTask 2 - Rounded-up prices:")

for price in prices:
    rounded_price = math.ceil(price)
    print(price, "->", rounded_price)


# --------------------------------------------------
# Task 3: Zomato order bill calculator
# Apply 10% discount and round down
# --------------------------------------------------

bill_amount = 1249.75

discount = bill_amount * 0.10
final_bill = bill_amount - discount

rounded_bill = math.floor(final_bill)

print("\nTask 3 - Zomato Bill:")
print("Original bill:", bill_amount)
print("10% discount:", discount)
print("Final bill:", final_bill)
print("Bill after rounding down:", rounded_bill)


# --------------------------------------------------
# Task 4: Dice roll using random.randint()
# --------------------------------------------------

dice = random.randint(1, 6)

print("\nTask 4 - Dice Roll:")
print("You rolled:", dice)


# --------------------------------------------------
# Task 5: Spotify-style playlist shuffle
# Using random.sample()
# --------------------------------------------------

songs = [
    "Kesariya",
    "Shape of You",
    "Believer",
    "Blinding Lights",
    "Perfect",
    "Tum Hi Ho",
    "Chaleya",
    "Apna Bana Le"
]

today_playlist = random.sample(songs, 3)

print("\nTask 5 - Today's Playlist:")

for song in today_playlist:
    print("-", song)