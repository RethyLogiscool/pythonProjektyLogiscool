for i in range(0,10,2):
    print(i)

i = 0
while(i < 10):
    print(i)
    i+=2

sum = 0
number = 1
while number < 101:
    print(number)
    sum += number
    number += 1

print(f"Součet je {sum}")

number = 861289389127481724987124897941789174897124
count = 0
while number != 0:
    number //= 10
    count += 1
print(f"Počet řádů {number}")

counter = 10
num1 = 0
num2 = 1
print("Fibonacciho sekvence:", end=" ")
while counter > 0:
    print(str(num1), end=" ")
    temp = num1 + num2
    num1 = num2
    num2 = temp
    counter -= 1

number = 2
counter = 2
isPrime = True
while number < 100:
    counter = 2
    isPrime = True
    while counter < number/2+1 and isPrime:
        if number % counter == 0:
            isPrime = False
        counter += 1
    if isPrime:
        print(number)
    number += 1


i = 0
times = int(input("Kolikrát to chceš říct: "))
tmInput = input("Co mám říct?: ")
while i < times:
    print(tmInput)
    i += 1

