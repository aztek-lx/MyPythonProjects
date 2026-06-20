import random

#
## Start of Part 1 - User Guesses
NumChosen = random.randint(0, 100)
print()
print ("A random between 0 and 100 (including both endpoints) has been chosen.")
print ("You will have to guess the number")
print()
#begining user input loop
Found = False
Count = 0
while Found == False:
    print("Enter your guess:")
    Guess = int(input())
    print()
    Count += 1
    if Guess > NumChosen:
        print("Your guess is too large.")
        print()
    elif Guess < NumChosen:
        print("Your guess is too small.")
        print()
    else:
        print("Well done! You guessed the number.")
        print("It took you", Count, "tries")
        print()
        Found = True
#reseting variables
Found = False
## End of Part 1 - User Guesses
#

#
## Start of Part 2 - Computer Guesses
Found = False
Low = 0
High = 100
Count = 0

print("<------------------------->")
print()
print("Pick a number between 0 and 100 (including both endpoints).")
print("Binary search will be used to guess your chosen number.")
print()

while not Found:
    Attempt = round((Low + High)/2)
    print("Is your chosen number", str(Attempt), "? (y = Yes, s = too large, l = too small)")
    Response = input()
    print()
    Count += 1

    if Response.lower() == "s":
        High = Attempt
    elif Response.lower() == "l":
        Low = Attempt
    elif Response.lower() == "y":
        print("It took", Count, "tries to get it")
        Found = True
#
## End of Part 2 - Computer Guesses
    