from model import *


db.connect()

def signup():
	username = input("Create username: ")
	password = input("Create password: ")

	exists = len(User.select().where(User.username == username))

	if exists == 0:
		User.create(username=username, password=password)
		print("Signed up successfully!")
    else:    
		print("Username already Exists! Use another username.")

def login():
	username = input("Enter username: ")
	password = input("Enter password: ")

	user = User.select().where(User.username == username)

	if len(user):
		user = user[0]

		if user.password == password:
			print("\nLogin successfull!")
			return user
		else:
			print("Incorrect password!")
	else:
		return None

def test(user):
    mark= User.Marks
    print("--"*20)
    print("Level 1")
    print("--"*20)
    for i in len(Level1.l1que):
        print(Level1.l1que.get(i+1))
        ans=input("Enter the option: ")
        if ans==Level1.l1ans.get(i+1):
            mark.l1mark+=5
        else:
            print("Incorrect answer")
            print(f"Correct answer is {Level1.l1ans.get(i+1)}")
    print(f"Your marks for Level 1 is {mark.l1mark}")
    
    
    print("--"*20)
    print("Level 2")
    print("--"*20)
    for i in len(Level2.l2que):
        print(Level2.l2que.get(i+1))
        ans=input("Enter the option: ")
        if ans==Level2.l2ans.get(i+1):
            mark.l2mark+=5
        else:
            print("Incorrect answer")
            print(f"Correct answer is {Level2.l2ans.get(i+1)}")
    print(f"Your marks for Level 2 is {mark.l2mark}")


    print("--"*20)
    print("Level 3")
    print("--"*20)
    for i in len(Level3.l3que):
        print(Level3.l3que.get(i+1))
        ans=input("Enter the option: ")
        if ans==Level3.l3ans.get(i+1):
            mark.l3mark+=5
        else:
            print("Incorrect answer")
            print(f"Correct answer is {Level3.l3ans.get(i+1)}")
    print(f"Your marks for Level 3 is {mark.l3mark}")


    mark.total=mark.l1mark+mark.l2mark+mark.l3mark
    printf(f"Your total marks is {mark.total}")
    user.compcomplete=True
    
    