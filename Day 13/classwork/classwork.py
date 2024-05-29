
age = 16
if age < 18:
    print("Apply Discount")
print("Proceed to Payment")

budget = 100

if budget >= 150:
    print("I will buy a soccerball: ")
elif budget >= 100:
    print("I will buy boots")
elif budget >= 50:
    print("I will buy a pen")
else:
    print("I dont have enough money to buy one of there")


print("something random")


age = int(input("Enter your age: "))

if age >= 0 and age <18:
    print("You are kid")
elif age > 18 and age <50:
    print("You are an adult")
else:
    print("You're old")


enter_number=int(input("please enter number"))

if enter_number > 0:
    print("number is positive")
elif enter_number < 0:
    print("number is negative") 
else:
    print("numer equals 0")


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




language = ["jv", "c++" , "pythoni" , "ruby" , "c"]

print(language[0:4])
print(language[0:5:2])