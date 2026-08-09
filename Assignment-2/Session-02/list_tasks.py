# Task 1: Playlist with song positions

playlist = ["Kesariya", "Tum Hi Ho", "Apna Bana Le", "Chaleya", "Tera Ban Jaunga"]

print("My Playlist:")

for i in range(len(playlist)):
    print(i + 1, playlist[i])


# Task 2: Print first three food items

foods = ["Pizza", "Burger", "Dosa", "Pasta", "Fries"]

print("\nFirst three food items:")

for i in range(3):
    print(foods[i])


# Task 3: Calculate total Flipkart cart value

prices = [299, 499, 150, 1200, 350]

total = 0

for price in prices:
    total = total + price

print("\nTotal cart value:", total)


# Task 4: WhatsApp-style unread messages counter

unread_counts = [2, 0, 15, 120, 5]

print("\nUnread messages:")

for count in unread_counts:
    if count > 99:
        print("99+")
    else:
        print(count)