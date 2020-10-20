"""
filter(function, sequence)
To filter out all the elements of a sequence for which the function returns True.
"""


num = range(0, 10)
print(num)

odd_num = list(filter(lambda x: x % 2, num))
print(odd_num)

even_num = list(filter(lambda x: x % 2 == 0, num))
print(even_num)
