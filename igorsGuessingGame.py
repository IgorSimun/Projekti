#Importing random extendion for random int generating.
import random

#Random int from program and number of failed attempts.
pcsRandomNumber = random.randint(0,100)
failedAttempts = 0
print("Welcome to Igor's guessing game.")
print("Guess the number and the program will help you by leading you towards it by saying if its lower or higher.")

#While loop for continuesly guessing the number.
while True:
    usersInput = int(input("Enter your number please: "))
    try:
        if usersInput in range(0, 100):
            if usersInput == pcsRandomNumber:
                print("Your guess was correct!")
                print("Number of failed attempts:", failedAttempts)
                break

            elif usersInput < pcsRandomNumber:
                print("Your input is lower then PcsNumber.")
                print("Please try again.")
                failedAttempts += 1
                continue

            elif usersInput > pcsRandomNumber:
                print("Your number is bigger then PcsNumber.")
                print("Please try again.")
                failedAttempts += 1

#Security elif and except.
        elif usersInput not in range(0, 100):
            print("Your number is not in the given range.")
            print("Try again.")
            continue
    except ValueError:
        print("Your input is not a whole number or not number at all.")
        print("Try again.")
        continue