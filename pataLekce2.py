import time
import random

num = 1
"""while True:
    num += 1
    print(num)
"""

sum = 0
while num <= 10:
    print(num)
    sum += num
    num += 1
print("součet je ",num)

num = 9842165
count = 0
while num != 0:
    num //= 10
    count += 1
print("počet rádů ", count)

counter = 10
num1 = 0
num2 = 1
print("Fibonacciho sekvence: ", end="")
while counter > 0:
    print(str(num1), end=", ")
    temp = num1 + num2
    num1 = num2
    num2 = temp
    counter -= 1

print("")

num = 0
counter = 2
isPrime = True
startTime = time.time();
while num < 100:
    counter = 2
    isPrime = True
    while counter < num:
        if num % counter == 0:
            isPrime = False
            break
        counter += 1
    if isPrime:
        print(num)
    num += 1
endTime = time.time();
print("Trvalo to", endTime-startTime)
"""
num = random.randint(1,100)
guessnum = int(input("Kolik chceš pokusů: \n"))
guess = 0
while guessnum > 0 and guess != num:
    guess = int(input("Hadej číslo: \n"))
    if guess > num:
        print("Myslím si menší číslo")
    elif guess < num:
        print("Myslím si větší číslo")
    guessnum -= 1
    print("Máš ještě {0} pokusů".format(guessnum))
if guess == num:
    print("Správně, měl jsem na mysli číslo {0}".format(num))
else:
    print("Bohužel, třeba příště. Myslel jsem si {0}".format(num))
    """


i = 0
times = int(input("Kolik to mam zopakovat \n"))
word = "If you happy and you know it... "
while i < times:
    tempInput = input("Co mám říct?: ")
    print("{0} {1}".format(word, tempInput))
    i += 1


