# A finally clause is always executed before leaving the try statement, 
# whether an exception has occurred or not.

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("Result is ", result)
    finally:
        print("Executing finally clause")

divide(6, 2)
print("*" * 50)
divide(2, 0)
