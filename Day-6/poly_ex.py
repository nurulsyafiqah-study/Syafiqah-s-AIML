# class Bird:
#     def fly(self):
#         print('Bird can fly')

# class Airplane(Bird):
#     def fly(self):
#         print('Airplane can fly')

# b=Bird()
# print('Bird implement')
# b.fly()

# print('Airplane Implementation')
# a=Airplane()
# a.fly()

# print('Using the loop')
# for obj in [Bird(), Airplane()]:
#     obj.fly()

#________________________________________________________________________________

class Emp:
    def reg(self):
        self.id=int(input('Enter ID number:\t'))
        self.name=input('Enter Name:\t')
    
    def disp(self):
        print('Name:\t',self.name)
        print('ID:\t',self.id)

##super class
class Dev(Emp):
    def reg(self):
        super().reg()
        self.domain=input('Enter domain:\t')
    def disp(self):
        super().disp()
        print('Domain:\t',self.domain)

d1=Dev()
d1.reg()
d1.disp()


