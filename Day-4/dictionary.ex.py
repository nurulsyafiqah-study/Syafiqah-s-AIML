#__________DTIONARY EXAMPLE 1
# employee= {'id':1,
#            'name':'sam',            #has to be in '' for non interger
#            'salary':60000.30
#            }

# print('Employee Details as follows: ')
# for key, value in employee.items():
#     print(key, '\t\t',value)

# employee['city']='Muscat'
# print('\nDictionary after adding City\n')

# for key, value in employee.items():
#         print(key, '\t\t',value)

##IF YOU WANT TO DELETE DATA
# del employee['salary']
# print('\nEmployee Details after deleting Salary\n')
# for key, value in employee.items():
#       print(key,'\t\t',value)


# employee= {'id':1,
#            'name':'sam',            #has to be in '' for non interger
#            'salary':60000.30
#            }

# print('\nAll keys from Employee\n')
# for k in employee.keys():
#     print(k,end='\t')

# print('\nAll values from Employee\n')
# for v in employee.values():
#     print(v,end='\t')

#THE OTHER WAY TO WRITE THE DICTIONARY CODE
employee= {'id':1,
           'name':'sam',            #has to be in '' for non interger
           'salary':60000.30            #items is for all,
            }
print('\nAll KEYS from employee\n')
for k in employee.keys():           #keys is data at the front
    print(k,end='\t')

print('\nAll VALUES from employee\n')
for v in employee.values():         #values is data at the back
    print(v,end='\t')
    
print('\nKey:Value\n')
for k,v in employee.items():
    print(k,':',v)

print('\nDictionary is as follows')
print(employee)