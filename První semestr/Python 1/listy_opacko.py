list = ["Honza","Adam","David"]

print(list[0])

list.append("Daniela")
list.append("František")
list.append("Bára")
list.append("Lucie")
list.append("Ahjj")

print(list)

list.insert(1,"Matěj")

print(list)

print(list[:2])

print(list[1:4])

print(list[3:])

print(list[-3:])

print(list[:3])

list[0],list[1] = list[1],list[0]

print(list)

for i in list:
    print(i)

print("___")

for i in list:
    if "a" in i.lower():
        print(i)

tabulka = (
    ("Honza", 10.1),
    ("Daniela", 10.3)
)

souradnice = [
    [10,15,8],
    [6,14,9]
]

uzivatele = [
    ("admin","admin@example.com","Heslo123+","+4207778238383"),
    ("admin","admin@example.com","Heslo123+",None),
    ("admin","admin@example.com","Heslo123+","+4207778238383"),
    ("admin","admin@example.com","Heslo123+","+4207778238383")
]

for jmeno, cas in tabulka:
    print(f"{jmeno} má čas {cas}s")

for x,y,z in souradnice:
    print(f"X={x}, Y={y}, Z={z}")

for jmeno, email, heslo, tel in uzivatele:
    print(f"Uživatel {jmeno} má email: {email}")


