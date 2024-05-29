def narcissistic(value):
    sum = 0
    for digit in str(value):
        sum += int(digit) ** len(str(value))
    return value == sum