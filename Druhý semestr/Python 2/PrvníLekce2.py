def Pozdrav():
    print("Hello_world")

Pozdrav()

def PozdravKrat(x: int):
    for i in range(x):
        Pozdrav()

PozdravKrat(10)

# Vytvořit funkci
# VSTUP: celé číslo (int)
# VÝSTUP: True/False // jestli to bude nebo nebude prvočíslo

def jeToPrvocislo(cislo:int) -> bool:
    prvocislo = True
    for i in range(2,int((cislo/2)+1)):
        if cislo % i == 0:
            prvocislo = False
    return prvocislo


def jeToPrvocislo(cislo:int) -> bool:
    for i in range(2,int((cislo/2)+1)):
        if cislo % i == 0:
            return False
    return True

print(jeToPrvocislo(98689))

# Vytvořit funkci
# VSTUP: 3 strany (a,b,c)
# VÝSTUP: True/False // jestli to je pravoúhlý trojúhelník
# c**2 = a**2 + b**2

def jeToPravTroj(a,b,c):
    if (a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (c**2 + a**2 == b**2):
        return True
    return False

print(jeToPravTroj(3,4,5))

def jeToPravTroj(strana_a:float,strana_b:float, strana_c:float) -> bool:
    if strana_a**2 + strana_b**2 == strana_c**2:
        return True
    return False

print(jeToPravTroj(strana_a = 3, strana_b = 4, strana_c = 5))

def cislo():
    x = 10
    print(x)

cislo()
x = 20
cislo()
print(x)

# VSTUP: 2 parametry!  1. spotřeba auta (třeba 7.8 l/100km)  2. délka cesty (třeba 650 km)
# VÝSTUP: počet litrů
# BONUS: 3. parametr cena benzinu, 2 vystupy, počet litrů a cena

# X = (7.8/100)*650  => 50,7 l

def spotreba(spotreba, delka, cena) -> float:
    litry = spotreba/100 * delka
    cena = litry * cena
    return(litry, cena)
print(spotreba(spotreba=7.8, delka=650 , cena=42))