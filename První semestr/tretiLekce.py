jmeno = 1
print("Moje jmeno je: " + str(jmeno))
print("Moje jméno je: %s" % (jmeno))
print("Moje jméno je: {0}".format(jmeno))
print("Moje jméno je: {jmeno}".format(jmeno=jmeno))

vek = 50
print("Můj věk je: " + str(vek))
print("Můj věk je: %i" % vek)
print("Můj věk je: {0}".format(vek))
print("Můj věk je: {vek}".format(vek=vek))



pocet = 15092049124
zvire = ""
jeZvire = True
hraBezi = False

if pocet:
    print("Pocet je definovan")
else:
    print("Pocet neni definovan")
if zvire:
    print("Zvire je definovano")
else:
    print("Zvire neni definovano")
if jeZvire:
    print("Je zvire")
else:
    print("Neni zvire")
if hraBezi:
    print("Hra bezi")
else:
    print("Hra nebezi")

cislo1 = 8
cislo2 = 10
try:
    if cislo1 > cislo2:
        print("Cislo 1 je větší")
    elif cislo1 < cislo2:
        print("Cislo 2 je větší")
    elif cislo1 == cislo2:
        print("Cisla jsou stejná")
except NameError:
    print("Error: Promena neni definovana")
except:
    print("Error")
else:
    print("Hotovo")

while True:
    try:
        a1 = "password123+"
        a2 = str(input("Zadej heslo: \n"))
    except:
        print("Heslo není ve správném formátu")
        continue
    else:
        if a1 == a2:
            print("Heslo je správné")
            break
        else:
            print("Heslo není správné, zkus to znovu")
            continue

print("____")
print("Jsi přihlášen!")

body = input("Kolik jsi dostal bodů? \n")
body = int(body)
grade = "F"

if body > 90:
    grade = "A"
elif body > 80:
    grade = "B"
elif body > 70:
    grade = "C"
elif body > 60:
    grade = "D"
elif body > 50:
    grade = "E"
else:
    grade = "F"


print("Dostal jsi známku " + grade)




