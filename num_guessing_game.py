#Name: Sophia Chang
# AM

import random # module that allows this program to generate random numbers

random_num = random.randint(0,10)
previous_guesses = []
tries = 5

print("You only have 5 tries to guess the number.")
user_guess = int(input("Enter a number between 1 - 10: "))

while user_guess > 10 or user_guess < 1:
    print("Invalid input!")
    tries -= 1
    print("You have ", tries, " tries!")
    if tries > 0:
        user_guess = int(input("Please enter a number between 1 and 10:"))
        for i in range(len(previous_guesses)):
            while user_guess == previous_guesses[i]:
                print("You have already guessed ", user_guess)
                print("Choose a different number.")
                print("Previous guesses:", previous_guesses)
                tries -= 1
                print("You have ", tries, " tries!")
                if tries > 0:
                    user_guess = int(input("Enter a number between 1 - 10:"))
 
if 1 < user_guess or user_guess < 10:
    for i in range(len(previous_guesses)):
        while user_guess == previous_guesses[i]:
            print("You have already guessed ", user_guess)
            print("Choose a different number.")
            print("Previous guesses:", previous_guesses)
            tries -= 1
            print("You have ", tries, " tries!")
            user_guess = int(input("Enter a number between 1 - 10:"))
        previous_guesses.append(user_guess)
    if user_guess == random_num:
        print("You guessed correctly!")
    elif user_guess > random_num:
        print("Try again! The random number is lower!")
        previous_guesses.append(user_guess)
        print("Previous guesses", previous_guesses)
        user_guess = int(input("Enter a number between 1 - 10:"))
    else:
        print("Try again! The random number is higher!")
        previous_guesses.append(user_guess)
        print("Previous guesses", previous_guesses)
        user_guess = int(input("Enter a number between 1 - 10:"))
            
        


    


        
    
