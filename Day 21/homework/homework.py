def bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25.0:
        return "Normal"
    elif bmi <= 30.0:
        return "Overweight"
    elif bmi > 30:
        return "Obese"

def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))

def square_digits(num):
    squareddigits_str = ""
    numstr = str(num)
    for digit in numstr:
        squareddigits_str += str(int(digit)**2)
    return int(squareddigits_str)

def solution(number):
    if number < 0:
        return 0
    summultiples = 0
    for num in range(number):
        if num % 3 == 0 or num % 5 == 0:
            summultiples += num
    return summultiples

def grow(arr):
    for number in arr[1:]:
        arr[0] *= number
    return arr[0]

def get_count(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for letters in sentence:
        if letters in vowels:
            count += 1
    return count if count > 0 else 0

def likes(names):
    num_likes = len(names)
    if num_likes == 0:
        return "no one likes this"
    elif num_likes == 1:
        return f"{names[0]} likes this"
    elif num_likes == 2:
        return f"{names[0]} and {names[1]} like this"
    elif num_likes == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {num_likes - 2} others like this"