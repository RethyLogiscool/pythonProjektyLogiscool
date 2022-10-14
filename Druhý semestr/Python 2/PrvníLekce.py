def Pozdrav():
    print("Ahoj Světe")

Pozdrav()

def PozdravKrat(x: int):
    for i in range(x):
        Pozdrav()

PozdravKrat(105)

def jeToPrvocislo(cislo: int) -> bool:
    prvocislo = True
    for i in range(2,cislo):
        if cislo % i == 0:
            prvocislo = False
    return prvocislo

def jeToPrvocislo2(cislo: int) -> bool:
    for i in range(2,cislo):
        if cislo % i == 0:
            return False
    return True

print("Je prvočíslo? " + str(jeToPrvocislo2(12)))

#  a**2 + b**2 == c**2 NEBO c**2 + b**2 == a**2 NEBO a**2 + c**2 == b**2

def pravoUhlyTroj(a, c, b):
    if a**2 + b**2 == c**2:
        return True
    return False

print(pravoUhlyTroj(c=5,b=3,a=4))
print(pravoUhlyTroj(4,3,5))

def cislo():
    abrakadabra = 10
    x = 10
    print(x)

cislo()
x = 20
cislo()
print(x)

# VSTUP: 2 parametry!  1. spotřeba auta (třeba 7.8 l/100km)  2. délka cesty (třeba 650 km)
# VÝSTUP: počet litrů

# X = (7.8/100)*650  => 50,7 l

def kolikLitru(spotreba, vzdalenost, cena):
    return spotreba/100*vzdalenost*cena

print("Kolik potřebuju peněz na cestu do chorvatska?")
print(kolikLitru(spotreba = 7.8,vzdalenost=650,cena=38.5))