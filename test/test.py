# დაწერეთ პროგრამა, რომელიც იღებს მომხმარებლისგან მთელ რიცხვს და დაბეჭდავს მის გამრავლების ცხრილს 10-ის ჩათვლით. მაგ: x, x2, x3 ... x*10.

number = int(input("enter a number: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# second way

# num = (input("Enter a number: "))

# length = len(num)

# numbers_sum = 0
# for i in range(length):
#     numbers_sum = numbers_sum + int(num[i])

# print(numbers_sum)