# Task 1: Product names and prices using zip()

products = ["Laptop", "Mobile", "Headphones", "Keyboard"]
prices = [55000, 25000, 2000, 1200]

product_dict = dict(zip(products, prices))

print("Product dictionary:")
print(product_dict)


# Task 2: Instagram-style followers using a loop
# We are NOT using zip() here.

usernames = ["raj_07", "ananya_xo", "ayushi_22", "rohan_dev"]
followers = [1200, 2500, 1800, 950]

follower_dict = {}

for i in range(len(usernames)):
    follower_dict[usernames[i]] = followers[i]

print("\nFollower dictionary:")
print(follower_dict)


# Task 3: IPL teams with more than 10 points

teams = ["CSK", "MI", "GT", "RCB", "KKR"]
points = [14, 12, 8, 10, 16]

team_points = dict(zip(teams, points))

print("\nTeams with more than 10 points:")

for team, point in team_points.items():
    if point > 10:
        print(team, "-", point, "points")


# Task 4: Movies, genres and ratings using zip()

movie_titles = ["3 Idiots", "Dangal", "KGF", "Drishyam"]
genres = ["Comedy", "Sports Drama", "Action", "Thriller"]
ratings = [8.4, 8.3, 8.2, 8.5]

movies = []

for title, genre, rating in zip(movie_titles, genres, ratings):
    movie = {
        "title": title,
        "genre": genre,
        "rating": rating
    }

    movies.append(movie)

print("\nMovie list:")
print(movies)