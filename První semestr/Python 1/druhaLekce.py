#print("Jak se máš?".__len__())
#print(input("Jak se máš?").__len__())
#print(len("Ahoj"))
#splitString = "Dnes jsem měl k obědu svíčkovou.\nZítra si dám řízek.".split("\n")
#for string in splitString:
#    print(string.split(" "))

#print("Jak se máš?".count("J"))
#print("Jak se máš?".find("se"))

#print("Jak se máš?".startswith("Jak"))
#print("Jak se máš?".endswith('?'))

#print("Jak".isalpha())
#print("10".isdecimal())

firstName = "Jan"
lastName = "Novák"
age = 28
jobType = "Baker"
gender = "man"
country = "Czech Republic"
weight = 98.6
height = 180

print(firstName + " " + lastName)
print(firstName + str(weight))
print("Jméno je: %s, váha je %s" % (firstName,weight))
print("Jméno je: {jmeno}, váha je {vaha}".format(jmeno=firstName,vaha=weight))

print(type(weight))
print(type(height))
print(type(firstName))

print(float(height))
print(str(height))
print(int(weight))

print(height + weight)

if(weight>=100):
    print("Jez zdravěji")
else:
    print("Jsi ok")

for i in range(0,10):
    print(i)



fruits = ["Banán","Jablko","Jahoda","Pomeranč","Ananas"]

for fruit in fruits:
    print(fruit)

print("_______")

for i in range(0,fruits.__len__()):
    fruits[i]=fruits[i].upper()

for fruit in fruits:
    print(fruit)

for fruit in fruits:
    fruits[fruits.index(fruit)]=fruit.upper()


for fruit in fruits:
    print(fruit)



pocetPater = 10

for i in range(pocetPater):
    print("*"*i)

for i in range(pocetPater):
    for j in range(i+1):
        print("*",end=" ")
    print("")



for fruit in fruits:
    print(fruit)



print("\033c")