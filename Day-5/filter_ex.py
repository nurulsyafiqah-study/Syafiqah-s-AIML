students_marks={'SAM':60,               #sam-is the key, the marks is the value
                'RAJ':55,
                'MAHA':35,
                'SANDY':45,
                'NIRAJ':76,
                'SYA':99,
                'DEEP':40,
                'GARIMA':54
                }
#_____key=lambda x:x[1] - to do the FILTER
print('All students')
for k,v in students_marks.items():
    print(f'Name:\t{k}\t\tMarks:\t{v}')
#print(students_marks)
pass_students=dict(filter(lambda x:x[1]>=50,students_marks.items()))
print('\nPASSED STUDENTS')
for k,v in pass_students.items():
    print(f'Name:\t{k}\t\tMarks:\t{v}')
#print(f'\n{pass_students}')        - this is just to print including {}''
sort_pass_students=sorted(pass_students.items(),key=lambda x:x[1])  #x:x[1] is for the marks,0 is for name sort
print('Printing in Ascending Order')
print(sort_pass_students)

sort_pass_student_desc=dict(sorted(pass_students.items(),key=lambda x:x[1],reverse=True))       
print('Printing in Descending Order')
for k,v in sort_pass_student_desc.items():
    print(f'Name:\t{k}\t\tMarks:\t{v}')

