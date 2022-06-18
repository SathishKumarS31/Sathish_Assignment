#!/usr/bin/env python
# coding: utf-8

# In[53]:


# Abstract class method

# An abstract class can be considered as a blueprint for other classes. It allows to create a set of methods that must be created within any child classes built from the abstract class.

# Below I've given example code using Abstract class, here multiplication function should be used in all other child classes built from abstract class.

from abc import ABC, abstractmethod

class Product(ABC):
  @abstractmethod
  def Multiplication(Self):
    pass
class Multiply(Product):
  def __init__(self):
    self.A = 10
    self.B = 20
class addition(Multiply):
  def sum(self):
    print("The value of A is",self.A)
    print("The value of B is",self.B,"\n")
    return f"The sum of A and B are {self.A+self.B}"
  def Multiplication(self):
    return f"The product of A and B are {self.A*self.B}"
  def division(self):
    return f"The division of A and B are {self.A/self.B}\n"

print("\n----------------------------------------------------------------------------------------------------------\n")

print("***THIS IS THE OUTPUT OF CODE USING ABSTRACT CLASS***\n")

Kumar = addition()
print(Kumar.sum())
print(Kumar.Multiplication())
print(Kumar.division())

print("----------------------------------------------------------------------------------------------------------\n")

# Multiple Inheritance

# When a class is derived from more than one base class it is called multiple Inheritance. The derived class inherits all the features of the base case.

# Below I've given example code using Multiple Inheritance, here all constructors are inherited to cool programmer class from parent class Ineuron and Neuron.

class Ineuron():
  def __init__(self,Name_of_the_Subscriber,courses_subscribed):
    self.name = Name_of_the_Subscriber
    self.courses = courses_subscribed

  def printdetails(self):
    return f"The name of the subscriber is {self.name}, and courses subscribed are {self.courses}"  
class Neuron():
  def __init__(self,Qualification,Employment_status):
    self.Qualification = Qualification
    self.Employment_status = Employment_status

  def printdetails(self):
    return f"The Qualification of Subscriber is {self.Qualification}, and employeement status is {self.Employment_status}"

class coolprogrammer(Ineuron,Neuron):
  pass

A = coolprogrammer("Sathish","FSDS - NOV 2021 and Tech - Neuron\n")
print("***THIS IS THE OUTPUT OF CODE USING MULTIPLE INHERITANCE***\n")
print(A.printdetails())

print("----------------------------------------------------------------------------------------------------------\n")

# Decorators

# Decorators provide the flexibility to write another function to expand the working of written function, without permanently modifying it.

# Below I've given example code using decorator, where addition function (A) is passed as an argument into the (sathish) function.

def sathish(func):
  def Execution():
    print("***THIS IS THE OUTPUT OF CODE USING DECORATOR***\n")
    print("The code is executing\n")
    func()
    print("The code has executed\n")
  return Execution

def A():
  a = 25
  b = 25
  print("The value of a is",a)
  print("The value of b is",b)
  c = a+b
  print("The sum of a and b is",c,"\n")

sub = sathish(A)
sub()


# In[ ]:




