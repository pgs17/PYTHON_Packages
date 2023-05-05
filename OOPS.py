#!/usr/bin/env python
# coding: utf-8

# In[31]:


# Create a class employee with attributes as name age salary and level

class Employee:
    
    # this is a class attribute
    alias="KEYBOARD WARRIOR"
    
    # writing instance attributes
    def __init__(self,name,age,level,salary):
        self.name=name
        self.age=age
        self.level=level
        self.salary=salary
     
    # writing instance method
    def Code(self):
        print(f"{self.name} is coding")
        
    def Code_in_language(self,language):
        print(f"{self.name} is coding in {language}")
    
    # creating a instance as well as class method using a decorator @staticmethod and here self is not passed
    @staticmethod
    def Entry_salary(age):
        if(age<25):
            return 7000
        else:
            return 9000


# In[32]:


# creating two objects E1 AND E2 for that class Employee and print name of both and show class attribute on E2
E1= Employee("Lisa",20,"Senior Developer",5000)
E2=Employee("Jennie",21,"Designer",6000)
print(E1.name,E2.name)
E2.alias


# In[33]:


# call instance method on the objects created
E2.Code()
E1.Code()
E2.Code_in_language('Python')


# In[34]:


Employee.Entry_salary(23) # works as class attribute even without @staticmethod
E1.Entry_salary(20)


# In[35]:


# Inheritance
# Create a class employee with attributes as name age salary
# Create a class Software Engineer and Designer and Software Engineer will have LVL type and define an instance method for the type of work they are doing 

class Employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def work(self):
        print(f"{self.name} is working")

class Software_engineer(Employee):
    
    # when we overwrite init function we super()__init__(params) in child class
    def __init__(self,name,age,salary,level):
        super().__init__(name,age,salary)
        self.level=level
    def work(self):
        print(f"{self.name} is Coding")

class Designer(Employee):
    def work(self):
        print(f"{self.name} is designing")


# In[36]:


Se1=Software_engineer("Lisa",20,20000,"senior developer")
d1=Designer("Jennie",27,30000)
print(d1.salary,Se1.salary)


# In[37]:


Se1.work()


# In[38]:


d1.work()


# In[2]:


# Create a class Software Engineer with attribute name and age as public and salary and number of bugs solved as private
class Software_Engineer:
    def __init__(self):
        
        # to create a private we ise __name and _name is protected
        self._salary=None
        
    
    def code(self):
            self._numberofbugssolved+=1
        
    # to set salary and get it from outside we will use setter and getter function in pythonic way
   # get value
    @property   
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self,base_value):
        self._salary= base_value
        
        
    # now we want and internal function where when a engineer codes each time his salary is determined by no bugs solved    
   # this is an private function accessed inside the class only
    def _calculate_salary(self,base_value):
        if(self._numberofbugssolved < 10):
            return base_value
        if(self._numberofbugssolved < 100):
            return base_value*2
        else:
            return base_value*3


# In[70]:


se1= Software_Engineer("Lisa",20)
print(se1.name,se1.age)
se1.set_salary(20000)
se1.get_salary()


# In[71]:


for i in range(70):
    se1.code()


# In[72]:


se1.set_salary(6000)
se1.get_salary()
# the set salary applies to abstraction implement as the implementation is  seen and not operation


# In[3]:


se2=Software_Engineer()


# In[5]:


# More Pythonic Way for Getter and Setter using Decorators
se2.salary=2000
print(se2.salary)


# In[9]:


# Create a class student with marks 1 and marks 2 and just add both student marks and generate 3rd student so basically override + add

class student:
    
    def __init__(self,mark1,mark2):
        self.mark1=mark1
        self.mark2=mark2
        
        # this is overloading the add operator 
    def __add__(self,other):
        mark1=self.mark1+other.mark1
        mark2=self.mark2+other.mark2
        s3=student(mark1,mark2)
        return s3


# In[11]:


s1=student(68,51)
s2=student(58,41)
s3=s1+s2
s3.mark1


# In[ ]:




