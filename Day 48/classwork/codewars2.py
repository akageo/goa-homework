def max_multiple(divisor, bound):
    if bound % divisor == 0:
        return bound
    
    multiples = []
    
    for num in range(divisor, bound):
        if num % divisor == 0:
            multiples.append(num)
    
    return max(multiples)