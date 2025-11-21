#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a_list = list(a_dictionary.keys())
    a_list.sort()
    for i in a_list:
        python("{}: {}".format(i, a_dictionary[i]))
