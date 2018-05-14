# coin flip
from random import randint
y = 0
h=int()
t=int()


while h != t or y == 0: #used "y == 0" to go around h=t @ y=0
    y +=1
    x = randint(1, 2)
    if x == 1:
        h += 1
        print("Heads")
    if x == 2:
        t += 1
        print("Tails")

else:
    print(">>>Heads: %d" % h)
    print(">>>Tails: %d " % t)
    print(">>>Number of Trials: %d" % y)