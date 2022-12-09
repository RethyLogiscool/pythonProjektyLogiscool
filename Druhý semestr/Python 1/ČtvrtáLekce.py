import re

print(1+1)
print(1-1)
print(2*10)
print(9/3)
print(9/2)
print(9//2)
print(11%2)
print(3**3)

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
num **= 4
print(num)

print(5 < 4)
print(32 > 8)
print(100 == 60)
print(100 != 60)
print(10*5 == 25*2)
print(False * 50)

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
print(k in text)

c1 = 4
c2 = 7

if c1 < c2:
    print(f"{c1} je menší než {c2}")
if c1 ** c2 == c2 ** c1:
    print(f"{c1} ^ {c2} se rovná {c2} ^ {c1}")
if c1 ** c2 != c2 ** c1:
    print(f"{c1} ^ {c2} se nerovná {c2} ^ {c1}")

email = "jmeno.prijmeni@seznam.google"

if "@" in email and " " not in email:  # zdali je v emailu @ a není mezera
    x = email.split("@")
    if len(x) == 2 and "." in x[1]: # zdali je v emailu pouze 1 @ a v doméně je tečka. 
        y = x[1].split(".")
        if len(y[-1]) >= 2: # zdali je koncovka domény delší než 2 znaky
            print("email je správný")
        
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

if re.fullmatch(regex,email):
    print(f"VALID {email}")

num = -1

if num >= 0:
    if num == 0:
        print("NULA")
    else:
        print("kladné číslo")
elif num <= 0: 
    print("záporné číslo")

a = 10
b = 6
c = 10

if a > b:
    if a > c:
        print(f"{a} je největší")
    elif c > a:
        print(f"{c} je největší")
    else:
        print(f"{c} i {a} jsou největší")
elif b > a:
    if b > c:
        print(f"{b} je největší")
    elif c > b:
        print(f"{c} je největší")
    else:
        print(f"{c} i {b} jsou největší")
else:
    if c > b:
        print(f"{c} je největší")
    elif a > c:
        print(f"{a} i {b} jsou největší")
    else:
        print("Všechny jsou stejný")



