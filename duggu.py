 # Let's make a system for giving grades to students ...
 
 
 
a = str(input("ENTER YOUR NAME :"))
b = str(input("enter your age:"))
c = str(input("enter your school name"))

marks = int(input(("ENTER YOUR MARKS YOU OBTAINED :")))

if(marks >= 90):
    grade = 'A'

elif(marks >=80 and marks <= 90 ):
    grade = 'B'
elif(marks >= 70 and marks <= 80):
    grade = 'C'
elif(marks >= 60 and marks <= 70):
    grade = 'D'
else:
    grade = 'abe Padhai likhai karo ias vis bano ........ fail hai tu ... '
    
    
print('hello ',a)

print('your age is :', b)     
print('your school name is',c)   
print("your grade is :",grade)




 
 
 
 
 