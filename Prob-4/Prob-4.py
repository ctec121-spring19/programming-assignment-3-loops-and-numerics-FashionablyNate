# Module 2
#   Programming Assignment 3
#     Prob-4.py

# Nathan Spelts

def main():
    print("\nStudent Output")
    # write code that will sum the numbers between 15 and 30 inclusive
    # and print the sum
    sum = 0
    for i in range(15, 31):
        sum = sum + i
    print("sum:", sum)
    # sum the numbers in the sequence [2, 4, 7, 9, 12, 14, 17, 19]
    # and print the sum
    sum = 0
    for i in [2, 4, 7, 9, 12, 14, 17, 19]:
        sum = sum + i
    print("sum:", sum)
    # use the randrange() function to sum 5 randomly generated numbers
    # between 1 and 99 inclusive.
    from random import randrange
    a = randrange(1, 100)
    b = randrange(1, 100)
    c = randrange(1, 100)
    d = randrange(1, 100)
    e = randrange(1, 100)
    sum = a + b + c + d + e
    # Print each random number on a line. 
    # Print the sum on the last line
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print("sum:", sum)
print()
main()
