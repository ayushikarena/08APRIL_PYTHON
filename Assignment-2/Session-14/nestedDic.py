# --------------------------------------------------
# Task 1: Dynamic Flipkart shopping cart
# --------------------------------------------------

cart = {}

# Add User 1
cart.setdefault("ayushi", [])
cart["ayushi"].append({
    "name": "Laptop",
    "quantity": 1,
    "price": 55000
})

cart["ayushi"].append({
    "name": "Mouse",
    "quantity": 2,
    "price": 800
})


# Add User 2
cart.setdefault("rahul", [])
cart["rahul"].append({
    "name": "Headphones",
    "quantity": 1,
    "price": 2000
})

cart["rahul"].append({
    "name": "Keyboard",
    "quantity": 1,
    "price": 1500
})


print("Task 1 - Flipkart Shopping Cart:")
print(cart)


# --------------------------------------------------
# Task 2: Spotify-style playlist
# --------------------------------------------------

playlists = {}


def add_song_to_playlist(
    playlists,
    user,
    playlist_name,
    song_title,
    artist
):
    # Create user if user does not exist
    playlists.setdefault(user, {})

    # Create playlist if playlist does not exist
    playlists[user].setdefault(playlist_name, [])

    # Add song
    playlists[user][playlist_name].append({
        "title": song_title,
        "artist": artist
    })


add_song_to_playlist(
    playlists,
    "ayushi",
    "Favourites",
    "Kesariya",
    "Arijit Singh"
)

add_song_to_playlist(
    playlists,
    "ayushi",
    "Favourites",
    "Tum Hi Ho",
    "Arijit Singh"
)

add_song_to_playlist(
    playlists,
    "rahul",
    "Chill",
    "Perfect",
    "Ed Sheeran"
)


print("\nTask 2 - Spotify Playlists:")
print(playlists)


# --------------------------------------------------
# Task 3: IPL cricket match scores
# --------------------------------------------------

ipl_scores = {}

# Add CSK players
ipl_scores.setdefault("CSK", {})

ipl_scores["CSK"]["Dhoni"] = 45
ipl_scores["CSK"]["Ruturaj"] = 78
ipl_scores["CSK"]["Jadeja"] = 32


# Add MI players
ipl_scores.setdefault("MI", {})

ipl_scores["MI"]["Rohit"] = 85
ipl_scores["MI"]["Surya"] = 62
ipl_scores["MI"]["Hardik"] = 40


print("\nTask 3 - IPL Scores:")
print(ipl_scores)

# Print a specific player's score
print("Rohit's runs:", ipl_scores["MI"]["Rohit"])


# --------------------------------------------------
# Task 4: Zomato orders
# --------------------------------------------------

orders = {
    101: {
        "restaurant": "Burger Hub",
        "items": ["Burger", "Fries"],
        "total": 450
    },
    102: {
        "restaurant": "Pizza Point",
        "items": ["Pizza", "Coke"],
        "total": 650
    }
}


# Function to add a new order
def add_order(orders, order_id, restaurant, items, total):

    orders[order_id] = {
        "restaurant": restaurant,
        "items": items,
        "total": total
    }


# Function to update order total
def update_total(orders, order_id, new_total):

    if order_id in orders:
        orders[order_id]["total"] = new_total
    else:
        print("Order not found")


add_order(
    orders,
    103,
    "Dosa Corner",
    ["Masala Dosa", "Coke"],
    300
)

update_total(orders, 103, 350)


print("\nTask 4 - Zomato Orders:")
print(orders)


# --------------------------------------------------
# Task 5: Fix KeyError using setdefault()
# --------------------------------------------------

playlists = {
    "user1": {
        "Favourites": ["Song1", "Song2"]
    }
}

# Create user2 if it doesn't exist
playlists.setdefault("user2", {})

# Create Chill playlist if it doesn't exist
playlists["user2"].setdefault("Chill", [])

# Now safely add Song3
playlists["user2"]["Chill"].append("Song3")


print("\nTask 5 - Updated Playlists:")
print(playlists)