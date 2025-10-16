# def salBonus(salary):
#     return salary*0.1

# my_sal=float(input('Enter salary to find out the bonus: \t'))
# bonus=salBonus(my_sal)
# print(f'Salary is {my_sal} \t Bonus is {bonus}')
# print(f'Salary after bonus is \t',my_sal+bonus)

def salBonus(salary):
    bonus=salary*0.1
    print(f'Salary {salary} Bonus: {bonus}')

my_sal=float(input('Enter salary to find out bonus:\t'))
salBonus(my_sal)
# print(f'salary after bonus = \t',bonus+my_sal)   =====this is not possible bcs bonus formula not outside the function