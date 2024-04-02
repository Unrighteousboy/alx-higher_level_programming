#!/usr/bin/python3

def safe_print_division(a, b):
    result = None

    try:
        result = a/b
        print("Inside Result: {}".format(result))
    except:
        print("Inside Result: {}".format(result))
    finally:
        return result
