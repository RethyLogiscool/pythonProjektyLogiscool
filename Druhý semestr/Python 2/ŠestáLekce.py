import random
import matplotlib.pyplot as plt
import numpy as np

def taxCalc(incomes,sale):
    tax = 0.0
    for income in incomes:
        if income < 1867728:
            tax += income * 0.15
            if income < 0:
                tax = 0.0
        else:
            tax += 280159 + (income - 1867728)*0.23
    if tax <= sale:
        tax = 0.0
    else:
        tax -= sale
    return round(tax, 0)
    
incomes = []
for i in range(3):
    temp = []
    for i in range(12):
        temp.append(random.randint(60000,180000))
    incomes.append(temp)

for person in incomes:
    print(f"Zaplatit na dani: bez slevy {taxCalc(person,0)}, se slevou {taxCalc(person,30840)} Kč")



property = [[[random.randint(20,100) for room in range(5)] for floor in range(10)] for building in range(5)]

print(property)


for building in property:
    for floor in building:
        for room in floor:
            print(f"Cena pokoje č. {floor.index(room)} s výměrou {room} m2 v {building.index(floor)}. patře budovy č. {property.index(building)+1} je {room * 100000} Kč")


def cubePlot():
    axes = [5, 5, 5]
    data = np.ones(axes)
    print(data)
    alpha = 0.7
    colors = np.ones(axes + [4])
    print(colors)

    colors[0] = (1, 0, 0, alpha)  # red
    colors[1] = (0, 1, 0, alpha)  # green
    colors[2] = (0, 0, 1, alpha)  # blue
    colors[3] = (1, 1, 0, alpha)  # yellow
    colors[4] = (1, 1, 1, alpha)  # grey

    print(colors)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.voxels(data, facecolors=colors, edgecolors='gold')
    ax.set_title("Colorized Cube")
    plt.show()
cubePlot()
