import random

print("Welcome to the dice rolling simulator!")
roll = input("Press enter to roll the dice: ")

roll = ""
num_rolls = 1
roll_results = str(random.randint(1, 6)) 
for i in range(num_rolls):
    print("Your dice result is: " + roll_results)