# score = int(input("enter a score"))
# if score <= 5:
#     print('f')
# elif score <= 10:
#     print('e')
# elif score <= 15:
#     print('d')
# elif score <= 20:
#     print('c')
# elif score <= 25:
#     print('b')
# else:
#     print('a')
# #
#
#


# prod = 1        # n =234
# # sums = 0
# # while n != 0:
# #     last = n % 10
# #     prod *= last
# #     sums += last
# #     n =n//10
# # return prod - sums

# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print('*', end='')
#     for j in range(1, 6 - i):
#         print(" ", end='')
#     for j in range(1, i + 1):
#         print('*', end='')
#     print()


# n = 5
# for i in range(n):
#     for j in range(i+1):
#           print("*",end="")
#     for j in range(i,n):
#         print(" ",end="")
#
#     for j in range(i+1):
#                 print("*",end="")
#     print()

# class Employee:
#     def __init__(self,n,s):
#         self.name = n
#         self.salary = s

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __repr__(self):
        return '{' + self.name + ', ' + str(self.salary) + '}'


if __name__ == '__main__':
    employee = [
		Employee('James', 80000),
		Employee('Robert', 60000),
		Employee('James', 70000),
        Employee('charls',4000),
        Employee('micky',2000)
	]


    employee.sort(key=lambda x: (x.name))
    print(employee)



