# If you code WAY 1 from welcome.py (with the return)
# from ourpack import welcome
# username=input('Please enter your name:\t')
# print(welcome.display(username))

#_________________________________________
# If you code WAY 2 without 'return'
# from ourpack import welcome
# username=input('Please enter your name:\t')
# welcome.display(username)

#________________________CALLING FROM student.py
from ourpack import student
s1=student.Student(1,'Akshay')      #fileName.className
s1.print_info()
