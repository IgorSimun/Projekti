#Importing module for generating a random integer.
import random

#Variable determening range of the random int simulating the dice roll.
randomRoll = random.randint(1,6)

#While loop for reapeating of dice roll if player desires so.
while True:

    #Input question for player.
    playQuestion = input("Would you like to roll the dice? yes or no? ").lower()

    #Positive input outcome.
    if playQuestion == 'yes':
        print("Your dice roll number is: ", randomRoll)
        continue
    
    #Negative input outcome.
    elif playQuestion == 'no':
        print("Thanks for playing the dice roll.")
        break

    #Wrong input outcome.
    else:
        print("Wrong input, please try again. ")
        continue