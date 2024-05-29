list1 = []
for i in range(0, 50):
    list1.append(i)

print(list1[:25])
print(list1[:25:3])

list2 = []
num = int(input("enter number: "))
for i in range(num, num + 10):
    list2.append(num)

print(list2[::2])