class InvalidAge(Exception):
    pass                # wajib ada pass bcs there's nothing inside the class
def check_age(age):
    if(age<=0):
        raise InvalidAge('Age should not be negative')
    elif(age<18):
        raise InvalidAge('Age should be above 18 years old')
    elif(age>=80):
        raise InvalidAge('Cannot be hired')
    else:
        print(f'Age {age} is accepted and valid for employment')

try:
    userage=int(input('Enter your age:\t'))
    check_age(userage)
except Exception as ex:
    print('Error!',ex)
