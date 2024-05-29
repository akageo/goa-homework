# age = int(input("Please enter your age: "))

# if age < 18:
#     print("You are child")
# elif age >= 18 and age < 65:
#     print("You are adult")
# else:
#     print("You are old")


# for i in range(5):
#     number = int(input("Please enter number: "))

#     if number % 2 == 0:
#         print(number,"is even")
#     else:
#         print(number,"is odd")

# num = 1

# while num < 10:
#     print(num)
#     num = num + 1


# grade = input("Please enter grade (A,B,C,D or F): ")

# if grade == "A":
#     print("Excellent!")
# elif grade == "B":
#     print("Good job!")
# elif grade == "C":
#     print("You passed.")
# elif grade == "D":
#     print("You can do better.")
# else:
#     print("You failed.")


# num = 4
# count = 0
# number = 0

# while number != num:
#     number = int(input("Please enter number (1-10): "))
#     count = count + 1
#     if number == num:
#         print("You guessed number in",count,"try")


# for i in range(5, 50 + 1, 5):
#     print(i)

# language = ["css", "c++" , "pythoni" , "ruby" , "c"]

# print(language[2])

# favorite = language[0]

# print(language[0])

# print(language[-5])









# დავალება1) შევქმნათ სია საყვარელი კინოების ან სერიალების,რომელსაც შევინახავთ ცვლადში. საბოლოოდ გამოვიტანოთ სია.
favourite_movies = ["chinuri zodiaqo",  "harry potter" , "hobbit"]
print(favourite_movies)

# დავალება2) სიიდან დავბეჭდოთ ერთი კონკრეტული მნიშვნელობა index-ით
print(favourite_movies[2])

# დავალება 3) შევქმნათ მეორე ცვლადი, რომლის სახელი იქნება საყვარელი კინო და მის მნიშვნელობას წინა სიიდან წამოვიღებთ
favourite_film = (favourite_movies[1])

# დავალება4) მასივიდან ბოლო ელემენტი უარყოფითი index-ით წამოიღეთ. ასევე გამოიტანეთ ბოლოდან მეორე ელემენტი, ისევ მინუსიანი ინდექსით
favourite_film = (favourite_movies[-2])

# დავალება5) მომხმარებელს შევეკითხოთ საყვარელი მანქანის ბრენდი, რომელსაც შევინახავთ ცვლადში. შემდეგ ეს ცვლადი ჩასვით სიაში და გამოვიტანოთ print-ით, მაგ: print([brand_variable_name_here])
car_brends = ["bmw" , "audi", "golfi" , "mersedes"]

car_brend =input("what is your favourite car brend ")




language = ["css", "c++" , "pythoni" , "ruby" , "c"]

print(language[0:4])
print(language[0:5:2])




my_arrary = []
for number in range(50, 101):

    my_arrary.append(number)

    print(my_arrary[-10:])
