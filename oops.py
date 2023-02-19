# class mobile:
#     def config(self):
#         print("rwalme X ,6gbRAM, 128gbROM")
#
#
#
# mob1 = mobile()
# mob2 = mobile()
# mobile.config(mob1)

# class student:
#     def __init__(self,name="John",roll_no=2):
#         self.name=name
#         self.roll_no=roll_no
#
# def main():
#
#     obj=student()
#     print(obj.name,obj.roll_no)
#
#
# main



# for i in rang('8',end="")
#  #
#  #    print()
#  #
#  #
#  #
#  # class object_count:
#  #     counter = 0
#  #
#  #            def __init__(self,object_count):
#  #                self.name = name
#  #
#  #                self.age = age
#  #
#  #                Student.counter += 1
#  #
#  #            def printDetails(self):
#  #                print(self.name, self.age, "years old")
#  #
#  #        student1 = Student('Ankit Rai', 22)
#  #
#  #        student2 = Student('Aishwarya', 21)
#  #
#  #        student3 = Student('Shaurya', 21)
#  #
#  #        print("Total number of objects created: ", Student.counter)
#  #
# e(1,6):
#     for j in range(1,i+1):
#  #        print
# class object_count:
#     counter = 0
#     def __init__(self):
#         object_count.counter += 1
#
#
#
# g1 = object_count()
# g2 = object_count()
# g3 = object_count()
# print(object_count.counter)


# import array as arr

# # creating an array with integer type
# a = arr.array('i', [1, 2, 3])
#
# # printing original array
# print("The new created array is : ", end=" ")
# for i in range(0, 3):
#     print(a[i], end=" ")
# print()

import array as arr

# array with int type
a = arr.array('i', [1, 2, 3])

print("Array before insertion : ", end=" ")
for i in range(0, 3):
    print(a[i], end=" ")
print()

# inserting array using
# insert() function
a.insert(1, 4)

print("Array after insertion : ", end=" ")
for i in (a):
    print(i, end=" ")
print()