#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    new_list = my_list[:]
    map(multiply(new_list, number), new_list)
    return new_list


def multiply(new_list, number):
    for x in range(len(new_list)):
        new_list[x] = new_list[x] * number
    return new_list
