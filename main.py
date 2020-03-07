from app import *
from model import *


while True:
    print("--"*30)
    print("Hello, Welcome to Aptitude test \n\
        Here you can test your aptitude skills\n\
            This test contains 3 Levels input\n\
                each question has 5 marks1")
    print("what would you like to do\n\
        1.Signup for the test\n\
        2.Login\n")
    option=input("==>")
    if option == "1":
        signup() 
    elif option=="2":
        user=login()
        if user.compcomplete==True:
            print("User has already attended the test\n")
        else:
            test(user)
    else:
        break
    