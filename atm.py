#register
# - firstname, lastname, password, email
# - generate user account


#login
# - account number and password

#bank operations

import random
from datetime import datetime
now = datetime.now()
currentDateAndTime = now.strftime("%B %d, %Y %H:%M:%S")

database = {}

#Initializing the system

def init():
  print("Welcome to The Vault ATM")
  print(currentDateAndTime)
    
  accountHolder = int(input("Do you have an account with The Vault Bank? 1(yes) 2(no) \n"))
  if (accountHolder == 1):
    login()
  elif (accountHolder == 2):
    register()
  else:
    print("You have selected an invalid option. Try again")
    
    init()
    
  
def register():
  print("*** Register Now With Us ***")
  print(currentDateAndTime)
  
  email = input("Enter your email address: \n")
  firstName = input("\nWhat is your first name? \n")
  secondName = input("\nWhat is your second name? \n")
  password = input("\nEnter your password: \n")
  accountBalance = 0
  
  accountNumber = generateAccountNumber()
  
  database[accountNumber] = [firstName, secondName, email, password, accountBalance]
  
  print("Your Account creation was successful....")
  print(f"\nThis your account number: {accountNumber}.")
  print("Thank you for registering with us....")
  
  login()
  
def login():
  print(currentDateAndTime)
  print("Login into your account")
    
  userAccountNumber = int(input("\nEnter your account number: \n"))
  userPassword = input("\nEnter your password: \n")
  
  for accountNumber, userDetails in database.items():
    if (accountNumber == userAccountNumber):
      if (userDetails[3] == userPassword):
        bankOperations(userDetails)
        
  print("\nInvalid account number or password")
  login()
  
  
def bankOperations(user):
  print(currentDateAndTime)
  print("Welcome %s %s" % ( user[0], user[1] ))
  userAction = int(input("What would you like to do? (1) deposit,(2) withdrawal, (3) Check Account Balance, (4) complaint, (5) Logout, (6) Exit \n"))
  
  if (userAction == 1):
    depositOperation(user)
  elif(userAction == 2):
    withdrawalOperation(user)
  elif(userAction == 3):
    getBalance(user)
  elif(userAction == 4):
    complaint()
  elif(userAction == 5):
    logout()
  elif(userAction == 6):
    exit()
  else:
    print("You've entered an invalid option")
    
    bankOperations(user)
  
  
def depositOperation(userDetails):
  deposit = int(input("\nHow much would you like to deposit? \n"))
  
  userDetails[4] += deposit
  balance = userDetails[4]
  print("Operation succesful...")
  print("Available balance: %s" % (balance))
  
  anotherOperation = int(input("Would you like to perform another transaction? 1(yes), 2(no) \n"))
  
  if (anotherOperation == 1):
    bankOperations(userDetails) 
  else:
    exit()
  
  
def withdrawalOperation(userDetails):
  withdrawal = int(input("\nHow much would you like to withdraw? \n"))
  
  if (userDetails[4] != 0 and withdrawal < userDetails[4]):
    userDetails[4] -= withdrawal
    balance = userDetails[4]
    print("Operation successful...")
    print("Available balance: %s" % (balance))
  else:
    print("Insufficient balance. Please try again")
    bankOperations(userDetails)
  
  anotherOperation = int(input("Would you like to perform another transaction? 1(yes), 2(no) \n"))
  
  if (anotherOperation == 1):
    bankOperations(userDetails) 
  else:
    exit()
    
def getBalance(userDetails):
  balance = userDetails[4]
  print(f"Your current account balance is: {balance}")
  
  anotherOperation = int(input("Would you like to perform another transaction? 1(yes), 2(no) \n"))
  
  if (anotherOperation == 1):
    bankOperations(userDetails) 
  else:
    exit()
  
def complaint():
  userComplaint = input("\nWhat will you like to report? \n")
  print("Thank you for contacting us.")
  exit()

def logout():
  print("signing out....")
  login() 
  
def generateAccountNumber():
  return random.randrange(1111111111, 9999999999)
  
init()



