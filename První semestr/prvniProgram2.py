print("""
┌──────────────────────────────────────────────┐
│                                              │
│                    x                         │
│     xxxxxx         x        x    xxxxx       │
│     x     xxxx     x    x   x      xxx       │
│     x        xx    x    x   x    xx          │
│    xx         x    x    x   x   xx           │
│     x     x   x    x    x   x  xx x  xx      │
│      xx   xx x      xxxxx              xxx   │
│        xxxxxxx                               │
│              xx                              │
│                                              │
└──────────────────────────────────────────────┘
""")
print("Jaké je hlavní město České republiky?")
#moznosti = "a) Brno;b) Plzeň;c) Praha".split(";")
moznosti = ["a) Brno","b) Plzeň", "c) Praha"]
for moznost in moznosti:
    print(moznost.replace("o","0"))
odpoved = input("")
if(odpoved.lower() == "c"):
    print("Odpověď je správně")
else:
    print("Odpověď je špatně")