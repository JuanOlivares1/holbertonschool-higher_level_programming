#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    resList = []
    for i in range(list_length):
        res = 0
        try:
            res = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            resList.append(res)
    return resList
