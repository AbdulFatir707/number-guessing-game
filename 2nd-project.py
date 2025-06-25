import random

random_number=random.randint(1,100)

print("Welcome to the number gusseing game! ")
print("I am guessing a number from 1,100 ")

while True:
    guess=int(input("Guess the number: "))

    if guess < random_number:
        print("The number is too low! ")

    elif guess > random_number:
        print("The number is too high!")

    else:
        print("Congragulation! you guessed the correct number. ")
    
        break

