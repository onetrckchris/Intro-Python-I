# Experiment with positional arguments, arbitrary arguments, and keyword
# arguments.

# Write a function f1 that takes two integer positional arguments and returns
# the sum. This is what you'd consider to be a regular, normal function.

# YOUR CODE HERE
def f1(num1, num2):
    return num1+num2

print(f1(1, 2))

# Write a function f2 that takes any number of integer arguments and prints the
# sum. Google for "python arbitrary arguments" and look for "*args"

# YOUR CODE HERE
def f2(*nums):
    sum = 0
    for num in nums:
        if isinstance(num, list):
            for list_num in num:
                sum = sum + list_num
        else:
            sum = sum + num
    return sum

print(f2(1))                    # Should print 1
print(f2(1, 3))                 # Should print 4
print(f2(1, 4, -12))            # Should print -7
print(f2(7, 9, 1, 3, 4, 9, 0))  # Should print 33

a = [7, 6, 5, 4]

# What thing do you have to add to make this work?
print(f2(a))    # Should print 22

# Write a function f3 that accepts either one or two arguments. If one argument,
# it returns that value plus 1. If two arguments, it returns the sum of the
# arguments. Google "python default arguments" for a hint.

# YOUR CODE HERE
def f3(num1, num2 = 0):
    if num2 != 0:
        return num1 + num2
    else:
        return num1 + 1

print(f3(1, 2))  # Should print 3
print(f3(8))     # Should print 9


# Write a function f4 that accepts an arbitrary number of keyword arguments and
# prints out the keys and values like so:
#
# key: foo, value: bar
# key: baz, value: 12
#
# Google "python keyword arguments".

# YOUR CODE HERE
def f4(**pairs):
    # if isinstance(arg1, dict):
    #     for key, value in arg1.items():
    #         print(f"key: {key}, value: {value}")
    # else:
    #     print('This function only iterates through dictionaries!')

    for key, value in pairs.items():
        print(f"key: {key}, value: {value}")

# Should print
# key: a, value: 12
# key: b, value: 30
f4(a=12, b=30)

# Should print
# key: city, value: Berkeley
# key: population, value: 121240
# key: founded, value: "March 23, 1868"
f4(city="Berkeley", population=121240, founded="March 23, 1868")

d = {
    "monster": "goblin",
    "hp": 3
}

# What thing do you have to add to make this work?
f4(**d)