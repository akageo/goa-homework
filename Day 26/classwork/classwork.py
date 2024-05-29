def my_range(start, end, step):
    numbers = []

    while start < end:
        numbers.append(start)
        start = start + step
    
    return numbers

print(my_range(0,10 + 1,2))