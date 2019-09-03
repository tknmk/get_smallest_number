# -*- coding: utf-8 -*-


lst_01 = []

# input element number
num = int(input("Enter number of elements in list: "))


# input numbers by user
for i in range(1, num + 1):
    ele = int(input("Enter elements: "))
    lst_01.append(ele)

# print maximum number
print("Smallest element is: ", min(lst_01))

