# 7. Write a python program to check whether a given number is positive, negative or
# zero using match case statement

num=float(input("Enter a number: "))

match num:
    case num if(num>0):
        print("Positive number")
    case num if(num<0):
        print("Negative number") 
    case _:
        print("Zero")       