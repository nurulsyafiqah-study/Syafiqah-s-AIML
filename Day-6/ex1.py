class Player:
    def __init__(self):
        print('Welcome to Player Class')

    def reg(self,id,name,team):
            self.id=id
            self.name=name
            self.team=team

    def display(self):
            print(f'ID:{self.id} \tTeam: {self.team}')

#object creation
p1=Player()
p2=Player()
p3=Player()
p1.reg(1,'MSD','India')
p2.reg(2,'Sya','Malaysia')
p3.reg(3,'Akshay','Pakistan')

p1.display()
p2.display()
p3.display()