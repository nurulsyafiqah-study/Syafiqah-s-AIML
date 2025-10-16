#1-LIST EXAMPLE
# print("List Example 1")

# my_list=[10,30,30,"Python",'syafiqah','dilla',22,11]
# print('The total number of the list are \t',len(my_list))   #len(container name) is to count inside container

# for item in my_list:
#     print(item)

#_________________________________________________________________________________
#2-LIST EXAMPLE
# print("List Example 2")
# students=['SYAFIQAH','DILLA','SYIKIN','MISCHA','AHMAD','ZYRA']
# print('\nThe total number of students attended today:\t',len(students))
# print('\nThe students that attended are:')

# for A in students:
#     print(A,)        #but this will be listed down, if next to another: print(A,end=" ")-separator

#_________________________________________________________________________________
#3-SORT EXAMPLE
#listName.sort()            #in ascending order
# students.sort()
# print("\nSTUDENT NAME LIST IN ASCENDING SORTING:")
# for B in students:
#     print(B)


#_________________________________________________________________________________
#4-REVERSE SORTING EXAMPLE
#listName.reverse()         #sorting in descending order
# students.reverse()
# print('\nSTUDENTS NAME LIST IN DESCENDING ORDER')
# for B in students:
#     print(B)


#_________________________________________________________________________________
#5-APPEND, REMOVE, POP INSERT METHOD

# students=['syafiqah','dilla','syikin','mischa','ahmad','zyra']
# print('\nThe total number of students attended today:\t',len(students))
# print('\nThe students that attended are:')

# for A in students:
#     print(A)        #but this will be listed down, if next to another: print(A,end=" ")-separator

#1__________append : adds the item at the end of the list
# newStudent=input('\nEnter student name to add in the list: \t')
# students.append(newStudent)
# print('\nAfter adding New Student, total number of students are: \t',len(A))
# for A in students:
#     print(A)

#2__________insert(index,item): This will add item at given index
# newStudent=input('\nEnter student name to add in the list: \t')
# position=int(input('Enter the position of the name in the list: \t'))

# students.insert(position,newStudent)
# print('\nAfter adding New Student, total number of students are: \t',len(A))
# for A in students:
#     print(A)

    
#3__________remove : will remove item from the list
#listName.remove(item)
# students=['syafiqah','dilla','syikin','mischa','ahmad','zyra']
# print('Student List')
# for student in students:
#     print(student,end=" ")
# delStudent=input('Student name to remove from the list: \t')
# if delStudent in students:
#     students.remove(delStudent)
#     print(f'Number of student after deleting {delStudent} in the list are: \t',len(students))
#     for A in students:
#         print(A)

# else:
#     print(f"Sorry, this {delStudent} not in the list")




#4__________pop() example : will delete element at given index and return to its value
#listName.pop(index)

students=['syafiqah','dilla','syikin','mischa','ahmad','zyra']
del_index=int(input('The position name to be deleted: \t'))
print('Pop Result:',students.pop{del_index})

print("Number of Students after pop() are:",len(students))
for A in students:
    print(A,end="\t")


#find out first and last element from the list
students=['syafiqah','dilla','syikin','mischa','ahmad','zyra']
print('Number of Students',len(students))
for B in students:
    print(B,end='\t')
count=len(students)
print('\nFirst element of student list is: ',students[0])
print('\nLast element of student list is: ',students[-1])
print('\nSecond last element of the student list is: ',students[-2])
print('\n,'students[count-2])
