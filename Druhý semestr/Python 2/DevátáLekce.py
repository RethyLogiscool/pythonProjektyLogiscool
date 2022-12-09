print(1 + 1)
print(1 - 1)
print(2 ** 2)
print(10 % 2)

x = 0
y = 10
print(x < y and y % 2 == 0)

print(bin(14))
print(bin(6))
print(14 & 6)
print(bin(14 & 6))
print(14 | 6)
print(bin(14 | 6))
print(14 ^ 6)
print(bin(14 ^ 6))

"""

10101000101 = 1349
10101011000 = 1368

10101011101 OR

10101000000 AND

00000011101 XOR


"""
print(bin(1349))
print(bin(1368))
print("AND")
print(1349 & 1368)
print(bin(1349 & 1368))
print("OR")
print(1349 | 1368)
print(bin(1349 | 1368))
print("XOR")
print(1349 ^ 1368)
print(bin(1349 ^ 1368))

print(~3)

print(14 >> 2)
print(14 << 2)

"""
1100
11

1110
111000

"""


if 6 % 2 == 0:
    print("ANo")

if 6 & 1 == 0:
    print("taky ano") 
    # 110
    # 001 
    # 0 == 0

x = 2

x <<= 2

print(x)

def isPowerOfTwo(n):
    print(bin(n))
    print(bin(n-1))
    if n > 0 and (n & (n-1) == 0):
        return True
    else:
        return False

print(isPowerOfTwo(32))

"""

10000 - 1
01111


"""

print(bin(52))
print(oct(52))
print(hex(10))

print(128 + 0b11 + 0xf + 0o11)

print(0o274)

print(0xf)





    




