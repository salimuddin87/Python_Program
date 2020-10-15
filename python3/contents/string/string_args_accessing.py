# Accessing arguments by position
print('{0}, {1}, {2}'.format('a', 'b', 'c'))  # 'a, b, c'
print('{}, {}, {}'.format('a', 'b', 'c'))  # 2.7+ only

print('{2}, {1}, {0}'.format('a', 'b', 'c'))  # 'c, b, a'
print('{2}, {1}, {0}'.format(*'abc'))  # unpacking argument sequence will print 'c, b, a'
print('{0}, {1}, {0}'.format('abra', 'cad'))   # arguments' indices can be repeated 'abra, cad, abra'

# Accessing arguments by name
print('Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W'))
# 'Coordinates: 37.24N, -115.81W'

coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
print('Coordinates: {latitude}, {longitude}'.format(**coord))  # 'Coordinates: 37.24N, -115.81W'

# Accessing arguments attributes
c = 3-5j
print('The complex number {0} is formed from the real part {0.real} '
      'and the imaginary part {0.imag}.'.format(c))
# 'The complex number (3-5j) is formed from the real part 3.0 and the imaginary part -5.0.'


class Point(object):
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return 'Point({self.x}, {self.y})'.format(self=self)


print(str(Point(4, 2)))  # 'Point(4, 2)'

# Accessing arguments items
coord = (3, 5)
print('X: {0[0]};  Y: {0[1]}'.format(coord))  # 'X: 3;  Y: 5'

# Replacing %s and %r
print("repr() shows quotes: {!r}; str() doesn't: {!s}".format('test1', 'test2'))
# "repr() shows quotes: 'test1'; str() doesn't: test2"

# Aligning the text and specifying a width
print('{:<30}'.format('left aligned'))  # 'left aligned                  '
print('{:>30}'.format('right aligned'))  # '                 right aligned'
print('{:^30}'.format('centered'))  # '           centered           '
print('{:*^30}'.format('centered'))  # use '*' as a fill char. '***********centered***********'

# Replacing and specifying a sign
print('{:+f}; {:+f}'.format(3.14, -3.14))  # show it always like '+3.140000; -3.140000'
print('{: f}; {: f}'.format(3.14, -3.14))  # show a space for positive numbers ' 3.140000; -3.140000'
print('{:-f}; {:-f}'.format(3.14, -3.14))  # show only the minus -- same as '{:f}; {:f}' '3.140000; -3.140000'

# Replacing %x and %o and converting the value to different bases
# format also supports binary numbers
print("int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42))  # 'int: 42;  hex: 2a;  oct: 52;  bin: 101010'
# with 0x, 0o, or 0b as prefix:
print("int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42))
# 'int: 42;  hex: 0x2a;  oct: 0o52;  bin: 0b101010'

# using the comma as a thousands separator
print('{:,}'.format(1234567890))  # '1,234,567,890'

# Expressing a percentage
points = 19.5
total = 22
print('Correct answers: {:.2%}'.format(points/total))  # 'Correct answers: 88.64%'

# using type-specific formatting
import datetime
d = datetime.datetime(2010, 7, 4, 12, 15, 58)
print('{:%Y-%m-%d %H:%M:%S}'.format(d))  # '2010-07-04 12:15:58'
