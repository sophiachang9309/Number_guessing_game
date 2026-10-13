#Name: Sophia Chang
# AM

import random # module that allows this program to generate random numbers

random_num = random.randint(0,10)
previous_guesses = []
tries = 5
correct_answer_picked = False
pass1 = False
is_dup = False

print("You only have 5 tries to guess the number. Duplicate numbers and numbers below 1 or above 10 don't affect the number of tries.")
user_guess = int(input("Enter a number between 1 - 10: "))

while user_guess > 10 or user_guess < 1: # checks whether or not the  
    print("Invalid input!")
    user_guess = int(input("Please enter a number between 1 and 10:"))      



while correct_answer_picked == False: # loops until the correct answer is picked
    if 1 < user_guess and user_guess < 10:

        while pass1 == False: # checks duplicates 
            for i in range(len(previous_guesses)): # checks for duplicates
                while user_guess == previous_guesses[i]:
                    print("You have already guessed ", user_guess)
                    print("Choose a different number.")
                    is_dup = True

            if is_dup == True:
                user_guess = int(input("Please enter a number between 1 and 10:"))
            else: 
                pass1 = True
        
        previous_guesses.append(user_guess)
                        
        
        print("Previous guesses:", previous_guesses)
        print("You have ", tries, " tries!")
        user_guess = int(input("Enter a number between 1 - 10:"))
        if user_guess == random_num:
            print("You guessed correctly!")
            correct_answer_picked = True
        elif user_guess > random_num:
            print("Try again! The random number is lower!")
            user_guess = int(input("Enter a number between 1 - 10:"))
        else:
            print("Try again! The random number is higher!")
            user_guess = int(input("Enter a number between 1 - 10:"))
        if user_guess > random_num:
        
            print("Try again! The random number is lower!")
            tries -= 1
            print("You have ", tries, " tries!")
            previous_guesses.append(user_guess)
            print("You have guessed these numbers: ", previous_guesses)
            user_guess = int(input("Enter a number between 1 - 10:"))
        elif user_guess < random_num:
            print("Try again! The random number is higher!")
            tries -= 1
            print("You have ", tries, " tries!")
            previous_guesses.append(user_guess)
            print("You have guessed these numbers: ", previous_guesses)
            user_guess = int(input("Enter a number between 1 - 10:"))

if tries == 0:
        print("You have ", tries, " tries.")
        print("The correct number was ", random_num, ".")
        print("Game over!")
