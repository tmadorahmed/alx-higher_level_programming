#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """that Print x elememts of a list

    Args:
        my_list (list): The list to print elements from.
        x (int): That is the number of elements of my_list to print.

    Returns:
        number of elements printed.
    """
    rt = 0
    for y in range(x):
        try:
            print("{}".format(my_list[y]), end="")
            rt += 1
        except IndexError:
            break
    print("")
    return (rt)
