import random

def number_guessing_game():
    random_number = random.randint(1,100)
    attempts = 0
    guess_is_correct = False

    print("I'm thinking of a random number between 1 and 100")
    
    while not guess_is_correct:
        guess = input("Enter a guess: ")

        try:
            guess = int(guess)
        except ValueError:
            print("Enter a valid number")
        else:
            attempts += 1

            if guess < random_number:
                print("Too low")
            elif guess > random_number:
                print("Too high")
            else:
                print(f"You are correct in {attempts} attempts.")
                guess_is_correct = True

