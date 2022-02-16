#string
# str1 = "apple"
# print(len(str1))


# str1 = "hellow"
# str2 = "world"
# print( str1+str2)
# print ( str1[2:6])
# print ( str1[::-1])

# name = "tintu";
# txt = "my name is {}"
# print(txt.format(name))
# print(name.index("n"))

# str = "123"
# print(str.isdigit())

# print(name.startswith("ap"))
# print(name.endswith("ap")) 

# x = bool(0)
# print(x)

# age = input("enter your age:")
# if age>=18:
#     print("eligible to vote")
# else:
#     print("not eligible to vote")

# fruits = ["apple",1,2,3]
# print(fruits[1])

# fruits = []
# fruits.append("apple")
# fruits.append("chilly")
# fruits.append("orange")
# fruits.append("mango")
 
# fruits.insert(0,"grapes")
# print(fruits)

# fruits = {"apple",1,2,3}
# print(fruits)


# fruits = {"apple","orange","banana"}
# for x in fruits:
#     print(x)

# fruits = {"apple","orange","banana"}
# fruits.add("graps")
# fruits.remove("orange")
# fruits.pop()
# print(fruits)

# std = {
#     "name" : "tintu",
#     "age" : 30,
#     "phone" : "1234567890"
# }

# print(std['age'])

# std = {
#     "name" : "tintu",
#     "age" : 30,
#     "phone" : "1234567890"
# }
# std.pop("phone")

# for x in std.values():
#     print(x)
  

# i = 1
# while i<=10:
#    print(i)
#    i = i + 1

# str = "welcome to programming"
# for x in "apple":
#     print(x)

# fruits = ["apple","mango","orange"]
# for i in fruits:
#     if i == "orange":
#         break
#     print(i)

# sum = 0
# for i in range(1,10):
#     sum = sum + 1
# print(sum)

# def sum(a,b):
#     c=a+b
#     return c
# print(sum(10,20))

# def fact(n):
#     f=1
#     for i in range(1,n+1):
#         f=f*i
#     return f

# print(fact(3))

# def smiley(msg):
#     emojis = {
#         "happy" : "😊",
#         "sad" : "😥"
#     }
#     words = msg.split(" ")
#     ret = ""
#     for word in words:
#         if word in emojis:
#             ret+= emojis[word]+" "
#         else:
#             ret+= word + " "
#     return ret

# x = input(" ")
# print(smiley(x))

# class std:

#     def __init__ (self,name,age):
#         self.name = name
#         self.age = age

#     def displayStudent(self):
#         print("name",self.name)
#         print("age",self.age)

# ob = std("tintu",30)
# ob.displayStudent()

# try:
#     age = int(input("Enter your age"))
# except NameError:
#     print("variable not defined")
# except ZeroDivisionError:
#     print("divide with 0 is not allowed")
# except:
#     print("error")


import calc
print (calc.mul(10,20))

