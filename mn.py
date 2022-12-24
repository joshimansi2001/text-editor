# # # # class parent1:
# # # #     def func_1(self):
# # # #         print("this function is defined inside the parent class")

# # # # class child1(parent1):
# # # #     def func_2(self):
# # # #         print("this function is defined inside the child class")

# # # # object = child1()
# # # # object.func_1()
# # # # object.func_2()

# # # # class employee():
# # # #     def showdetail(self):
# # # #         print("this is an emplyoee")

# # # # class programmer(employee):
# # # #     def getinfo(self):
# # # #         print("this is a programmer")

# # # # p = programmer()
# # # # p.showdetail()
# # # # p.getinfo()


# # # # #first base class

# # # # class father1:
# # # #     fathername1 = ""
# # # #     def father1(self):
# # # #         print(self.fathername1)

# # # # #second base class

# # # # class mother1:
# # # #     mothername1 = ""
# # # #     def mother1(self):
# # # #         print(self.mothername1)

# # # # #child class

# # # # class son(father1, mother1):
# # # #     def parents1(self):
# # # #         print("father name is: ",self.fathername1)
# # # #         print("mother name is: ",self.mothername1)


# # # # s1 = son()
# # # # s1.fathername1 = 'rajesh'
# # # # s1.mothername1 = 'siya'
# # # # s1.parents1()


# # # # class employee:
# # # #     company = 'goggle'
# # # #     def employee(self):
# # # #         print(self.company)

# # # # class employee2:
# # # #     company2 = 'tsc'
# # # #     def employee2(self):
# # # #         print(self.company2)

# # # # class owner(employee, employee2):
# # # #     def owner2(self):
# # # #         print("your first company is: ")
# # # #         print("your second company is: ")

# # # # q = owner()
# # # # q.employee()
# # # # q.employee2()


# # # #base class
# # # class grandfather1:
# # #     def __init__(self, grandfathername1):
# # #         self.grandfathername1 = grandfathername1

# # # #intermidate class
# # # class father1(grandfather1):
# # #     def __init__(self, fathername1, grandfathername1):
# # #         self.fathername1 = fathername1
# # #         grandfather1.__init__(self,grandfathername1)

# # # class son1(father1):
# # #     def __init__(self, sonname1, fathername1, grandfathername1):
# # #         self.sonname1 = sonname1
# # #         father1.__init__(self.fathername1)

# # #     def print_name(self):
# # #         print("grandfather name is: ",self.grandfathername1)
# # #         print("father name is: ",self.fathername1)
# # #         print("son name is: ",self.sonname1)

# # # s1 = son1('rahul', 'sourav', 'shubham')
# # # print(s1.grandfathername1)
# # # s1.print_name()



# # class parent:
# #     def __init__(self, txt):
# #         self.message = txt

# #     def printmessage(self):
# #         print(self.message)

# # class child(parent):
# #     def __init__(self, txt):
# #         super().__init__(txt)

# # x = child("hello , and welcome !")
# # x.printmessage()

# class person:
#     age = 25

#     def printage(self):
#         print("your age is: ",self.age)

# #class method()
# person.printage = classmethod(person.printage)

# person.printage()
x = int(input('enter a number'))
try:
    x = int(a)
    print(x)
except:
    print('an except occured')