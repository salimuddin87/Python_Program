class fruits:
    def __init__(self, price):
        self.price = price

obj = fruits(50)

obj.quantity = 10
obj.bags = 2

print obj.quantity+len(obj.__dict__)
print obj.__dict__
