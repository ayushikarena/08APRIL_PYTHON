from instahelpers import format_likes


counts = [500, 999, 1200, 1500, 2500, 1500000, 2300000]

for count in counts:
    print(count, "->", format_likes(count))