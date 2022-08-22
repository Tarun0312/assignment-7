# 1. Write a python script to display the number of days in a given month number.

monthNum=int(input("Enter the month number: "))

# match monthNum:
#     case 1:
#         print("31 Days")
#     case 3:
#         print("31 Days")
#     case 5:
#         print("31 Days")      
#     case 7:
#         print("31 Days")
#     case 8:
#         print("31 Days")
#     case 10:
#         print("31 Days")             
#     case 12:
#         print("31 Days")
#     case 2:
#         print("28/29 Days")
#     case 4:
#         print("30 Days")
#     case 6:
#         print("30 Days")
#     case 9:
#         print("30 Days")
#     case 11:
#         print("30 Days")        
#     case _:
#         print("Invalid Month number")    

# Precise coding
match monthNum:
    case monthNum if(monthNum==1 or monthNum==3 or monthNum==5 or monthNum==7 or monthNum==8 or monthNum==10 or monthNum==12):
        print("31 Days")
    case monthNum if(monthNum==2):
        print("28/29 Days")
    case monthNum if(monthNum==4 or monthNum==6 or monthNum==9 or monthNum==11):
        print("30 Days")
    case _:
        print("Invalid Month number")        

