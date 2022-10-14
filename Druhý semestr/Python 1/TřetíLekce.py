from symbol import except_clause

import math

jmeno = "Ondřej"
vek = 21
hodin = 12

print("Moje jmeno je: " + jmeno + ", můj věk je: " + str(vek))
print("Moje jmeno je: %s, můj věk je: %i" % (jmeno,vek))
print("Moje jmeno je: {0}, můj věk je: {1}".format(jmeno,vek))
print("Moje jmeno je: {jmeno}, můj věk je: {vek}".format(jmeno=jmeno, vek=vek))


jmeno, prijmeni, vek, adresu, telefon, email, vysku, vahu,titul = "Ondřej","Rethy",21,"Pražšká 181","777888777","info@domena.cz","181","87","Bc."

print("Ahoj, já jsem {8} {1} {0}, je mi {2} let a bydlím na adrese {3}. Můj telefon je {4}, email je {5}. Měřím {6} cm a vážím {7} kg".format(jmeno, prijmeni, vek, adresu, telefon, email, vysku, vahu, titul))

print("Ahoj, já jsem {titul} {pr} {jm}, je mi {vek} let a bydlím na adrese {adr}. Můj telefon je {tel}, email je {mail}. Měřím {h} cm a vážím {w} kg".format(titul=titul,jm=jmeno, pr=prijmeni, vek=vek, adr=adresu, tel=telefon, mail=email, h=vysku, w=vahu))

print("Ahoj, já jsem %s %s %s, je mi %i let" % (titul, prijmeni, jmeno, vek))

print("Teď je: " + str(hodin) + " hodin")
print("Teď je: %s hodin" % hodin)


cislo1, cislo2 = 2,1

try:
    if cislo1 > cislo2:
        print("Číslo 1 je větší")
    elif cislo1 < cislo2:
        print("Číslo 1 je menší")
    elif cislo1 == cislo2:
        print("Čísla jsou stejná")
except NameError:
    print("Chybí proměnná")
except TypeError:
    print("Máš chybu v typu proměnné")
except ValueError:
    print("Máš špatnou hodnotu")
except:
    print("Error")
else:
    print("Hotovo")

"""while True:
    try:
        dbPass = "password123+"
        userPass = str(input("Zadej heslo: "))
    except:
        print("Heslo není ve správném tvaru")
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

while True:
    try:
        body = input("Kolik jsi dostal bodů? \n")
        body = int(body)
    except:
        print("Nezadal jsi číslo")
        continue
    else:
        if body > 100:
            grade = "F"
        elif body > 90:
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
        break"""

game = True
vek = 21.1
ovoce = ["Banán","Jablko","Jahoda"]

print(type(vek))
print(type(jmeno))
print(type(game))
print(type(ovoce))

print(ovoce[2])

for ov in ovoce:
    print(ov)

studenti = ["Jakub","Martin","David"]

for student in studenti:
    print(student)

for i in range(studenti.__len__()):
    print(studenti[i])

for student in studenti:
    print(studenti[studenti.index(student)].upper())

for student in studenti:
    student = student.capitalize()
    print(student)

for student in studenti:
    student = student.replace("a","4")
    print(student)


pocetPater = 10

for i in range(1,pocetPater):
    print("*"*i)

for i in range(pocetPater):
    for j in range(i+1):
        print("*",end=" ")
    print("")

print("\033c")

for student in studenti:
    print(student)
