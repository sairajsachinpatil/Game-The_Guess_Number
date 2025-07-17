print("🎯 Welcome to the Number Guessing Game! 🎯")
print("I'm thinking of a number... Can you guess it?")
print("Hint: It's between a secret range... 😉")
print()

import random
a=random.randrange(1,1000)
b=(a-100,a+100)
print("The Number Is Between Range:",b)

while True:
    gues=int(input("👉 Your Guess: "))
    if gues==a:
        print(" 🎉Congrats! You guessed it right!")
        print("\n🏁 Thanks for playing! See you again 🎮")
        break
    elif gues<a:
        print("📉 Too low! Try a higher number.\n")
    else:
         print("📈 Too high! Try a lower number.\n")

