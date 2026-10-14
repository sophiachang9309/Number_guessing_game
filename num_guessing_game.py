#Name: Sophia Chang
# AM

# module that allows this program to generate random numbers
import random

#Generates a random integer from 1 and 10
random_num = random.randint(1,10)

#Initializes an empty list of the previous guesses
previous_guesses = []

#Sets the maximum number of tries to 5 for the player
tries = 5

#Sets a boolean to control whether or not the main game loops continues to run
correct_answer_picked = False

#Explains to the player of how to play the game 
print("You only have ",tries, " tries to guess a number from 1 - 10. Duplicate numbers and numbers below 1 or above 10 don't affect the number of tries.")

#Starts the main game loop
while correct_answer_picked == False and tries > 0:

    #Asks the user for a random number and converts the string to an integer
    user_guess = int(input("Enter a number between 1 - 10: "))

    #Sets a boolean to control whether or not the number is in range of 1-10
    in_range = False

    #Checks whether or not the number is in range of 1-10
    while in_range == False:
        #Checks if the user's guess is out of the range of 1 - 10
        if user_guess < 1 or user_guess > 10:
            #Tells the user that the number isn't valid
            print("Invalid input!")
            #Asks the user for another number
            user_guess = int(input("Please enter a number between 1 and 10:"))      

        #Checks if the number was guessed before
        else:
            #Sets a boolean to control whether or not there's a duplicate
            is_dup = False

            #Loops through each item of the previous_guesses list 
            for num in previous_guesses:
                #Checks whether or not the user's guess is the same as the elements in the previous_guess list
                if num == user_guess:
                    #Basically flags down that there's a match
                    is_dup = True

            #Checks whether or not there's a duplicate in the previous_guesses list
            if is_dup == True:
                #Tells the user that they've already guessed the number
                print("You have already guessed ", user_guess)
                #Tells the user to choose a different number
                print("Choose a different number.")
                #Tells the user what they've already guessed
                print("Previous guesses:", previous_guesses)
                #Reminds the user their tries did not change
                print("You still have", tries, "tries remaining.")
                #Asks the user for a new number
                user_guess = int(input("Enter a number between 1 - 10: "))
            #runs when the guess is in range and not a duplicate
            else:
                #Ends the loop
                in_range =True

    #Adds the valid, new guess to the list
    previous_guesses.append(user_guess)

    #Checks if the user's guess matches the random number
    if user_guess == random_num:
        #Tells the user they won
        print("You guessed correctly! The number was", random_num, ".")
        #Shows the final list of guesses
        print("Your guesses:", previous_guesses)
        #Stops the main game loop
        correct_answer_picked = True
    #Checks if the guess is higher than the random number
    elif user_guess > random_num:
        #Tells the user to go lower
        print("Try again! The random number is lower!")
        #Takes away one try for a valid wrong guess
        tries -= 1

    #Otherwise the guess must be lower than the random number
    else:
        #Tells the user to go higher
        print("Try again! The random number is higher!")
        #Takes away one try for a valid wrong guess
        tries -= 1

    #Runs only if the guess was wrong and the game isn't over yet
    if correct_answer_picked == False and tries > 0:
        #Shows the previous guesses
        print("Previous guesses:", previous_guesses)
        #Shows how many tries are left
        print("You have", tries, "tries remaining.")

#Runs after the loop if the player ran out of tries without winning
if correct_answer_picked == False:
    #Tells the user they lost
    print("You ran out of tries!")
    #Shows all of their guesses
    print("Your guesses were:", previous_guesses)
    #Reveals the random number
    print("The correct number was", random_num, ".")
    #Tells the user that the game ended
    print("Game over!")
