#pattern 1
for i in range(1, 6):
    for j in range(i):
        print("*", end=' ')
    print(" ")



print("------------------------------")
#pattern 3
for i in range(1, 6):
    for j in range(i):
        print(i, end=' ')
    print(" ")


print("------------------------------")
#pattern 4
for i in range(1, 6):
    for j in range(i):
        print(j+1, end=' ')
    print(" ")


print("------------------------------")
#pattern 5
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end=' ')
    print(" ")

print("------------------------------")
#pattern 6
n=1
for i in range(1,6):
    for j in range(i):
        print(n, end=' ')
        n+=1
    print(" ")


print("------------------------------")
#pattern 7 
"""a
a b
a b c"""
for i in range(1, 6):
    for j in range(i):
        print(chr(97 + j), end=' ')
    print(" ")
