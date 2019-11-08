# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE


def is_even(x):
    sum = None
    if x % 2 == 1:
        sum = False
    else:
        sum = True
    return print(sum)

is_even(2)
    # Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE


def oddEven(x):
    if x % 2 == 1:
        print('odd')
    else:
        print('even')


oddEven(num)
