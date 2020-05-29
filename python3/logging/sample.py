import logging

# 10 DEBUG , 20 INFO
# 30 WARNING , 40 ERROR, 50 CRITICAL

logging.basicConfig(filename="test.log", level=logging.DEBUG, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

def add(x, y):
    """ Add Function """
    return x + y

def subtract(x, y):
    """ Subtract Function """
    return x - y

def multiply(x, y):
    """ Multiply Function """
    return x * y

def divide(x, y):
    """ Divide Function """
    return x / y

num_1 = 20
num_2 = 10

add_result = add(num_1, num_2)
logging.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
logging.debug('sub: {} + {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
logging.debug('Mul: {} + {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
logging.debug('Div: {} + {} = {}'.format(num_1, num_2, div_result))
