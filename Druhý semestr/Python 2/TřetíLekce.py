from curses import init_pair
import math
import random
import matplotlib.pyplot as plt

print(math.factorial(5))
print(math.pi)
print(math.degrees(math.cos(120)))
print(math.isnan(1))

x = 10
y = 12.5

if(math.isnan(x) and math.isnan(y)):
    print("Žádný běžec nedoběhl do konce")
if(math.isnan(x) or math.isnan(y)):
    print("Někdo nedoběhl do konce")
if(not math.isnan(x) and not math.isnan(y)):
    print("Oba doběhli")


print(random.randint(1,100))

def piechart(size, lab):
    plt.figure(projection='3d')
    plt.pie(size, labels=lab, autopct='%.2f%%')
    plt.show()

n = int(input("Kolik máš rád her?"))
games = []
likes = []
data = []
db = s = 0

for i in range(n):
    game_name = input("Dej mi název hry: ")
    like = int(input("Jak moc tuto hru máš rád?: "))
    db += like
    games.append(game_name)
    likes.append(like)
for i in range(n):
    s = likes[i] / db * 100
    s = round(s, 1)
    data.append(s)

piechart(likes,games)