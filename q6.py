# 6.Write a python program to check whether a given string is a multiword string or single
# word string using match case statement

s=str(input("Enter a string(but first character can't be space): "))

match s:
    case s if(' ' in s):
        print("Multiword string")
    case _:
        print("Single Word String") 
