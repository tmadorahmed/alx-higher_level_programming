#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """that is Print the first x elements of a list that are integers.

    Args:
        my_list (list): that is The list to print elements from.
        x (int): is The number of elements of my_list to print.

    Returns:
        The number of elements printed.
    """
    rt = 0
    for y in range(0, x):
        try:
            print("{:d}".format(my_list[y]), end="")
            rt += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (rt)
