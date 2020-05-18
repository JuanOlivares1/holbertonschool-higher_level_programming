def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for i in range(x):
            print("{}".format(my_list[i]))
            count += 1
        return count
    except IndexError as ex:
        return count
