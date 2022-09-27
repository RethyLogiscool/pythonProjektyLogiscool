for i in range(10):
    print(i)

for i in range(1,11):
    print(i)

suda = []
licha = []
for i in range(2,100,2):
    suda.append(i)
    licha.append(i+1)
print(suda)
print(licha)

for char in "Hello world!":
    print(char)

for num in range(1,11):
    for i in range(1,11):
        print("{0} * {1} = {2}".format(str(i), str(num), str(i*num)))

for i in range(5,101,5):
    print(i/10)

encrypted_mess = "Wyh earne  eclaenp hIa nbtu?"
decrypted_mess = ""
for i in range(len(encrypted_mess)):
    if i % 2 == 0:
        decrypted_mess += encrypted_mess[i]
for i in range(len(encrypted_mess)):
    if i % 2 == 1:
        decrypted_mess += encrypted_mess[i]
print(decrypted_mess)

decrypted_mess = "Hello, my name is Andrew"
first_half = decrypted_mess[:(len(decrypted_mess)+1)//2]
second_half = decrypted_mess[(len(decrypted_mess)+1)//2:]
encrypted_mess = ""
print(first_half + second_half)
for i in range((len(decrypted_mess)+1)//2):
    encrypted_mess += first_half[i]
    if i < len(second_half):
        encrypted_mess += second_half[i]
print(encrypted_mess)

def encrypt_mess(zprava):
    first_half = zprava[:(len(zprava)+1)//2]
    second_half = zprava[(len(zprava)+1)//2:]
    encrypted_mess = ""
    print(first_half + second_half)
    for i in range((len(zprava)+1)//2):
        encrypted_mess += first_half[i]
        if i < len(second_half):
            encrypted_mess += second_half[i]
    return encrypted_mess

def decrypt_mess(zprava):
    decrypted_mess = ""
    for i in range(len(zprava)):
        if i % 2 == 0:
            decrypted_mess += zprava[i]
    for i in range(len(zprava)):
        if i % 2 == 1:
            decrypted_mess += zprava[i]
    return decrypted_mess


zprava = encrypt_mess("Ahoj jak se máš?")
print(zprava)
print(decrypt_mess(zprava))


numbers = []
for i in range(1,11):
    for j in range(1,11):
        numbers.append(i*j)
print(numbers)


for i in range(10):
    print(numbers[i*10:(i*10)+10])
 




