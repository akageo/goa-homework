def replace(first,second,third):
    final_list = []
    for element in first:
        if element == second:
            final_list.append(third)
        else:
            final_list.append(element)
    return final_list

print(replace([15, 5, 5, 5], 5, 15))