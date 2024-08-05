"""
num = int(input("Enter a number: "))
if num % 2 ==0:
   print("It is a even number")
else:
    print("It is a odd number")
##
n1= int(input("Enter a number1: "))
n2= int(input("Enter a number2: "))
n3= int(input("Enter a number3: "))
n4= int(input("Enter a number4: "))
n5= int(input("Enter a number5: "))

sum=n1+n2+n3+n4+n5
avg=sum/5
print(avg)


##
n=int(input("Enter a number1:"))

print("1/"+str(n))
##

s1= int(input("Enter side1: "))
s2= int(input("Enter side2: "))
s3= int(input("Enter side3: "))
s4= int(input("Enter side4: "))
d1= int(input("Enter the diagonal 1: "))
d2=int(input("enter the diagonal 2:"))

if s1!=s2 or s2!=s3 or s3!=s4:
    print("not a square")
else: 
    if d1==d2:
        print("It is a square")
    else:
        print("not a square")

##
radius =int(input("Enter the radius: "))
area=3.14 * radius * radius
print(area)

##
p = int(input("Enter principal: "))
r = int(input("Enter rate of interest: "))
t = int(input("Enter time:"))

ci=p*pow((1+r),t)-p
print(ci)

##

def ispalindrome(str):
    if(string==string[::-1]):
        print("It is a palindrome")
    else:
        print("it is not a palindrome")
    
string =input("enter the string:")

print(ispalindrome(string))
    
##

def fibo(n):
    if n<0:
        print("Invalid number ")
    elif n==0 or n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
    
print(fibo(2))

 ##   
arr =[19,11,15,131]
    
for i in range(0,len(arr)):
    if arr[i] in range(100,1000):
        print("It is a three digit number")
    else:
        print("It is not a three digit number")
    
##
    
n1=int(input("Enter the Number1 "))
n2=int(input("Enter the Number2 "))

def ad(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

print(ad(n1,n2))
print(sub(n1,n2))
print(mul(n1,n2))
print(div(n1,n2))



class employee:
    def __init__(self,empname,depart,desig):
        self.empname=empname
        self.depart=depart
        self.desig=desig
        
    def pr(self):
        return f"the details of the employee is {self.empname},{self.depart},{self.desig}"

emp1=employee("Ayush","Data & AI","ASE")

print(emp1.empname)
print(emp1.depart)
print(emp1.desig)

 
class Item:
    def __init__(self,itemname,price,quantity):
        self.itemname=itemname
        self.price=price
        self.quantity=quantity
        

item1=Item("Coffee","24","10")
item2=Item("Tea","11","15")
item3=Item("Ice tea","30","25")

print("The item details are "+item1.itemname+" , "+item1.price+" , "+item1.quantity)
            
     
 
class toys:
    def __init__(self):
        self.toyname="ball"
        self.price="300"
        self.quantity="20"
        self.age_group="18-30"
        

class Automatic_toy(toys):
    def __init__(self):
        self.type_of="sensor"

class Digitaltoy(toys):
    def __init__(self):
        self.works_on="battery"
        
    

at=Automatic_toy()
dt=Digitaltoy()


print(at.type_of)
print(dt.works_on)
print()
    
        
class calculator:
    def add(self,a,b):
        self.a=a
        self.b=b
        
    def add(self,a,b=0):
        self.a=a
        self.b=b
    
        
c=calculator()
c.add(12,23)
print(c.a)
   
    
        
      

class Employee:
    def __init__(self, name, department):
        self._name = name
        self._department = department
        
    @property
    def name(self):
        return self._name
    
    @property
    def department(self):
        return self._department
    
    @name.setter
    def name(self, value):
        self._name = value
        
    @department.setter    
    def department(self, value):
        self._department = value

# Create an instance with initial values
e = Employee("John Doe", "Marketing")

# Update values using the property setters
e.name = "Peter"
e.department = "Sales"

# Print updated values
print(e.name)        
print(e.department) 



class Item:
    def __init__(self, itemname, price,quantity , batchNo):
        self._itemname = itemname
        self._price = price
        self._quantity=quantity 
        self._batchNo=batchNo
                
    @property
    def itemname(self):
        return self._itemname
    
    @property
    def price(self):
        return self._price
    
    @property
    def quantity(self):
        return self._quantity
    
    @property
    def batchNo(self):
        return self._batchNo
    
    @itemname.setter
    def itemname(self, value):
        self._itemname = value
        
    @price.setter    
    def price(self, value):
        self._price = value

    @quantity.setter    
    def quantity(self, value):
        self._quantity = value
        
    @batchNo.setter    
    def batchNo(self, value):
        self._batchNo = value
# Create an instance with initial values
it = Item("Biscuit", "20","2","1221")

# Print updated values
print(it.itemname)
print(it.price)
print(it.quantity)
print(it.batchNo)

        
        """
        
from abc import ABC , abstractmethod

class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    def stop(self):
        pass
    
class car(vehicle):
    
    def start(self):
        print("car starting")
        
    def stop(self):
        print("car stoping")
        
c=car()
c.start()
c.stop()