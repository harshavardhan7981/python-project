import random
def number_guessing_game():
    print('Welcome to the Number Guessing Game!')
    print("I'm thinking of a number between 1 and 100.")
    secret_number=random.randint(1,100)
    attempts=0
    while True:
        try:
            guessing=int(input("Enter your guess: "))
            attempts+=1
            if guessing<secret_number:
                print("Low! tyr again.")
            elif guessing>secret_number:
                print("High! tyr again.")
            else:
                print(f"Congratulations, you guessed  the number{secret_number}in {attempts} attempts.")
                break
        except ValueError:
            print("please enter a number.")
number_guessing_game()