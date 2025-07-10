# Simple Class
# class Student:
#     name = "Shrikant"
# s1 = Student()
# print(s1.name)


# Class with init function/Default Constuctor
# class Teacher:
#     def __init__(self):
#         print("This is the First INIT execution...")
# t1 = Teacher()


# class with init function/Parameterized Constructors
# obj attr has an higher priority than class attr
# class Teacher:
#     college_name = "ABCD College"   # class attr
#     def __init__(self,firstname, lastname):     # Standard Pracrice to keep same names i.e. self.name = name
#         self.fname = firstname      #obj attr
#         self.lname = lastname
#         print("This is the Second INIT execution...")
# t1 = Teacher('John', 'Doe')
# print("FIRST NAME : ", t1.fname)
# print(t1.college_name)
# print("================")
# t2 = Teacher('Mery', 'zaa')
# print("LAST NAME : ", t2.lname)
# print("FIRST & LAST NAME : ", t2.fname, t1.lname)
# print(t2.college_name)



# class College:
#     def __init__(self, fullname):
#         self.fname = fullname
#         print("Constructor Called")
#
#     def welcome(self):
#         print("Welcome to Our", self.fname, "College")
#
#     def greet(self):
#         return "Hello I am", self.fname
#
#     @staticmethod
#     def static_method():
#         print("Static method without self parameter executed with decorator")
#         print("Static method can't access or modify class state...")
#
# c1 = College("ADCET")
# print(c1.fname)
# print("===========")
# c1.welcome()
# print("===========")
# c1.greet()
# print(c1.greet())
# print("===========")
# c1.static_method()
# print("===========")


# Problem Statement Banking Credit Debit Amount

# class Account:
#     def __init__(self, acc, bal):
#         self.account_no = acc
#         self.balance = bal
#
#     def debit(self, amount):
#         self.balance = self.balance - amount
#         print("Debited amount is : ", amount)
#         print("Your remaining balance is : ", self.balance )
#         # print("Your remaining balance is : ", self.get_balance())
#
#
#     def credit(self, amount):
#         self.balance = self.balance + amount
#         print("Credited amount is : ", amount)
#         print("Your remaining balance is : ", self.balance )
#         # print("Your remaining balance is : ", self.get_balance())
#
#
#     def get_balance(self):
#         return self.balance
#
# a1 = Account(16131012, 25000.00)
# # print("Your account Number is : ", a1.account_no)
# # print("Your account Balance is : ", a1.balance)
#
# a1.debit(1000)
# print("===============")
#
# a1.credit(2000)
# print("===============")
# a1.get_balance()
# print("Your Total Balance is : ", a1.get_balance())
# print("===============")



# # Private methods - To access the attribute inside class, outside class it is noe accesible.
#
# class Account:
#     def __init__(self, acc, pw):
#         self.account_no = acc
#         self.__password = pw
#
#     def reset_pass(self):
#         print("Inside class info accesible : ", self.__password)
#
# a1 = Account(12345, 'asdf')
# print("Account Number is : ", a1.account_no)
# # print("Account Password is : ", a1.__password)    #not accesible bcz it is make a private
#
# a1.reset_pass()



# INHERITANCE with super method

# class Car:
#      def __init__(self, fueltype):
#          self.fueltype = fueltype
#      @staticmethod
#      def start():
#          print("Car Stared...")
#      @staticmethod
#      def stop():
#          print("Car Stopped...")
#
# class Toyota(Car):      # here not needed to 'self.fueltype = fueltype', bcz of super class
#     def __init__(self, color, fueltype):
#         self.color = color
#         super().__init__(fueltype)
#         super().start()
#         # super().stop()
#
# t1 = Toyota("White", "diesel")
# print(t1.color)
# print(t1.fueltype)


# Class has 3 types of methods:
# staticmethod = ()    @staticmethod    def MethodName()
# classmethod = (cls)   @classmethod    def MethodName(cls)
# imstancemethod = (self)   def MethodName(self)