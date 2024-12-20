import random
def roll_dice():
    while True:
        input('Press Enter to roll the dice...')
        result=random.randint(1,6)
        print(f"you rolled a {result}!")
        again=input("Roll again'? (y/n):")
        if again.lower()!='y':
            print("Goodbye!")

            break
roll_dice()
