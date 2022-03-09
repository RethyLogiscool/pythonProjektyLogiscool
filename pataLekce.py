number = 1;
#while True:
#    number += 1;
#    print(number)

sum = 0
while number < 11:
    print(number);
    sum += number;
    number += 1;
print("součet je: ",sum)

number = 9845198
count = 0
while number != 0:
    number //= 10;
    count+=1
print("počet řádů: ", count)

"""
number = 88
guessnum = int(input("Kolik chceš pokusů \n"))
guess = 0
while guessnum > 0 and guess != number:
    guess = int(input("Hádej číslo: \n"))
    if guess > number:
        print("Myslím si menší číslo")
    elif guess < number:
        print("Myslím si větší číslo")
    guessnum -= 1
    print("Máš ještě " + str(guessnum) + " pokusů.")
if guess == number:
    print("Správně, měl jsem na mysli číslo " + str(guess));
else:
    print("Bohužel, třeba přístě. Myslel jsem si " + str(guess))
"""

counter = 10
num1 = 0
num2 = 1
print("Fibonacciho sekvence: ", end="");
while counter > 0:
    print(str(num1), end="")
    temp = num1 + num2
    num1 = num2
    num2 = temp
    counter -= 1

print("")
"""
i = 0
times = int(input("Kolikrát to chceš říct"))
word = "If you happy and you know it... "
while i < times:
    tempInput = input("Co mám říct?: ")
    print("{0} {1}".format(word, tempInput))
    i += 1

"""

number = 2
counter = 2
isPrime = True
while number < 1000000000:
    counter = 2
    isPrime = True
    while counter < number:
        if number % counter == 0:
            isPrime = False
        counter += 1
    if isPrime:
        print(number)
    number += 1