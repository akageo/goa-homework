score = int(input("enter your score: "))


while score >= 90 or score >= 100 :
    print("Excellent!")
    score = int(input("enter your score: "))

if score >= 80 or score >= 89:
    print("Good job!")
    score = int(input("enter your score: "))
if score >= 70 or score >= 79:
    print("You passed.")
    score = int(input("enter your score: "))
elif score >= 60 or score >= 69:
    print("You can do better.")
    score = int(input("enter your score: "))
else:
    print(f"{59 <=59}You failed.")
    score = int(input("enter your score: "))


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