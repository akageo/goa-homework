cars = ["mercedes", "BMW", "Opel", "jiguli"] # მნიშვნელობების კოლექცია #list სია

print(cars)





cars = ["mercedes", "5", True, "BMW", "Opel", "jiguli"] # ლისტში მოქცეული ნებისმიერი რამე თავის ფუნქციას არ კარგავს

print(cars[1])

print(cars[-1])


The_list1 = ["nika", "saba", "rolandiko", "luka", "dato"]

The_list2 = ["mercedes", "BMW", "Opel", "jiguli", "lamborgin"]

print(The_list1[0])

print(The_list2[1])


cars = ["mercedes", "BMW", "Opel", "jiguli", 5+5]

print(cars)


name = "luka"

print(name[1])

cars = ["mercedes", "BMW", "Opel", "jiguli", 345]

numbers = range(5,10 + 1)

print(numbers[2])




print(len(name)) #გვიჩვენებს რამდენი ელემენტია სიაში

print(cars[len(cars) - 1])#ამ კოდით გამოაქ სიიდან ბოლო ელემენტი




#მძიმიდან მძიმის შორის რაც წერია ის ერთი ინდექსია






namess = ("luka", "saba") #tuple ასე არ დაწერო ლისტი თორე თაფლს მიიღებ


manga_names = ["One piece", "Naruto", "Bleach", "Dr stone", "one punch"]

print(manga_names[0:5:2]) #ყოველი მეორე ინდექსის გამოტანა



manga_names = ["One piece", "Naruto", "Bleach", "Dr stone", "one punch"]

print(manga_names[::3]) #ყოველი მესამე ინდექსის გამოტანა


languages = ["JS", "C++", "Python", "Ruby", "PHP"]

for item in languages:
    print(item)








def multiply_by_three(user_num):
    print(user_num * 3)

multiply_by_three(😎
multiply_by_three(15)
multiply_by_three(1)
multiply_by_three(3)
multiply_by_three(4)

-------------------------
from turtle import *

speed(50)
width(3)

for i in range(4):
    forward(200)
    left(90)

penup()
goto(0, 300)
pendown()

for i in range(4):
    forward(200)
    left(90)

penup()
goto(-300, 0)
pendown()

for i in range(4):
    forward(200)
    left(90)

penup()
goto(-300,300)
pendown()

for i in range(4):
    forward(200)
    left(90)

exitonclick()


def say_hi(user_name):
    return user_name + " gamarjoba"





print(say_hi("luka"))


a = say_hi("luka")
print(a)
print(a + " axla naxvamdis :D")





def say_hi(user_name):
    return user_name + " gamarjoba"



a = say_hi("luka")

print(a)
a.split()
print(a + " megesalme ukve")




print(6 % 2 == 0)




def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        print("Odd")


