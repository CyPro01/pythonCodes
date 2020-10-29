import random
import time
import sys


def Coin():
    print("Flipping Coin")
    string ="\|/\|/\|/\|/\|/\|/\|/\|/\|/" #To give the feel of filp ;P

    for i in string:
        time.sleep(.1)
        print(i)

    a = ['Heads','Tails']
    b = random.choice(a)
    return b

input("First Decide What You want! Then press Enter to Flip")

print(Coin())

time.sleep(2)

x = input("Want to go for best of 3 ? Press 'Y' for Yes and 'N' for No: ").upper()
coin = []
if x == 'Y':
    for i in range(0,3):
        face = Coin()
        coin.append(face)
    print(coin)
elif x == 'N':
    print("OK. Bye!")
else:
    print("Incorrect choice!!")

