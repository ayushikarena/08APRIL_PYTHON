# --------------------------------------------------
# Task 1: Calculate total
# --------------------------------------------------

def calculate_total(price, quantity):
    return price * quantity


total = calculate_total(120, 3)

print("Task 1 - Total:", total)


# --------------------------------------------------
# Task 2: Format username
# --------------------------------------------------

def format_username(username, prefix="user_"):
    return prefix + username


# Calling without prefix - uses default value
username1 = format_username("ayushi")

# Calling with prefix
username2 = format_username("ayushi", "student_")


print("\nTask 2:")
print("Default prefix:", username1)
print("Custom prefix:", username2)


# --------------------------------------------------
# Task 3: Book movie ticket
# --------------------------------------------------

def book_movie_ticket(movie_name, seat_type="Regular", snacks=None):

    print("\nBooking Summary")
    print("Movie:", movie_name)
    print("Seat Type:", seat_type)

    if snacks is None:
        print("Snacks: No snacks")
    else:
        print("Snacks:", snacks)


# Only positional arguments
book_movie_ticket("Jawan", "Regular", "Popcorn")


# Only keyword arguments
book_movie_ticket(
    movie_name="Pathaan",
    seat_type="VIP",
    snacks="Nachos"
)


# Mix of positional and keyword arguments
book_movie_ticket(
    "Jawan",
    seat_type="Premium",
    snacks="Popcorn and Coke"
)


# Using default seat type and snacks
book_movie_ticket("Pathaan")


# --------------------------------------------------
# Task 4: Apply coupon
# --------------------------------------------------

def apply_coupon(amount, coupon_code=None):

    if coupon_code == "SAVE10":
        discount = amount * 0.10
        final_amount = amount - discount
        return final_amount

    return amount


# Without coupon
price_without_coupon = apply_coupon(1000)

# With SAVE10 coupon
price_with_coupon = apply_coupon(1000, "SAVE10")


print("\nTask 4:")
print("Amount without coupon:", price_without_coupon)
print("Amount with SAVE10:", price_with_coupon)