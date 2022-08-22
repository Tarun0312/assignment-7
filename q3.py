# 3. Write a menu driven program with the following options:
# a. Check whether a given set of three numbers are lengths of an isosceles
# triangle or not
# b. Check whether a given set of three numbers are lengths of sides of a right
# angled triangle or not
# c. Check whether a given set of three numbers are equilateral triangle or not
# d. Exit.

from turtle import clearscreen

while(1):
    clearscreen
    print("\n\n1.Isosceles triangle or not\n2.Right angle triangle or not\n3.Equilateral triangle or not\n4.Exit\n")
    choice=eval(input("Enter your choice: "))
    match choice:
        case 1:
            a=eval(input("Enter three sides of a triangle : "))
            b=eval(input())
            c=eval(input())
            print("Islosceles triangle" if(a==b or b==c or a==c) else "Not an isoceles triangle")
        case 2:    
            l=eval(input("Enter three sides of a triangle : "))
            b=eval(input())
            h=eval(input())
            print("Right angle triangle" if(h*h==l*l+b*b) else"Not a right angle triangle")  
        case 3:
            a=eval(input("Enter three sides of a triangle : "))
            b=eval(input())
            c=eval(input())
            print("Equilateral triangle" if(a==b and b==c) else'Not an equilateral triangle')
        case 4:
            print("Press enter to exit")
            input()    
            exit()


