# Program Name: basic_list.py
# Program Author: Russell Holmes
# Date: 11/12/2020


# initializes a list of user input
def make_list():
    a = []
    for i in range(0, 3, 1):
        foo = get_input()
        if foo.isnumeric() != 1:
            raise ValueError
        else:
            a.append(int(foo))
            # a.index(a.length, foo)
    return a


# returns specified input
def get_input():
    return input()
