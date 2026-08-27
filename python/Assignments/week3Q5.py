dict={'alice':25,'bob':80,'cat':45,'tania':100,'khushbu':95,'nahida':0}
while True:
    print('choose an operation')
    print('A-Add a student\nB-Update marks\nC-Search for a student\nD-Display all the students and marks')
    ch=input()
    if(ch=='A'):
        name=input("Enter the student name : ")
        marks=input("enter his marks: ")
        dict.update({name:marks})
    elif(ch=='B'):
        name=input("Enter the existing student name : ")
        if name in dict:
            marks=input("update the  marks:")
            dict[name]=marks
        else:
            print('student not found')
    elif(ch=='C'):
        name=input('Enter the student name : ')
        if name in dict:
            print(f'Found!\nHere is your Student  \n The student is {name}\nmark is {dict[name]}')
        else:
            print('the person is not our student')
    elif(ch=='D'):
        print(dict.items())
    else:
        print('you have entered a wrong input')
        break
    
