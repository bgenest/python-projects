##number guesser 
import random
print("Welcome to the number guesser")

limit_low = 0
limit_high = 5

x = random.randint(limit_low,limit_high)
y = 0

while x != y:
    y = int(input("Guess the number:"))
    y = int(y)



print("you got it! the number was",x)

input()

