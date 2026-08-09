# Task 1: Playlist dictionary

playlist = {
    "Kesariya": 268,
    "Tum Hi Ho": 262,
    "Apna Bana Le": 295
}

# Update the duration of one song
playlist["Kesariya"] = 280

print("Updated playlist:", playlist)


# Task 2: Nested dictionary - User profiles

user_profiles = {
    "raj_07": {
        "followers": 1200,
        "following": 350,
        "posts": 45
    },
    "ananya_xo": {
        "followers": 2500,
        "following": 420,
        "posts": 78
    }
}

# Print followers of ananya_xo
print("\nAnanya's followers:", user_profiles["ananya_xo"]["followers"])


# Task 3: Zomato-style restaurant menu

restaurants = {
    "Burger Hub": {
        "cuisine": "Fast Food",
        "rating": 4.2
    },
    "Pizza Point": {
        "cuisine": "Italian",
        "rating": 4.0
    }
}

# Update Pizza Point's rating
restaurants["Pizza Point"]["rating"] = 4.5

print("\nRestaurant menu:")
print(restaurants)


# Task 4: IPL team squad

team = {
    "CSK": {
        "captain": "Dhoni",
        "players": 18
    },
    "MI": {
        "captain": "Rohit",
        "players": 17
    }
}

# Add GT team
team["GT"] = {
    "captain": "Hardik",
    "players": 16
}

print("\nIPL Teams and Captains:")

# Print team names and captains
for team_name, details in team.items():
    print(team_name, "-", details["captain"])