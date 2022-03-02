print("Jak se máš?".__len__())
print(len("Jak se máš?"))

splitString = "Dnes jsem měl k obědu svíčkovou.\nZítra si dám řízek.".split("\n")

for radek in splitString:
    print(radek.split(" "))

auta = ["Audi","Škoda","Lambo","Seat"]

for auto in auta:
    print(auto)

print("Jak se máš?".count("J"))
print("Jak se máš?".count("se"))
print("Jak se máš?".startswith("Jak"))
print("Jak se máš?".endswith("?"))

print(str(["Audi","Škoda","Lambo","Seat"]).count("o"))

firstName = "Jan"
lastName = "Novák"
age = 29
jobType = "Baker"
gender = "man"
country = "Czech Republic"
weight = 108.4
height = 180

print(firstName + " " + lastName)
print(firstName + str(weight))

print("Jměno je: {0}, váha je {1}.".format(firstName,weight))
print("Jměno je: {jmeno}, váha je {vaha}.".format(jmeno=firstName,vaha=weight))

print("Jméno je: %s, váha je %s." % (firstName,weight))

print(type(weight))
print(type(height))
print(type(firstName))

print(float(height))
print(str(height))
print(int(weight))

print(height - weight)

if weight>=100:
    print("Jez zdravěji")
else:
    print("Jsi ok")

for i in range(100):
    print(i)

user = [
    {
        "jméno" : "Ondřej",
        "Příjmení" : "Rethy"
    },
    {
        "jméno" : "Martin",
        "Příjmení" : "Novák"
    }
]

print(user[0])

users = {
    "email@jmeno.cz" : {
        "Jméno" : "Ondřej",
        "Příjmení" : "Rethy"
    } 
}

print(users["email@jmeno.cz"]["Jméno"])

uživatel1 = {
    "jméno" : "Jan"
}
uživatel1["příjmení"] = "Novák"

uživatel1.update({
    "datumNarozeni" : "10. 2. 1999",
    "věk" : 21,
    "země" : "česko"
})

print(uživatel1)


seznamOvoce = ["Banán","Jablko","Jahodu"]

seznamOvoce.append("Ananas")
seznamOvoce.insert(0,"Hrušku")

exotickeOvoce = ["Papája","Liči"]

seznamOvoce.extend(exotickeOvoce)

print(seznamOvoce)

for ovoce in seznamOvoce:
    seznamOvoce[seznamOvoce.index(ovoce)]=ovoce.upper()

print(seznamOvoce)

for i in range(len(seznamOvoce)):
    seznamOvoce[i]=seznamOvoce[i].upper()

print(seznamOvoce)











pocetPater = 10

for i in range(pocetPater):
    print("* "*i)

for i in range(pocetPater):
    for j in range(i+1):
        print("*",end=" ")
    print("")

