# Selection sort in Python
# time complexity O(n*n)
# sorting by finding min_index
# def selectionSort(array, size):
#      for ind in range(size):
#           min_index = ind
# 
#           for j in range(ind + 1, size):
#                # select the minimum element in every iteration
#                if array[j] < array[min_index]:
#                     min_index = j
#           # swapping the elements to sort the array
#           (array[ind], array[min_index]) = (array[min_index], array[ind])
# 



# 
# arr = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
# size = len(arr)
# selectionSort(arr, size)
# print('The array after sorting in Ascending Order by selection sort is:')
# print(arr)

# def selectionsort(array, size):
#      for i in range(size):
#           min = i
#          for j in range(i+1, size):
#                if arr[j]<array[min]:
#                    min = j
#      (array[i],array[min])=(array[in,array[i]])
#
# arr = [1,2,3,4,5,6,7,8,9]
# size = len(arr)
# selectionsort(array,size)
# print(arr)





# reverse = 0
# while num > 0:
#     remainder = num % 10
#     reverse = (reverse * 10) + remainder
#     num = num // 10


# i = int(input("enter number :"))
# rev = 0
# while (i>0):
#     rev = (rev*10)+i%10
#     i = i//10
# print("reverse=",rev)


# import array as arr
# a = arr.array("i",[1,2,3])
# print("The orignal array is :",end=" ")
# for i in range(0,3):
#     print(a[i], end=" ")
# print()

# #




# import array as arr
# l = [1,2,3,4,5,6,7,8,9]
# a = arr.array('i',l)
#
# for i in (a):
#      print(i,end=" ")
# sliced_array= a[3:8]
# print("\n",sliced_array)
# #



#
# def l(arr,n):
#      mx = arr[0]
#
#      for i in range(1,n):
#           if arr[i]>mx:
#                mx = arr[i]
#
#      return mx
#
#
# arr = [10,20,30,40,50,60]
# n = len(arr)
# ans = l(arr,n)
# print(ans)





# # import array as arr
# #
# # # array with int type
# a = arr.array('i', [1, 2, 3])
#
# print("Array before insertion : ", end=" ")
# for i in range(0, 3):
#     print(a[i], end=" ")
# print()
#
# # inserting array using
# # insert() function
# a.insert(1, 4)
#
# print("Array after insertion : ", end=" ")
# for i in (a):
#     print(i, end=" ")
# print()







# def prime(arr,n):
#      if (n <= 1):
#           return False
#      if (n <= 3):
#           return True
#      if (n%2 == 0 or n%3 == 0):
#           return False
#
#      i = 5
#
#      while (i * i <= n):
#           return False
#
#      i += 6
#      return True
#
# arr = [2,3,4,5,6,7,8,9]
# n = len(arr)
# print(arr,n)














# num = 1221
# temp = num
# reverse = 0
# while temp > 0:
#     remainder = temp % 10
#     reverse = (reverse * 10) + remainder
#     temp = temp // 10
# if num == reverse:
#     print("palindrome")
# else:
#      print("not a palindrome")


# number = 371
# num = number
# digit, sum = 0, 0
# length = len(str(num))
# for i in range(length):
#   digit = int(num%10)
#   num = num/10
#   sum += pow(digit,length)
# if sum==number:
#   print("Armstrong")
# else:
#   print("Not Armstrong")

# n = 10
# sum = 0
# while(i>=n):
#   sum = sum-i
#   i = i-1
# print("sum =",sum)
#
#
# n = 3
# i = 1
# sum = 0
# while(i<=n):
#   sum = sum+i
#   i = i+1
#   print("sum =",sum)
# i = 10

#
# i = 1
# while i<=5:
#     j = 1
#     while j<=i:
#         print("#", end=" ")
#         j = j+1
#         print()
# i = i+1




# for i in range(4):
#     for j in range(i+1):
#         print("* ", end= "")
#     print()
#
#
#
# i = 1
# while i<=5:
#     b = 1
#     while b<=5-i:
#         print(" ",end="")
#         b = b+1
#     j = 1
#     while j<=i:
#         print("*",end="")
#         j = j+1
#     print()
#     i = i+1

# import numpy
# arr = [1, 2, 3, 4, 5];
#
# print("Elements of given array: ");
# # Loop through the array by incrementing the value of i
#
# for i in range(0, len(arr)):
#     print(arr[i]),


#
# a = [5, 4, 7, 2, 6]
# max_element = a[0]
#
# for i in range(len(a)):
#   if a[i] > max_element:
#      max_element = a[i]
#
# print (max_element)




# arr = [5,6,2,9,-2]
# mini = arr[0]
#
# for i in range(len(arr)):
#   if arr[i] < mini:
#      mini = arr[i]
#
# print (mini)


# num = []
# flag = False
#
# # prime numbers are greater than 1
# if num > 1:
#     # check for factors
#     for i in range(2, num):
#         if (num % i) == 0:
#             # if factor is found, set flag to True
#             flag = True

# n = [5,2,-4,-5,3,-1,2,3,1]
# maxSum = le-8
# for i in range(0, n):
#     currSum = 0
#     for j in range(i, n):
#         currSum = currSum + arr[j]
#         if (currSum > maxSum):
#             maxSum = currSum
# return maxSum

#
# a = []
# for i in range(n):
#     val = int(input())
#     a.append(val)
#
# for i in range(1, n):
#     t = a[i]
#     j = i - 1
#     while j >= 0 and t < a[j]:
#         a[j + 1] = a[j]
#         j = j - 1
#
#     a[j + 1] = t
# (a)
# print

#
# from array import *
# vals = array('i',[2,6,4,3,7])
#
# for i in range(len(vals)):
#     print(vals[i])



# from array import*
# arr = array('i',[])
# n = 3
# for i in range(n):
#     x = int(input("enter a neext value"))
#     arr.append(x)
#
# print(arr)




# arr1 = array([1,2,3,4,5,6])
# arr2 = arr1.copy()
# arr1[1] = 7
# print(arr1)
# print(arr2)
# from numpy import*
#
# arr1 = array([
#
#                [1,2,3,64,54,34],
#                [4,5,6,34,34,53,]
# ])
# print(arr1)
#
# arr= arr2.reshape(3,4)
#2 = arr1.flatten()
#
# arr3
#
# print(arr3)


  # if (score <= 5) {
  #       return 'F';
  #   } else if (score <= 10) {
  #       return 'E';
  #   } else if (score <= 15) {
  #       return 'D';
  #   } else if (score <= 20) {
  #       return 'C';
  #   } else if (score <= 25) {
  #       return 'B';
  #   } else {
  #       return 'A';
  #   }
  #
  #   return grade;
# }