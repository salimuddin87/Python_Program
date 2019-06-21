"""
In Python, property() is a built-in function that creates and returns a
property object. The signature of this function is
        property(fget=None, fset=None, fdel=None, doc=None)

where, fget is function to get value of the attribute,
fset is function to set value of the attribute,
fdel is function to delete the attribute and
doc is a string (like a comment).
As seen from the implementation, these function arguments are optional.
"""

class Celcius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print "Getting value"
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature less than -273 is not valid!")
        print "setting value"
        self._temperature = value


if __name__ == '__main__':
    man = Celcius()
    man.temperature = 37
    print man.temperature
    print man.to_fahrenheit()
