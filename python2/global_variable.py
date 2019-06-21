"""
Global variable declaration and uses
"""

GLOBAL_VAR = 10


def change_var():
    """
    Modify global variable
    """

    global GLOBAL_VAR
    GLOBAL_VAR = 20


def print_global():
    """
    Display global variable
    """

    print "Inside printGlobal : ", GLOBAL_VAR


if __name__ == '__main__':

    change_var()
    print 'Inside main : ', GLOBAL_VAR
    print_global()
