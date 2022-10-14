import time


def f(x):
    print(x)
    if x < 10:
        x+=1
        f(x)
    else:
        print("hotovo")

f(6)

now = time.perf_counter()

def factorial_recursion(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*factorial_recursion(n-1)

print(factorial_recursion(5))

print(time.perf_counter()-now)


now = time.perf_counter()
num = 5

factorial = 1


for i in range(1,num + 1):
   factorial = factorial*i
print("The factorial of",num,"is",factorial)

print(time.perf_counter()-now)

def fibb_recur(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibb_recur(n-1) + fibb_recur(n-2)

print(fibb_recur(10))

# Vytvořte za pomocí rekurzivní funkce sčítání.
# Příklad:
# Zadám číslo 10 -> 10+9+8+7+6+5+4+3+2+1

# Zadám číslo 10 -> 1/10 + 1/9 + 1/8

# sum = 1/6 + 1/5 + 1/4 + 1/3 + 1/2 + 1
def harmonic_sum(n): #6
    if n < 2:
        return 1
    else:
        return 1/n + harmonic_sum(n-1)

# return = 10+9+8+7+6+5+4+3+2+1

def recursive_sum(n):
    if n < 2:
        return 1
    else:
        return n + recursive_sum(n-1)

print(recursive_sum(20))

# rows = 4
def pascalTriangle(row):
    if row == 0:
        return []
    elif row == 1:
        return [1]
    else:
        next_row = [1]
        prev_row = pascalTriangle(row-1) # [1,2,1]
        for i in range(0, len(prev_row)-1):
            next_row.append(prev_row[i]+prev_row[i+1]) # next_row = [1,3,3]
        next_row += [1] # next_row = [1,3,3,1]
    return next_row

def printTriangle(rows):
    for i in range(1,rows):
        print(pascalTriangle(i))

printTriangle(10)