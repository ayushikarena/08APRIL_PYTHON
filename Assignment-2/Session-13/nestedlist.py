# --------------------------------------------------
# Task 1: Even numbers from 10 to 50
# --------------------------------------------------

even_numbers = [number for number in range(10, 51) if number % 2 == 0]

print("Task 1 - Even numbers:")
print(even_numbers)


# --------------------------------------------------
# Task 2: Song durations greater than 200 seconds
# Using nested list comprehension
# --------------------------------------------------

playlists = [
    [210, 180, 240],
    [150, 200],
    [300, 120, 90]
]

long_songs = [
    duration
    for playlist in playlists
    for duration in playlist
    if duration > 200
]

print("\nTask 2 - Durations greater than 200 seconds:")
print(long_songs)


# --------------------------------------------------
# Task 3: Product name and price above 1000
# --------------------------------------------------

names = ["Shoes", "Bag", "Watch", "Headphones"]
prices = [999, 1500, 700, 2200]

expensive_products = [
    (name, price)
    for name, price in zip(names, prices)
    if price > 1000
]

print("\nTask 3 - Products above 1000:")
print(expensive_products)


# --------------------------------------------------
# Task 4: Ratings above 4 from a matrix
# Flatten using nested list comprehension
# --------------------------------------------------

ratings = [
    [4, 5, 3, 2],
    [5, 4, 4, 3],
    [3, 2, 5, 5]
]

high_ratings = [
    rating
    for restaurant in ratings
    for rating in restaurant
    if rating > 4
]

print("\nTask 4 - Ratings above 4:")
print(high_ratings)