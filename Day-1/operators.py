#2. Assignment operators: =, +=, -= etc.
# -Example1
# price=float(input("Enter product price \t"))
# discount=price*0.10
# discountedPrice=price-discount
# print(f"Price: {price} \nDiscount: {discount} \nTotal:{discountedPrice}") #\n - is new line

# -Example2
# salary= 50000
# bonus=500

# print(f"Salary {salary} and Bonus {bonus}")
# salary+=bonus           #salary=salary+bonus
# print("Salary with Bonus",salary)

# -Example3
# salary= 50000
# tax=salary*0.005

# print(f"Salary {salary} and Tax {tax}")
# salary-=tax           #salary=salary-tax
# print("Salary after Tax",salary)

#3. Comparison operators: ==, >, >=, <, != etc.
# if(condition):
#   #code
# else:
#   #code

# -Example1  (=>)
# age=int(input("Enter your age \t"))
# if(age>=18):
#     print("You are eligible to participate in voting")
# else:
#     print("You are not eligible to participate in voting, participate again after you reach 18")

# print("End of Program")

# -Example2  (<)
# marks=int(input("Enter marks percentage without '%' sign \t"))
# if(marks<30):
#     print("I'm Sorry, You have Failed in Exam")
# else:
#     print("Congrats! You have PASSED the exam!")

# -Example3  (!=)
# #accessCode="wes12"
# accessCode=input("Enter Access Code: \t")
# if(accessCode!="wes12"):            # '!=': not equal to
#     print("Access Denied!")
# else:
#     print("Welcome to the course")

# -Example4  (==)
##accessCode="wes12"
# accessCode=input("Enter Access Code: \t")
# if(accessCode=="wes12"):            # '==': equal to
#     print("Welcome to the course")
# else:
#     print("Access Denied!")


#4. Logical operators: and, or, not.
# -Example1  (and)  *all conditions must comply, must TRUE then print will be TRUE
# physicsMarks=int(input("Enter marks obtained in Physics \t"))
# ChemistryMarks=int(input("Enter marks obtained in Chemistry \t"))
# mathMarks=int(input("Enter marks obtained in Mathematics \t"))

# if((physicsMarks>=50) and (ChemistryMarks>=50) and (mathMarks>=50)):
#     print("You are eligible to sit in the pre exam of MBBS")
# else:
#     print("You have not passed the required marks to sit for pre exam of MBBS")


# -Example2  (or) *either conditions in the command is true, means TRUE
# idProof=input("Enter ID Proof you have in capital letters \t")

# if(idProof=="PASSPORT") or (idProof=="DL" or (idProof=="VOTER ID")):
#     print(f"Valid ID {idProof} we accept here")
# else:
#     print("Only passport, dl and viter id are accepted as Identity Proof")
#     print(f"{idProof} is not valid ID here")

# -Example3  (not) *'!=' or not can be use for this command. It's same
# mathMarks=int(input("Enter marks obtained in Mathematics: \t"))
# gapYear=int(input("Enter number of Year Gap if any, otherwise 0 \t"))
# if((mathMarks<=55) or (gapYear != 0)):  
#     print("Not Eligble for BTech")
# else:
#     print("Eligible for BTech")


# -Example4  (not) *'!=' or not can be use for this command. It's same
name=input("Enter User Name \t")
if(not name):
    print("Error!!!")
else:
    print ("Welcome",name)