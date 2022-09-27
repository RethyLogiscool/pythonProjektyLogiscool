jmeno = 666
#Moje jméno je: Ondřej

print("Moje jméno je: " + str(jmeno))
print("Moje jméno je: {0}".format(jmeno))
print("Moje jméno je: %s" % jmeno)
print("Moje jméno je: {jmeno}".format(jmeno=jmeno))

vek = 50.24
print("Můj věk je: %i a %f" % (vek,vek))



pocet = 150125
zvire = "AHoj"
jeZvire = True
hraBezi = False

if pocet:
    print("Pocet je definovat")
else:
    print("Pocet není definován")
if zvire:
    print("Zvire je definovano")
else:
    print("Zvire není definováno")
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
        print("Cislo 1 je menší")
    elif cislo1 == cislo2:
        print("Cisla jsou stejna")
except NameError:
    print("Error: Promena neni definovana")
except:
    print("Error")
else:
    print("Hotovo")

while True:
    try:
        dbPass = "password123+"
        userPass = str(input("Zadej heslo: "))
    except:
        print("Heslo není ve správném formátu")
        continue
    else:
        if dbPass == userPass:
            print("Heslo je správné")
            break
        else:
            print("Heslo není správné, zkus to znovu")
            continue

print("_____")
print("Jsi přihlášen")
grade = "F"

while True:
    try:
        body = input("Kolik jsi dostal bodů? \n")
        body = int(body)
    except:
        print("Nezadal jsi číslo")
        continue
    else:
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
        print("Dostal jsi " + grade)
        break
    