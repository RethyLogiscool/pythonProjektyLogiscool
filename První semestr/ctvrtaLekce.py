import re


print(1+1)
print(1-1)
print(2*10)
print(9/3)
print(9/2)
print(1900 % 100)
print(3 ** 3)
print(11 / 3)
print(11 // 3)

num = 10
print(num)
num += 5
print(num)
num -= 5
print(num)
num *= 4
print(num)
num /= 4
print(num)
num //= 4
print(num)
num **= 2
print(num)

print(5 < 4)
print(32 > 8)
print(100 == 60)
print(100 != 60)
print(10 * 5 == 25 * 2)
print(True * 50)

b = 0
a = b

print(a is b)

x1 = 5
x2 = 5
x3 = 8
y1 = "random name"
y2 = "random animal"
print(x1 is x2)
print(x1 is x3)
print(x1 is y1)
print(y1 is y2)
print(y1 is y1)

h = "H"
k = "K"
world = "world"
text = "Hello world"
print(world in text)
print(h in text)

c1 = 4
c2 = 4
if c1 < c2:
    print(str(c1) + " je menší než " + str(c2))

if c1 ** c2 == c2 ** c1:
    print(str(c1) + "^" + str(c2) + " se rovná " + str(c2) + "^" + str(c1))

if c1 ** c2 != c2 ** c1:
    print(str(c1) + "^" + str(c2) + " se nerovná " + str(c2) + "^" + str(c1))

email = "honza.hrouda@chodim.online"
if "@" in email and " " not in email and ( email[-4] == "." or email[-3] == "."):
    print(" ")

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

if re.fullmatch(regex,email):
    print("VALID " + email)



if num >= 0:
    if num == 0:
        print("Nula")
    else:
        print("Kladné číslo")
else:
    print("Záporné číslo")

a = 50
b = 100
c = 12
if a > b:
    if a > c:
        print(str(a) + " je největší")
    elif c > a:
        print(str(c) + " je největší")
    else:
        print("Je tu více největších čísel")
elif b > a:
    if b > c:
        print(str(b) + " je největší")
    elif c > b:
        print(str(c) + " je největší")
    else:
        print("Je tu více největších čísel")
else:
    print("Je tu více největších čísel")

list = input("Zadej čísla: ").split(",")
big = 0
for i in list:
    if int(i) > big:
        big = int(i)
print(big)
