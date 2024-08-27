# Print numbers from 1 to 5 using a for loop
# for i in range(1, 6):
#     print(i)

# Print numbers from 1 to 5 using a while loop
# i = 1
# while i <= 5:
#     print(i)
#     i += 1

# functions
# def multiply_numbers(a,b):
#     return a*b
# result = multiply_numbers(23,8)
# print(f"the multiplication is {result}")

#lists

# fruits =['apple','banana','cherry']
# fruits.append('guava')
# print(fruits)
# fruits.remove('apple')
# print(fruits)
# fruits[1] = 'mango'# replacement 
# print(fruits)

# Dictionary
# student = {
#     "name":"Chhoti",
#     "age":"21",
#     "address":"kathmandu"
# }
# # print(student["name"])
# # print(student.get("age"))
# # student.update("name")
# student["grade"] ="A"
# print(student)
# student["age"] ="18"
# print (student)
# #update 


# question practice on list
#creating list
fruits = ['Apple','Banana','Mango','Cherry','Guava',]
print(fruits)
print(fruits[2])# accessing 3rd item from the list
fruits[1] ="Litchi"
print(fruits)
fruits.append("Pomigranet")
print(fruits)
fruits =["Apple"]+fruits
print(fruits)
fruits.remove("Pomigranet")
print(fruits)
length = len(fruits)
print(length)
print(fruits[:3])# slicing 
# for sorting
fruits.sort()
print("sorted list",fruits)

fruits.reverse()
print("reversed list ",fruits)

for fruit in fruits:
    print(fruit.upper())

vegitables =['carrot','spinich','couliflower','pumpkin']
combine = fruits + vegitables
print(combine)
print(fruits[1])
duplicate = list(set(fruits))
print(duplicate)

