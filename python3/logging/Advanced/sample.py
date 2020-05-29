import logging
# import employee

# When we import employee, it become root logger i.e. 
# it did not log sample.py bebug We need to make info logging in it '

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('test.log')
file_handler.setLevel(logging.ERROR) # To log ERROR
file_handler.setFormatter(formatter)

# To log in terminal
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler) # To log Traceback


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
num_2 = 0

add_result = add(num_1, num_2)
logger.info('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
logger.info('sub: {} + {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
logger.debug('Mul: {} + {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
logger.debug('Div: {} + {} = {}'.format(num_1, num_2, div_result))
