# class Emp:
#     def display():
#         print('Display of employee class')

# obj=Emp()
# obj.display()
#________________________________________________________
#class className:
    #definition of class
        #attribute Method, constructors

#objectName=className()
#objectName.MethodName()
#________________________________________________________
# e=Emp()
# e.display()

class Emp:
    def reg(self,eid,ename):
        self.eid=eid
        self.ename=ename

    def display(self):
        print('Employee Details is as follows')
        print('Employee ID:\t',self.eid)
        print('Employee Name:\t',self.ename)

e1=Emp()
e2=Emp()
e3=Emp()
e1.reg(1,'Sam')
e2.reg(102,'Neha')
e3.reg(103,'Jai')
print('\nFirst Employee Details')
e1.display()
print('\nSecond Employee Details')
e2.display()
print('\nThird Employee Details')
e3.display()
    