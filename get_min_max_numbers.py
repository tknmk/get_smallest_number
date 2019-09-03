# -*- coding: utf-8 -*-

lst = []

num = int(input('Enter number of elements in lis: '))

for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)

print("Maximum element in the list is : ", max(lst))
print("Minimum element in the list is : ", min(lst))
