# 8. Write a python script to check whether two given strings are identical, first string
# comes before the second in dictionary order or first string comes after the second
# string in dictionary order using match case statement

str1=str(input("Enter two strings: "))
str2=str(input())

match str1:
    case str1 if(str1==str2):
        print("Strings are same")
    case str1 if(str1>str2):
        print("First string comes after the second in dictionary order")
    case str1 if(str1<str2):
        print("First string comes before the second in dictionary order")        
