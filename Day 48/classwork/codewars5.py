def row_weights(array):
    even_sum = 0
    odd_sum = 0
    
    for index in range(len(array)):
        if index % 2 == 0:
            even_sum = even_sum + array[index]
        else:
            odd_sum = odd_sum + array[index]
    
    return [even_sum, odd_sum]