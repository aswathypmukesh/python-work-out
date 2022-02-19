# def triangle(n):
#     for i in range(1,2*n):
#         for j in range(1,2*n):
#             if i==j or i+j==2*n:
#                 print('*', end='')
#             else:
#                 print(' ', end='')
#         print("\r")
# n = 5
# triangle(n)
# def add():
#     dic1 = {6:"six",4:"four",2:"two",1:"one",5:"five",3:"three"}
#     dic2 = {7:"seven",8:"eight",9:"nine"}
#     dic1.update(dic2)
#     print(dic1) 
# add() 

def asc():
    a = {6:"six",4:"four",2:"two",1:"one",5:"five",3:"three"}
    print(sorted(a.items()))
asc()