from tkinter import Y
from typing import final
from unittest import result


try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')

def bool_return():
    try:
        return True
    finally:
        return False


#
def divide(x, y):
    try:
        result = x/y
    except ZeroDivisionError:
        print ("division by zero!")
    else:
        print("result is", result)
    finally:
        print("excuting finally clause")

