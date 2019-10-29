"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
poetry = open('foo.txt')
# print(poetry.read())

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE
bar_test = open('bar.txt', 'w')
bar_test.write('Is this working?\n')
bar_test.write('This should be working...\n')
bar_test.write('Yeah, I think it is working!')
bar_test.close()

bar_test = open('bar.txt')
print(bar_test.read())