def descending_order(num):
    sorted_num = sorted(str(num))
    return int("".join(sorted_num[::-1]))