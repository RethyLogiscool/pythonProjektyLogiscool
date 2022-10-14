import math
import random
import matplotlib.pyplot as plt

print(math.pi)
print(math.factorial(5))
print(math.degrees(math.cos(120)))
print(math.isnan(math.nan))


x = math.nan
y = math.nan

if(math.isnan(x) and math.isnan(y)):
    print("Žádný běžec nedoběhl do konce")
if(math.isnan(x) or math.isnan(y)):
    print("Někdo nedoběhl do konce")
if(not math.isnan(x) and not math.isnan(y)):
    print("Oba doběhli.")

print(random.randint(1,100))
print(random.seed(100))
print(random.randint(1,100))

plt.pie(x=[1,4,3,2,2,3],labels=["raz","dva","tři","čtyři","pět","šest"],autopct="%.1f%%")
plt.show()