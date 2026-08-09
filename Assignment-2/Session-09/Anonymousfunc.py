# --------------------------------------------------
# Task 1: Lambda to calculate square
# --------------------------------------------------

square = lambda number: number * number

print("Task 1 - Squares:")

for number in range(1, 6):
    print(number, "->", square(number))


# --------------------------------------------------
# Task 2: Lambda with map()
# Add 10% service charge
# --------------------------------------------------

prices = [120, 250, 99, 180, 310]

updated_prices = list(
    map(lambda price: price + (price * 0.10), prices)
)

print("\nTask 2 - Prices after 10% service charge:")
print(updated_prices)


# --------------------------------------------------
# Task 3: Lambda with filter()
# Get usernames with more than 1000 followers
# --------------------------------------------------

users = [
    ("raj", 800),
    ("simran", 1500),
    ("veer", 1200),
    ("ananya", 950)
]

verified_users = list(
    filter(lambda user: user[1] > 1000, users)
)

print("\nTask 3 - Users with more than 1000 followers:")

for username, followers in verified_users:
    print(username, "-", followers, "followers")


# --------------------------------------------------
# Task 4: Lambda returning sum and product
# --------------------------------------------------

calculate = lambda a, b: (a + b, a * b)

pairs = [(3, 4), (5, 2), (7, 8)]

print("\nTask 4 - Sum and Product:")

for a, b in pairs:
    result = calculate(a, b)

    print(
        f"Pair: ({a}, {b}) -> "
        f"Sum: {result[0]}, Product: {result[1]}"
    )


# --------------------------------------------------
# Task 5: Lambda to check palindrome
# --------------------------------------------------

is_palindrome = lambda text: text == text[::-1]

words = ["madam", "python", "noon"]

print("\nTask 5 - Palindrome check:")

for word in words:
    print(word, "->", is_palindrome(word))