# 2. Write a menu driven program to perform following operations - Addition, Subtraction,
# Multiplication, Division

from turtle import clearscreen

while(1):
 clearscreen
 print("\n\n1.Addition\n2.Subtraction\n3.Multiplication\n4.True Divsison\n5.Floor Divsion\n6.Exit\n")
 choice=int(input("Enter your choice: "))
 match choice:
       case 1:
        x=eval(input("Enter two number to add: "))
        y=eval(input())
        print("Sum is",x+y)
       case 2:
        x=eval(input("Enter two number to subtract: "))
        y=eval(input())
        print("Subtraction is",x-y)    
       case 3:
        x=eval(input("Enter two numbers for multiplication: "))
        y=eval(input())
        print("Multiplication is",x*y)
       case 4:
        x=eval(input("Enter two numbers for true division: "))
        y=eval(input())   
        print("True divsion is",x/y)
       case 5:
        x=eval(input("Enter two numbers for floor division: "))
        y=eval(input())    
        print("Floor divsion is",x//y)    
       case 6:
        print("Press enter to exit")
        input()
        exit()    
    


