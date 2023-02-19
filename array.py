# storing the element in an array
# import array as arr
# a = arr.array("i",[1,2,3,4,5,6,7,8,9])
# for i in range (0,9):
#     print(a[i], end=" ")
# print()

# lartgest array
# def largest(arr,n):
#     max = arr[0]
#     for i in range(1,n):
#         if arr[i] >max:
#             max = arr[i]
#     return max
#
#
#
# arr = [10,12,52,48,63,95,87]
# n = len(arr)
# ans = largest(arr,n)
# print(ans)

# def minimum(arr,n):
#     min = arr[0]
#     for i in range(1,n):
#         if arr[i]<min:
#             min = arr[i]
#     return min
#
# arr = [1,2,5,6,3,7,8,9]
# n = len(arr)
# ans = minimum(arr,n)
# print(ans)

# def get_primelist(upper):
# 	result = []
# 	for cp in range ( 2, upper + 1 ):
# 		for i in range ( 2, cp ):
# 			if ( cp % i == 0 ):
# 				break
# 		else:
# 			result.append(cp)
# 	return result
#
# # RUN to create an array of the prime numbers
# # [ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
# #  43,47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97 ]
# print (get_primelist(100))


def subArraySum(arr, n, sum_):
	# Pick a starting point
	for i in range(n):
		curr_sum = arr[i]

		# Try all subarrays starting
		# with 'i'
# 		j = i + 1
# 		while j <= n:
# 			if curr_sum == sum_:
# 				print("Sum found between")
# 				print("indexes % d and % d" % (i, j - 1))
# 				return 1
#
# 			if curr_sum > sum_ or j == n:
# 				break
#
# 			curr_sum = curr_sum + arr[j]
# 			j += 1
#
# 	print("No subarray found")
# 	return 0
#
#
# # Driver code
# arr = [15, 2, 4, 8, 9, 5, 10, 23]
# n = len(arr)
# sum_ = 23

# subArraySum(arr, n, sum_)
# b.Salary()

class Member:
    def __init__(self, name, age, phone, address, salary):
        self.name = name
        self.age = age
        self.phone = phone
        self.address = address
        self.salary = salary

    # def printSalary(self):
    #     print(f'{self.name} salary is {self.salary}')

class Employee(Member):
    def __init__(self, name, age, phone, address, salary, specialization):
        super().__init__(name, age, phone, address, salary)
        self.specialization = specialization

class Manager(Member):
    def __init__(self, name, age, phone, address, salary, department):
        super().__init__(name, age, phone, address, salary)
        self.department = department
employee1 = Employee('John', 30, '123-456-7890', '123 Main St', 50000, 'Computer Science')
manager1 = Manager('Jane', 35, '987-654-3210', '456 Market St', 75000, 'Marketing')
# employee1 = Employee('John', 30, '123-456-7890', '1250000, 'Computer Science')
# manager1 = Manager('Jane', 35, '987-654-3210', '456 Market St', 75000, 'Marketing')3 Main St',
print(employee1.name)
print(employee1.age)
print(employee1.phone)
print(employee1.address)
print(employee1.salary)
print(employee1.specialization)

print(manager1.name)
print(manager1.age)
print(manager1.phone)
print(manager1.address)
print(manager1.salary)
print(manager1.department)
# employee1.printSalary()
# manager1.printSalary()
