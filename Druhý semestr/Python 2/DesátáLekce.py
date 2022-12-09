from collections import namedtuple

prazdnej_tuple = ()
cisla = (1,2,3,4)
random = (1, "string", True, [1, 2, 3], cisla)
print(random)
print(prazdnej_tuple,cisla,random)

random[3][0] = 4

print(random)

uzivatel1 = ("uzivatel@domena.cz","Jméno","Příjmení",[[156, 192, 104],[8123,123123,2312]])

print(uzivatel1)

uzivatel1[-1][0] = tuple(uzivatel1[-1][0])

print(uzivatel1)

uzivatel1[-1][0] = list(uzivatel1[-1][0])

print(uzivatel1)

Zamestnanec = namedtuple("Zamestnance","jmeno oddeleni vyplata")

bob = Zamestnanec("Bob Novotný","IT oddělení",121000)
honza = Zamestnanec("Jan Dvořák","IT oddělení",96000)
pepa = Zamestnanec("Pepa Zelený","IT oddělení",158000)
eva = Zamestnanec("Eva Nováková","Účtárně",36000)

Zamestnanci = []

Zamestnanci.append(bob)
Zamestnanci.append(eva)
Zamestnanci.append(honza)
Zamestnanci.append(pepa)

for zam in Zamestnanci:
    if(zam.oddeleni == "IT oddělení"):
        print(zam.vyplata)

print(type(Zamestnanec))

class Zamestnanec1:
    def __init__(self,name,department,salary):
        self.name = name
        self.deparment = department
        self.salary = salary

    def getSalary(self):
        return self.salary
    
    def getSalaryAfterTax(self):
        return self.salary*0.85

    def pozdrav(self):
        return f"Ahoj, já jsem {self.name} a pracuji v {self.deparment}, beru {self.salary} Kč"
    

josef = Zamestnanec1("Josef Novotný","IT Oddělení",127000)

print(josef.getSalary())


cisla = (1,1,1,2,2,2,3,3,3,2,2,2,1,1,1)

print(cisla.index(2))

jmeno, oddeleni, vyplata = bob

print(vyplata)

cords = (172,112,-12)

x,y,z = cords

print(x)
print(y)
print(z)

a = (3,1)
b = (4,0)
c = (8,1)
d = (7,4)

def konvexCtyr(a,b,c,d):
    ret = False
    if(d[1]>a[1] and d[1]>c[1]):
        ret = True
    if(b[1]<a[1] and b[1]<c[1]):
        ret = True
    else:
        ret = False
    return ret

print(konvexCtyr(a,b,c,d))


def ccw(a,b,c):
    return (c[1]-a[1])*(b[0]-a[0]) > (b[1]-a[1])*(c[0]-a[0])

def jeprusecik(a,b,c,d):
    return ccw(a,c,d) != ccw(b,c,d) and ccw(a,b,c) != ccw(a,b,d)

print(jeprusecik(a,c,d,b))



