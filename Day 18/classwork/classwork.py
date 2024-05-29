# def filter_evens(numbers):
#     filtered_list = []

#     for num in numbers:
#         if num >= 10 and num % 2 == 0:
#             filtered_list.append(num)

#     return filtered_list

# def sum_of_numbers(numbers):
#     sum = 0

#     for i in numbers:
#         sum = sum + i

#     return sum

# count = int(input("Please enter how many numbers do u want to input: "))

# numbers = []

# for i in range(count):
#     number = int(input("Please enter number: "))
#     numbers.append(number)


# print(sum_of_numbers(numbers))
# print(filter_evens(numbers))

# def sort_list(numbers):
#     for index in range(1,len(numbers)):
#         if numbers[index - 1] > numbers[index]:
#             [index], [index + 1] = [index + 1], [index]     

#     return numbers


# number = [1,5,3,3,6,2,9,7,8]

# print(sort_list(number))