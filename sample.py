# string
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


# import calc
# print (calc.mul(10,20))


# <---------------------------------------------------- assignment -------------------------------------------------------->
# no:1

c = input("enter number")
print(c)

# no:2

a = input("enter number")
b = input("enter number")
sum = int(a) + int(b)
print(sum)

# no:3

p = input("enter number")
r = input("enter number")
n = input("enter number")
SI = (int(p)*int(r)*int(n))/100
print(SI)

# no:4

a = input("enter mark")
if int(a)<50:
    print("failed")
else:
    print("passed")

# no:5

a = input("enter mark")
if int(a)>=90:
    print("A")
elif int(a)>=80:
    print("B")
elif int(a)>=70:
    print("C")
elif int(a)>=60:
    print("D")
elif int(a)>=50:
    print("E")
else:
    print("failed")

# no:6

a = input("enter number")
if int(a) == 1:
    print("Sunday")
elif int(a) == 2:
    print("Monday")
elif int(a) == 3:
    print("Tuesday")
elif int(a) == 4:
    print("Wednesday")
elif int(a) == 5:
    print("Thursday")
elif int(a) == 6:
    print("Friday")
elif int(a) == 7:
    print("Saturday")
else:
    print("Invalid Entry")

# no:7

num = 5
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)

# no:8

a = input("enter a number:")
sum = 0
for num in range(1, int(a) + 1):
    if num % 2 != 0:
        sum = sum + num
print(sum)

# no:9

def num(n):
	num = 1
	for i in range(0, n):
		num = 1
		for j in range(0, i+1):
			print(num, end=" ")
			num = num + 1
		print("\r")
n = 5
num(n)

# no:10

a = [1,2,3]
b = [4,5,6]
a,b = b,a
print(a)
print(b)

# no:11

a = [11,20,34,50,33]
c = 0  
for num in a: 
    if num % 2 == 0:
        c = c + 1
        print(num,end=",")
print("\n")
print(c)

# no:12

num = [20, 10, 50, 30, 40]
num.sort(reverse=True)
print(num)

# no:13

s = input("enter a string")
if  s == s[::-1]:
    print("Yes")
else:
    print("No")

# no:14

a = [3, 2, 1]
b = [1, 2, 3]  
out_arr = int(a) + int(b)  
print (out_arr)  

# no:15

lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    e = int(input())
    lst.append(e)     
print(lst)

# no:16

number = int(input("Enter any number: "))
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
    else:
        print(number, "is a prime number")
else:
    print(number, "is not a prime number")

# no:17
 
import calc
print (calc.sub(10,20))
print (calc.add(10,20))
print (calc.mul(10,20))
print (calc.div(10,20))

# no:18

wt = float(input("Please enter written test: "))
le = float(input("Please enter Math lab exams: "))
ass = float(input("Please enter assignments: "))
grade = int((wt * 70)/100 + (le * 20)/100 + (ass * 10)/100) 
print(grade)

# no:19

p = int (input("enter rate"))
if p<=250000:
    tax = "no tax"
elif 250000<p>=500000:
    tax = (5/100)*p
elif 500000<p>=1000000:
    tax = (20/100)*p
elif 1000000<p>=5000000:
    tax = (30/100)*p
else :
    tax = "not mentioned"
print(tax)

# no:20

def num(n):
	num = 1
	for i in range(0, n):
		for j in range(0, i+1):
			print(num, end=" ")
			num = num + 1
		print("\r")
n = 4
num(n)

# no:21

test_tup = (1, 5, 7, 8, 10)
a = tuple(i * j for i, j in zip(test_tup, test_tup[1:]))
print(a)

# no:22

def num():
    list1 = []
    list2 = []
    n = int(input("Enter number of elements : "))
    for i in range(0, n):
        e = int(input())
        a = int(input())
        list1.append(e)
        list2.append(a)     
    print(list1)
    print(list2)
num()
def sum():
    list1 = [1,2,3]
    list2 = [4,5,6]
    sum = []
    for (item1, item2) in zip(list1, list2):
        sum.append(item1+item2)
    print(sum)
sum()
def display():
    list = [1,2,3]
    print(list)
display()

# no:23

def num():
    list = []
    n = int(input("Enter number of elements : "))
    for i in range(0, n):
        e = int(input())
        list.append(e)
    print(list)
num()