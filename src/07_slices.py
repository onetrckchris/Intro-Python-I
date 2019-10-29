"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""

a = [2, 4, 1, 7, 9, 6]
b = [6, 2, 10, 1, 9]
c = 23

# a[start:stop]  items start through stop (exlusive)
# a[start:]      items start through the rest of the array
# a[:stop]       items from the beginning through stop (exlusive)
# a[:]           a copy of the whole array

# Output the second element: 4:
print(a[1])

# Output the second-to-last element: 9
print(a[-2])

# Output the last three elements in the array: [7, 9, 6]
print(a[-3:])

# Output the two middle elements in the array: [1, 7]
def slice_middle_elements(myList):
    if isinstance(myList, list):
        list_middle = len(myList)/2

    if not isinstance(myList, list):
        return 'Error: Must pass a list.'
    elif int(list_middle) == list_middle and isinstance(list_middle, float):
        return myList[int(list_middle-1):int(list_middle+1)]
    else:
        return myList[int(list_middle)] # This will round the float down.

print(slice_middle_elements(c))

# Output every element except the first one: [4, 1, 7, 9, 6]
print(a[1:])

# Output every element except the last one: [2, 4, 1, 7, 9]
print(a[:-1])

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
print(s[7:-1])