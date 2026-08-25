import random
print("Hi welcome to the Number guessing game.\n you have 7 chances to guess the number.Lets start!")

low = int (input("Enter the Lower Bound:"))
high = int(input("Enter the Upper Bound:"))

print(f"\nYou have 7 chances to guess the number between {low} and {high}.Let's start")

num = random.randont(low,high)
#total allowed chances
ch = 7
#Guess counter
gc = 0

while gc < ch:
    gc += 1
    guess = int(input("Enter your guess and make it with a best:"))

    if guess == num:
        print(f'correct!  The number is {num}.You guesses it in [gc] attempts.')
        break
    elif gc >=ch and guess != num:
        print(f'sorry!The number is{num}.Better Luck next time.')
