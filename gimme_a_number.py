print("Guess the Number: A Game")
print("First, let's determine the range.")
num1 = int(input("Enter a number for the lower bound: "))
num2 = int(input("Enter a number for the upper bound: "))
tries = int(input("Enter the number of tries you are willing to take to guess your number: "))
print("The number you're guessing is between ", num1," and ", num2, ". You have", tries, "tries.")

import random
guessesTaken = 0
hidden = random.randint(num1, num2)
# print("The number is", hidden)

while guessesTaken < tries:
    print("Take a guess: ")
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1
    if guess < hidden:
        print("Your guess is too low.")
    if guess > hidden:
        print("Your guess is too high.")
    if guess == hidden:
        break
if guess == hidden:
    print("hell yea b! you got it in only ", guessesTaken , " guesses!")

if guess != hidden:
    print('Ya fucked up. The number was ', hidden)