# Task 1: Create my_profile tuple

my_profile = ("Ayushi", 22, "Pizza", False)

print("My Profile:", my_profile)


# Task 2: Tuple slicing
# Index: 0     1                  2             3          4
#        Shape  Blinding Lights    Believer      Senorita   Levitating

playlist = (
    "Shape of You",
    "Blinding Lights",
    "Believer",
    "Senorita",
    "Levitating"
)

# [1:4] means index 1, 2, and 3
print("\n2nd, 3rd and 4th songs:", playlist[1:4])


# Task 3: Convert tuple to list, add item, convert back to tuple

order = ("Burger", "Fries", "Coke")

order_list = list(order)

order_list.append("Ice Cream")

order = tuple(order_list)

print("\nFinal order:", order)


# Task 4: Create a mixed tuple

insta_post = (
    101,                       # post_id - int
    "ayushi_karena",           # username - string
    1250,                      # likes - int
    ["#python", "#coding"],    # hashtags - list
    True                       # is_public - boolean
)

print("\nInstagram Post:", insta_post)

print("\nType of each element:")

for element in insta_post:
    print(element, "->", type(element))


# Task 5: WhatsApp call durations

call_durations = (12, 5, 0, 20, 7, 3, 15)

# Convert tuple to list
call_list = list(call_durations)

# Keep only calls that are 5 minutes or longer
filtered_calls = [duration for duration in call_list if duration >= 5]

# Convert the filtered list back to tuple
call_durations = tuple(filtered_calls)

print("\nOriginal call durations:", (12, 5, 0, 20, 7, 3, 15))
print("Calls 5 minutes or longer:", call_durations)