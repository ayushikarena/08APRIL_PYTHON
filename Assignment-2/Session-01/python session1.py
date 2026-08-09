# Task 1: Create fav_items list
fav_items = ["Kesariya", 21, 15.5, True]

print("Original fav_items:", fav_items)


# Task 2: Update song name and increase age by 1
fav_items[0] = "Tum Hi Ho"
fav_items[1] = fav_items[1] + 1

print("Updated fav_items:", fav_items)


# Task 3: Remove mobile data usage using del
del fav_items[2]

print("After removing mobile data usage:", fav_items)


# Task 4: Create weekend_plan list
weekend_plan = ["Watch a movie", "Go shopping", 2, "Meet friends", 500]

print("Original weekend_plan:", weekend_plan)

# Remove the last item using pop()
removed_item = weekend_plan.pop()

print("Removed item:", removed_item)
print("Updated weekend_plan:", weekend_plan)