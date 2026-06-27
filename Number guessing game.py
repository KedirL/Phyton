
import random

print("Welcome to Number Guessing Game")
def generate_random_number():
     return random.randint(1,100)

random_number = generate_random_number()
print(random_number)
print("Do you want the hint?\nEnter\nYes for hint || No for no")
hint = input("Enter your choice: ")
if hint.lower() == "yes":
    print("Enter range of gues number")
    minimum = int(input("Enter minimum number: "))
    maximum = int(input("Enter maximum number: "))

    if random_number in range(minimum, maximum):
        print("You are one step closer. \nYou are in the right range")
    else:
        print("You have missed the range\nThe number is out side of your guessed range.\nSo be wise.")
elif hint.lower()=="no":
    print("You are confident in your guessing.\nGood Luck")

attempts = 0

guess = int(input("Guess a number between 1 and 100: "))
while guess != random_number:
    if guess < random_number:
        print("Too low. Go a bit higher")
    elif guess > random_number:
        print("Too high. Go a bit lower")
    attempts += 1
    guess = int(input("Enter your next guess: "))

if attempts <=3:
   print("Congratulations! You guessed the number in less than 3 attempts")
   print("You have won yourself a big cup of coffee.\nDM ME FOR YOUR PRIZE IN LESS THAN 40 MINUTE!")