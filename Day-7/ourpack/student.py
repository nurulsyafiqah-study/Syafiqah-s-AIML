class Student:
    def __init__(self,id,name):
        self.id=id
        self.name=name

    def print_info(self):
        print('Student ID:\t',self.id)
        print('Student Name:\t',self.name)