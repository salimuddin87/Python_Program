
f = open('write_file.txt', 'w')
print(f)  # <_io.TextIOWrapper name='write_file.txt' mode='w' encoding='cp1252'>
f.close()
"""
Methods of file objects
1. f.read(size)
To read a file’s contents, call f.read(size), which reads some quantity of data and returns it as a string.
size is an optional numeric argument. When size is omitted or negative, the entire contents of the file 
will be read and returned; it’s your problem if the file is twice as large as your machine’s memory. 
Otherwise, at most size bytes are read and returned. If the end of the file has been reached, f.read() 
will return an empty string ("").
"""
f = open('read_file.txt', 'r')
f.read()  # 'This is the entire file.\n'
f.read()  # ''
f.close()

"""
2. f.readline()
f.readline() reads a single line from the file; a newline character (\n) is left at the end of the string, 
and is only omitted on the last line of the file if the file doesn’t end in a newline. This makes the 
return value unambiguous; if f.readline() returns an empty string, the end of the file has been reached,
while a blank line is represented by '\n', a string containing only a single newline.
"""
f = open('read_file.txt', 'r')
f.readline()  # 'This is the first line of the file.\n'
f.readline()  # 'Second line of the file\n'
f.readline()  # ''
f.close()

"""
For reading lines from a file, you can loop over the file object. 
This is memory efficient, fast, and leads to simple code:
"""
f = open('read_file.txt', 'r')
for line in f:
    print(line)
f.close()

"""
output:-
This is the first line.
This is the second line.
"""

# Note:- If you want to read all the lines of a file in a list you can also use list(f) or f.readlines().

"""
3. f.write(string)
f.write(string) writes the contents of string to the file, returning None.
"""
f = open('write_file.txt', 'w')
f.write('This is a test\n')
value = ('the answer', 42)
s = str(value)
f.write(s)
f.close()

f = open('write_file.txt', 'r+')
f.write('0123456789abcdef')
f.seek(5)      # Go to the 6th byte in the file
f.read(1)  # '5'
# f.seek(-3, 2)  # Go to the 3rd byte before the end
f.read(1)  # 'd'
f.close()

"""
It is good practice to use the with keyword when dealing with file objects. This has the advantage that 
the file is properly closed after its suite finishes, even if an exception is raised on the way. It is 
also much shorter than writing equivalent try-finally blocks:
"""
with open('read_file.txt', 'r') as f:
    read_data = f.read()
