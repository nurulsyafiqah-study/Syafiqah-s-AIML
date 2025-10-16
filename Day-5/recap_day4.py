# print('____________RECAP FUNCTIONS____________')
# def display():
#     print('Welcome to functions recap')

def welcome(name1):
    print('Welcome to functions Mr./Ms. ',name1)

def cube(num):          #num is parameters
    cube_num=num*num*num
    # print(f'Cube of {num} is equal to :\t',cube_num)          # or you can use this code
    print(f'Cube of {num} is: \t {cube_num}')

def square(num):
    return num*num


username=input('Enter your name:')
numInput=int(input('Enter the number to find out the cube of it:\t'))
welcome(username)
cube(numInput)
square(numInput)
print(f'The square of {numInput} is: \t',square(numInput))

#_________________________________________________________________________________________

