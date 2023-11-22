#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """that is Divides two lists element by element.

    Args:
        my_list_1 (list): first list.
        my_list_2 (list): second list.
        list_length (int): number of elements to divide.

    Returns:
        new list of length list_length containing all the divisions.
    """
    new_list = []
    for i in range(0, list_length):
        try:
            division = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            division = 0
        except ZeroDivisionError:
            print("division by 0")
            division = 0
        except IndexError:
            print("out of range")
            division = 0
        finally:
            new_list.append(division)
    return (new_list)
