# Task 1: Cricket scores using round()

scores = [56.7, 102.3, 88.9, 45.2, 120.8]

rounded_scores = []

for score in scores:
    rounded_scores.append(round(score))

print("Original scores:", scores)
print("Rounded scores:", rounded_scores)


# Task 2: Restaurant ratings using sorted()

ratings = [4.2, 3.8, 4.9, 2.5, 4.0]

descending_ratings = sorted(ratings, reverse=True)

print("\nOriginal ratings:", ratings)
print("Ratings in descending order:", descending_ratings)


# Task 3: Flipkart product names using sort()

products = ["Laptop", "Mobile Phone", "Headphones", "Smart Watch", "Keyboard"]

products.sort()

print("\nProducts sorted alphabetically:", products)


# Task 4: Zomato restaurants and delivery times using zip()

restaurants = ["Burger Hub", "Pizza Point", "Sushi House"]
delivery_times = [30, 25, 40]

print("\nRestaurant delivery times:")

for restaurant, time in zip(restaurants, delivery_times):
    print(f"{restaurant} - {time} min")


# Task 5: YouTube titles and rounded view counts

def rounded_views(titles, view_counts):
    return [
        (title, round(views / 1000) * 1000)
        for title, views in zip(titles, view_counts)
    ]


video_titles = [
    "Python Tutorial",
    "Django Course",
    "Learn GitHub",
    "Python Project"
]

view_counts = [125678, 89432, 456789, 231245]

result = rounded_views(video_titles, view_counts)

print("\nYouTube video views:")

for title, views in result:
    print(f"{title} - {views} views")