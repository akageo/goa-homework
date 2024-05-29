# დაწერეთ პროგრამა, რომელიც ეკითხება მომხმარებლის ასაკს და შემდეგ დაბეჭდავს შეტყობინებას ასაკის მიხედვით: using(if-elif-else)
# If the age is less than 18, print "You are a minor."
# If the age is between 18 and 65, print "You are an adult."
# If the age is 65 or older, print ""

age = int(input("Please enter your age: "))

if age <= 17:
    print("You are a minor.")
    age = int(input("Please enter your age: "))
if age >= 18 and age <= 65:
    print("You are an adult.")
    age = int(input("Please enter your age: "))
if age >= 65:
    print("You are a senior citizen.")


# შექმენით პროგრამა, რომელიც სთხოვს მომხმარებელს შეიყვანოს რიცხვი და შემდეგ დაბეჭდოს რიცხვი ლუწია თუ კენტი. გამოიყენეთ ფორ ციკლი, რომ სთხოვოთ მომხმარებელს 5 რიცხვი და შეამოწმეთ ხუთივე რიცხვი.

for _ in range(5):
    num = int(input("Enter a number: "))
    print("Even" if num % 2 == 0 else "Odd")


# დაწერეთ პროგრამა, რომელიც სთხოვს მომხმარებელს შეიყვანოს ქულები ასოებით (A, B, C, D ან F) და შემდეგ დაბეჭდოს შეტყობინება ასოების მიხედვით: using(if-elif-else)
# If the grade is A, print "Excellent!"
# If the grade is B, print "Good job!"
# If the grade is C, print "You passed."
# If the grade is D, print "You can do better."
# If the grade is F, print "You failed."

grade = input("please enter your grade : ")

if grade == "A":
   print("Excellent")
elif grade == "B":
   print("good job") 
elif grade == "C":
   print("you passed")
elif grade == "D":
    print("you can do better")
elif grade == "F":
   print("you failed") 
else:
   print("try again")

# დაწერეთ პროგრამა, რომელიც ბეჭდავს რიცხვებს 1-დან 10-მდე while ციკლის გამოყენებით

sum=0
while sum != 20:
    sum += 1
    print(sum)

# შექმენით პროგრამა, რომელიც სთხოვს მომხმარებელს გამოიცნოს რიცხვი 1-დან 10-მდე. გამოიყენეთ while loop, რათა გააგრძელოთ კითხვა, სანამ მომხმარებელი სწორად არ გამოიცნობს

import random

secret_number = random.randint(1, 10)

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break
    print("Sorry, that's not the correct number. Try again.")

# დაწერეთ პროგრამა, რომელიც დაბეჭდავს მოცემული რიცხვის (მაგ 5) პირველ 10 ჯერადს for loop-ის გამოყენებით.
    
number = 5

for i in range(1, 11):
    result = number * i
    print(result)

# შექმენით პროგრამა, რომელიც ბეჭდავს უკუთვლას 10-დან 1-მდე for loop-ის გამოყენებით.
    
for i in range(10, 0, -1):
    print(i)




# #1
# sum=0
# while sum != 10:
#     sum +=1
#     print(sum)

# #2
# sum=0
# while sum != 10:
#     sum += 2
#     print(sum)

#3
# num1=int(input("enter your number: "))
# if num1<0:
#     print("it's negative number")
# else: 
#     print("it is positive")

#4
# password="abc123"
# new_password=input("enter your password: ")
# if new_password == password:
#     print("access granted")
# else:
#     print("Access denied")

# #5 

# num_b = 1

# while num_b <= 10:
#     print(num_b)
#     if num_b == 5:
#         break
#     num_b += 1

# #6 

# # Loop until the user enters a valid input
# while True:
#     # Ask the user to enter a number
#     number = int(input("Please enter a number between 1 and 5: "))

#     # Check if the number is valid
#     if number < 1 or number > 5:
#         print("Invalid input. Please try again.")
#     else:
#         print("Valid input")
#         break
#  #7 

# inp_numb = int(input("please enter your chosen number: "))

# if inp_numb % 3 == 0:
#     print("Fizz")
# elif inp_numb % 5 == 0:
#     print("Buzz")
# elif inp_numb % 3 and inp_numb % 5:
#     print("FizzBuzz")
# else:
#     print(inp_numb)