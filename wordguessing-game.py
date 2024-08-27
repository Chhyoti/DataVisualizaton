import random # to generate random numbers 
# funtion for the number guessing 
def guess_the_numbers():
    number_to_guess = random.randint(1,10)
    guess = None
    limit = 6

    print("Welcome to the  number guessing Game!")
    print("Here we have selested number between 1 to 10. Try to guess it!")  

    while guess != number_to_guess:
        guess = int(input("Enter your guess:"))
        if guess<number_to_guess :
            print("Too low")
        elif guess>number_to_guess:
            print("Too high")
        else:
            print("Congratulations you have guessed right number")
    
guess_the_numbers()