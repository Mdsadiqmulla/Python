# # a = input("enter ur name")
# # print(a)
# a = input("enter a number :")
# b = input("enter a 2 numbewr :")
# a = int(a)
# b = int(b)
# print(a+b)


# num = 20
# if num < 0:
#     print("negative")
# elif num > 0:
#     print("positive")
# else:
#     print("zero")


# n = 21
# if n%2==0:
#     print("even")
# else:
#     print("odd")

#
# num = 5
# sum = 0
# for i in range(num+1):
#     sum += i
# print(num)


# n1, n2 = 2, 5
# sum = 0
# for i in range(n1,n2+1):
#     sum += i
# print(sum)

# n1,n2 = 20, 1
# if n1 <= n2:
#     print(n2)


# n1, n2, n3 = 59, 34, 23
# if n1<n2 and n3<n2:
#     print(n2)
# elif n2<n3 and n1<n3:
#     print(n3)
# else:
#     print(n1)

# n = 3
# sum = 0
# count = 0
# for i in range(n):
#     if(i%2==0):
#         sum=sum+i
#         count=count+1
# print(sum)
# n = 3
# i = 1
# sum = 0
# count = 0
# while(count<n):
#     if(i%2==0):
#         sum=sum+i
#         count=count+1
#     i=i+1
# print(sum)


# write a program sum of digits of given number:

# n = 333
# sum = 0
# while(n>0):
#     sum=sum+n%10 # 0 + 3
#     n=n//10  # 33
# print(sum)

# squre of digits
# n = 153
# orig = n
# sum = 0
# while(n>0):
#     sum = sum+(n%10)*(n%10)*(n%10)
#     n = n//10
# if orig==sum:
#     print("amstrong")
# else:
#     print("not amstrong")


# n = 234
# prod = 1
# while(n>0):
#     prod = prod*(n%10)
#     n = n//10
# print(prod)

# i = 525
# rev = 0
# orig = i
#
# while(i>0):
#     rev=(rev*10)+i%10
#     i=i//10
# if (orig==rev):
#     print("palindrome")
# else:
#     print("not")



# # for loop
# n = "sadiq"
# for i in (n):
#     print(i

#
#
# for i in range(5,15,2):
#     print(i)
#
# for i in range(2):
#     print(i)
#     for j in range(3):
#         print(j)
# #
# for i in range(5):
#     for j in range(5):
#         print("*",end="")
# print()

# n = 5
# # for i in range(n):
# #     for j in range(i+1):
# #         print("$",end="")
# #     for j in range(i,n):
# #         print("", end=" ")
# #     for j in range(i+1):
# #         print("*",end="")
# #     # for j in range(i,n):
# #     #
# #     #     print("*",end="")
# #     print()
#
# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print("*",end=" ")
#     print()
# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print("",end="")
#
#     for j in range(i):
#         print("*",end="")
#
#     for j in range(i+1):
#         print("*",end="")
# #     print()
#
# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print(1)
#
# #
#     for j in range(i,n-1):
#         print("*",end="")
#
#     for j in range(i,n):
#         print("*",end="")
#     print()


# nums = [3, 2, 4]
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[0]+nums[1]:
#             return[i,j]
#
#
# n = 12
#
# for i in range(0,n):
#     for j in range(i+1):
#         print(j+1,end=" ")
#     print()

# num = 123
# sum = 0
#
#
# for i in num:
#     sum = sum + int(i)
#
# print(sum)

# num = 1 ,2, 3
# sum = 0
#
# for i in num:
#     sum = sum + int(i)
# print(sum)



# import string
# import random
#
# if __name__=="__main__":
#     s1 = string.ascii_lowercase
#     s2 = string.ascii_uppercase
#     s3 = string.digits
#     s4 = string.punctuation
#
#     p = int(input("Enter Password Length\n"))
#     s = []
#     s.extend(list(s1))
#     s.extend(list(s2))
#     s.extend(list(s3))
#     s.extend(list(s4))
#
#     random.shuffle(s)
#     print("".join(s[0:p]))

# class Phone:
#     def set_color(self,color):
#         self.color=color
#
#     def show_color(self):
#         return self.color
#     def make_call(self):
#         print("making a call")
# p1 = Phone()
# p1.set_color("blue")
# p1.show_color()


# class Employee:
#     def __init__(self,name,age,salary,gender):
#         self.name = name
#         self.age = age
#         self.salary = salary
#         self.gender = gender
#
#     def show_employee_details(self):
#         print("name of Employee",self.name)
#         print("age of employee",self.age)
#         print("salary of employee",self.salary)
#         print("gender of employee",self.gender)
#
#
# e1 = Employee('ram',32,50000,'male')
# e1.show_employee_details()



# class Parent:
#     def __init__(self):
#         print("This is Parent",self)
#
#
# pc = Parent()
#
#
# class Child(Parent):
#     print("This is child")
#
# cc = Child()




# This is Parent class
# This is Child class
# This is Parent class




# class Member:
#     def __init__(self,Name,Age,Phone,Address,Salary):
#         self.Name = Name
#         self.Age = Age
#         self.Phone = Phone
#         self.Address = Address
#         self.Salary = Salary
#      def salary_Details(self):
#          print(self.Salary)
#
# class Employee(Member):
#     def __init__(self,Name,Phone,Address,Salary,Specialization):
#         super().__init__(Name,Age,Phone,Address,Salary)
#         self.Specialization = Specialization

# class Manager(Member):
#     def __init__(self,Name,Age,Phone,Address,Salary,Department):
#         super().__init__(Name,Age,Phone,Address,Salary)
#         self.Department = Department
#
# a = Employee("Rahul",21,123,"xyz",25000,"abc")
# b = Manager("Raksha",20,456,'wasd',30000,"xyz")
# a.Salary()
# b.Salary()



# class Shape:
#     def Shape(self):
#         print("This is Shape")
#
# class Rectangle(Shape):
#     def Rectangle(self):
#         print("This is Ractangular Shape")
#
# class Circle(Shape):
#     def Circle(self):
#         print("This is Circular Shape")
#
# class Squre(Rectangle):
#     def Squre(self):
#         print("squre is a rectangle")
#
#
# ob = Squre()
# ob.Rectangle()
# ob.Shape()






