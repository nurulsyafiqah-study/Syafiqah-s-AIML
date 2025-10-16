# take user marks from user within 0 to 50
#if the user enter outside [0-50] raise Error InvlidMarks using Custom Exception
#give chance to user till he/she entered the valid marks



class InvalidMarks(Exception):
    pass
        
def check_marks(marks):
    if(marks<0):
        raise InvalidMarks('Marks should not be less than 0')
    elif(marks>50):
        raise InvalidMarks('Invalid Marks! Marks cannot be above 50')
    else:
        print(f'Dear {username}, your marks is {marks} is qualified to sit for Physical Exam')
while True:
        try:
            username=input('Please enter your name:\t')
            marks=int(input('Please enter your marks:\t'))
            check_marks(marks)
        except InvalidMarks as e:
             print('Marks:\t',e)
        except Exception as ex:
            print('Error!',ex)
            break
        choice=input('Continue to next participants? Y/N:\t').lower()
        if(choice!='y'):
             print('Thank you for using the system')
             break
        

