# --------------------------------------------------
# Task 1: Count frequency of each character
# --------------------------------------------------

text = input("Enter a string: ")

char_frequency = {}

for char in text:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

print("\nCharacter frequency:")
print(char_frequency)


# --------------------------------------------------
# Task 2: Count words in a food delivery review
# --------------------------------------------------

review = """
I love Zomato because Zomato delivers food quickly.
The food is fresh and the delivery is fast.
I use Zomato when I want tasty food at home.
"""

# Convert to lowercase
review = review.lower()

# Remove punctuation
punctuation = ".,!?;:'\""

for symbol in punctuation:
    review = review.replace(symbol, "")

# Split text into words
words = review.split()

word_frequency = {}

for word in words:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

print("\nFood delivery review word frequency:")
print(word_frequency)


# --------------------------------------------------
# Task 3: word_freq_dict() function
# --------------------------------------------------

def word_freq_dict(text):

    text = text.lower()

    punctuation = ".,!?;:'\""

    for symbol in punctuation:
        text = text.replace(symbol, "")

    words = text.split()

    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


ipl_text = "Virat scored 100, Rohit scored 80, and Gill scored 50 in the IPL match"

print("\nIPL word frequency:")
print(word_freq_dict(ipl_text))


# --------------------------------------------------
# Task 4: Ignore common stopwords
# --------------------------------------------------

stopwords = ["the", "and", "in", "of", "a", "to", "is"]

def word_freq_without_stopwords(text):

    text = text.lower()

    punctuation = ".,!?;:'\""

    for symbol in punctuation:
        text = text.replace(symbol, "")

    words = text.split()

    frequency = {}

    for word in words:

        # Ignore stopwords
        if word in stopwords:
            continue

        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


print("\nWord frequency without stopwords:")
print(word_freq_without_stopwords(ipl_text))


# --------------------------------------------------
# Task 5: Character count function and sorting
# --------------------------------------------------

def char_count_dict(text):

    frequency = {}

    for char in text:

        if char.isalpha():

            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1

    return frequency


character_text = "Python Programming"

character_counts = char_count_dict(character_text)

print("\nCharacter frequency sorted alphabetically:")

for char in sorted(character_counts):
    print(char, ":", character_counts[char])