"""
Finally note that, the actual temperature value is stored in the private
variable _temperature. The attribute temperature is a property object which
provides interface to this private variable.
"""


class Celsius:

    def __init__(self, temperature=0):
        self.temperature = temperature
        # self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    # New method
    def get_temperature(self):
        print("Getting temperature")
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not valid!")
        print("Setting temperature")
        self._temperature = value

    temperature = property(get_temperature, set_temperature)


if __name__ == '__main__':
    man = Celsius()
    # Set temperature
    man.temperature = 37
    print("man.__dict__ : ", man.__dict__)
    # Get temperature
    print(man.temperature)
    # Convert to fahrenheit
    print(man.to_fahrenheit())
