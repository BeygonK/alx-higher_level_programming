#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return

    biggest = my_list[0]
    else:
        for i in my_list:
            if i > biggest:
                biggest = i
    return biggest
