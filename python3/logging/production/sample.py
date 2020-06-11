import logging

from make_logger import MakeLogger


logger = MakeLogger(__name__)


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
    try:
        result = x / y
    except ZeroDivisionError:
        # logger.error('Tried to divide by zero') # To log ERROR
        logger.exception('Tried to divide by zero') # To log Traceback
    else:
        return result


num_1 = 20
num_2 = 10


logger.info('-----------Arithmetic Operation--------------')

add_result = add(num_1, num_2)
logger.info('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
logger.info('sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
logger.error('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
logger.warn('Div: {} / {} = {}'.format(num_1, num_2, div_result))

