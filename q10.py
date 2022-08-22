# 10.Write a program to display day name on the basis of user’s liking of a colour. Ask
# user for his favorite colour. User can answer in a sentence like “I like red colour”.
# Assuming all colour name entered by user is in lowercase. Use match case to display
# day name associated with the colour.
# a. Yellow - Monday
# b. Blue - Tuesday
# c. Orange - Wednesday
# d. White - Thursday
# e. Black - Friday
# f. Red - Saturday
# g. All other colours - Sunday

str=input("Enter your favourite colour name: ")

match str:
    case str if("yellow" in str):
        print("Monday")
    case str if("blue" in str):
        print("Tuesday")
    case str if("orange" in str):
        print("Wednesday")
    case str if("white" in str):
        print("Thursday")    
    case str if("black" in str):
        print("Friday")  
    case str if("red" in str):
        print("Saturday")
    case _:
        print("Sunday")               