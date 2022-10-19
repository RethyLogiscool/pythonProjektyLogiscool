from cgi import test
from operator import contains
import random
import math


def nextSquare():
    k = 1
    while True:
        yield k * k
        k += 1

for num in nextSquare():
    if num > 100:
        break
    print(num)


db = ["jarda","tomas","honza","martin"]

def fetchUsers(db):
    userId = 0
    while userId < db.__len__():
        yield db[userId]
        userId += 1

def fetchUsers2(db):
    for user in db:
        yield user

for user in fetchUsers(db):
    print(user)


def printEven(list):
    for i in list:
        if i % 2 == 0:
            yield i

testList = []
while len(testList) < 20:
    value = random.randint(1,100)
    if not testList.__contains__(value):
        testList.append(value)

print(f"Originální list je {testList}")
print("Sudá čísla z listu jsou: ", end=" ")
for num in printEven(testList):
    print(num, end=", ")
print("\n")


prices = [9.50, 26.76, 89.99, 12.99, 649.99,999.99]
items = ["Led Strip", "Wifi extender", "Mini projector", "Socks", "laptop","iphone"]
basket = []
item_price = []

db = list(zip(items,prices))
print(db)

def buyItems(howMany,db):
    for i in range(howMany):
        rand = random.randint(0, items.__len__() - 1)
        yield db[rand][0],db[rand][1]

for item, price in buyItems(3,db):
    basket.append(item)
    item_price.append(price)
    print(f"Položka {item} ze {price} $")

## TŘI FUNKCE
# 1) Spočítat cenu VŠECH produktů
# 2) Najít NEJDRAŽŠÍ položku
# 3) Najít NEJLEVNĚJŠÍ položku

def totalPrice(list):
    x = 0
    for item in list:
        x += item
    return x

def maxPrice(list):
    x = 0
    for item in list:
        if item > x:
            x = item
    return x

def minPrice(list):
    x = math.inf
    for item in list:
        if item < x:
            x = item
    return x

print(minPrice(prices))
print(maxPrice(prices))
print(totalPrice(prices))