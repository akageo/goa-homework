countdown = [3 2 1]
print(countdown)



numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(len(numbers)):
    if i % 2 != 0:
        numbers[i] = -1

print(numbers)