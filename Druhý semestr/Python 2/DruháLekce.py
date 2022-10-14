def f(a):
    print(a)
    if a < 10:
        a +=1
    else:
        print("hotovo")
        return
    f(a)

def factorial_recursive(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*factorial_recursive(n-1)

def fibonacci_recursive(m):
    if m == 0:
        return 0
    elif m == 1:
        return 1
    else:
        return fibonacci_recursive(m-1) + fibonacci_recursive(m-2)

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

# return = 1+2+3+4+5+6+7+8+9+10