import re

print(1+1)
print(1-1)
print(2*10)
print(9/3)
print(9//3)
print(11%2)
print(3**3)

print(5 < 4)
print(32 > 8)
print(100 == 60)
print(10 >= 10)
print(10 <= 10)
print(100 != 60)
print(10 * 5 == 25 * 2)
print(False * 50)

num = 10
num += 10
num -= 10
num *= 4
num /= 4
num //= 4
num **= 2
num %= 2

b = 0
a = 0

print(a is b)

h = "H"
k = "K"
word = "world"
text = "Hello world"
print(word in text)
print(h in text)
print(k in text)


domeny = [".com",".cz"]
email = "honda.hrounda@gmail.com"
domainCheck = False

for domena in domeny:
    if domena in email:
        domainCheck = True
        break

if "@" in email and domainCheck:
    print("email je platný")

if "@" in email and (".com" in email or ".cz" in email) and " " not in email:
    print("email je platný")

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

if re.fullmatch(regex,email):
    print("email je platný")


num = 10

if num >= 0:
    if num == 0:
        print("Je to nula")
    else:
        print("Je to kladné číslo")
else:
    print("Je to zaporné číslo")

a = 10
b = 12
c = 15
if a > b:
    if a > c:
        print(str(a) + " je největší")
    elif c > a:
        print(str(c) + " je největší")
    else:
        print("Je to více největších")
if b > a:
    if b > c:
        print(str(b) + " je nejvštší")
    elif c > b:
        print(str(c) + " je největší")
    else:
        print("Je tu více nejvetších")
else:
    print("Je to více největších")

list = "1,10,150".split(",")
big = 0
for cislo in list:
    if int(cislo) > big:
        big = int(cislo)
pocet = list.count(str(big))
if pocet == 1:
    print("největší je " + str(big))
else:
    print("největší je " + str(big) + " a je tam " + str(pocet) + "krát")