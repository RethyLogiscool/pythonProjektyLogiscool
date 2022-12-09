seznamOvoce = ["banán","jablko","hruška"]

for ovoce in seznamOvoce:
    print(ovoce)

for i in range(seznamOvoce.__len__()):
    print(seznamOvoce[i])
    seznamOvoce.append("jahoda")

print("---")
i = 0
while i < seznamOvoce.__len__()-1:
    print(seznamOvoce[i])
    i += 1


for i in range(0,10,2):
    print(i)

i = 0
while i < 10:
    print(i)
    i += 2

for i in range(5):
    print("AHOJ")

for i in range(5,10):
    print(i)

for i in range(0,1001,2):
    print(i)

for pismeno in "Hello world":
    print(pismeno)



for x in range(1,11,1):
    for i in range(1,11,1):
        print(f"{i} * {x} = {i*x}")


message = "Ahoj, já jsem Ondra"

print(message)
encrypted_message = ""
for i in range(0,len(message),2):
    encrypted_message += message[i]
for i in range(1,len(message),2):
    encrypted_message += message[i]

print(encrypted_message)

firstHalf = encrypted_message[:(len(encrypted_message)+1)//2]
secondHalf = encrypted_message[(len(encrypted_message)+1)//2:]

decrypted_message = ""

for i in range(len(firstHalf)+len(secondHalf)):
    if i % 2 == 0:
        decrypted_message += firstHalf[i//2]
    else:
        decrypted_message += secondHalf[i//2]

print(decrypted_message)

abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
lenAbc = len(abc)
message = "ahoj, ja jsem ondra"
key = 5
caesar = "fmto, of oxjr tsiwf"

print(message)

encrypted_message = ""

for i in message:
    if i in abc:
        abcI = abc.index(i)
        if (abcI + key) >= lenAbc:
            abcI = abcI + key - lenAbc
        else:
            abcI = abcI + key
        encrypted_message += abc[abcI]
    else:
        encrypted_message += i

print(encrypted_message)

decrypted_message = ""

for i in encrypted_message:
    if i in abc:
        decrypted_message += abc[abc.index(i) - key]
    else:
        decrypted_message += i

print(decrypted_message)

guestList = ["Pavel", "Honza", "David", "Martin"]

name = "Pavel"

inList = False

for guest in guestList:
    if name == guest:
        inList = True

if inList:
    print("Ano, jmeno je na seznamu")
else: 
    print("Jmeno neni na seznamu")

if name in guestList:
    print("Ano, jmeno je na seznamu")
else: 
    print("Jmeno neni na seznamu")


for i in range(100, -100, -1):
    print(i)
