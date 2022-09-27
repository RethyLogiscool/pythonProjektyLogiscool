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

# Tady vypíšu otázky
print("Jaké je hlavní město České republiky?")

# Tady zjistí odpověď
odpoved = input("a) Brno\nb) Plzeň\nc) Praha\n")

# Tady ověřím odpověď 
if(odpoved.upper()=="C"):
    print("Tvá odpověď je správná".upper()) # Správná odpověď
else:
    print("Tvá odpověď je špatná".lower()) # Špatné odpověď