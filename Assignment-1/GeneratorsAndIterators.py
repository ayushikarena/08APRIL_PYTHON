#Write a generator function that generates the first 10 even numbers

def even_numbers():
    for i in range(1, 11):
        yield i * 2

for num in even_numbers():
    print(num)


print("----------------------------------")
#Write a Python program that uses a custom iterator to iterate over a list of integers.
class MyNumbers:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 5:
            x = self.num
            self.num += 1
            return x
        else:
            raise StopIteration

for i in MyNumbers():
    print(i)