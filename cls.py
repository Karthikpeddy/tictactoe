class details:
    def __init__(self,name,age,email,salary):
        self.name=name
        self.age=age
        self.email=email
        self.salary=salary
        print(name,"\n",age,"\n",email,"\n",salary)
    def getdetails(self,name,age,email,salary):
        li=[name,age,email,salary]
        self.li=li
        print(li)
    def setdetails(self,*arg):
        l=[]
        for i in arg:
            l.append(i)
        print(l)    
emp1=details('karthik',15,"example@gmail.com",5000)
emp2=details('abhi',16,"example@gmail.com",5000)     
emp3=details('john',19,"example@gmail.com",5000)
emp4=details('ray',35,"example@gmail.com",5000)
emp5=details('maria',25,"example@gmail.com",5000)
emp1.getdetails('karthik',15,"example@gmail.com",5000)
n1=input("enter your name:  ")
n2=int(input("enter you age:  "))
n3=input("enter your emailid:  ")
n4=int(input("enter your salary:  "))
emp1.setdetails(n1,n2,n3,n4)
emp1.name=n1
emp1.li.append("testing")
print(emp1.li)
print(emp1.name)