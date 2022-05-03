puzzle = "computer science"
my_solution = "________ _______"
life = 10
correct_letters = []
incorrect_letters = []


while life > 0 and puzzle != my_solution:
    print(my_solution)
    tip = input("Tipni si písmeno:\n")
    if len(tip) == len(puzzle):
        temp = my_solution
        my_solution = tip
        print("Snažíš se uhodnout celé slovo... a tvůj tip je...")
        if my_solution == puzzle:
            print("Správně.")
        else:
            print("Špatně!")
            life -= 1
            print("Tohle není správné řešení. Zbývá ti {0} životů.".format(life))
            my_solution = temp
    else:
        found_something = False
        for i in range(len(puzzle)):
            if puzzle[i] == tip:
                my_solution_list = list(my_solution)
                my_solution_list[i] = tip
                my_solution = "".join(my_solution_list)
                found_something = True
        if not found_something:
            incorrect_letters.append(tip)
            life-=1
            print("Neuhodl jsi. Zbývá ti {0} životů.".format(life))
        else: 
            correct_letters.append(tip)
        print("List správných písmet: {0}".format(str(correct_letters)))
        print("List nesprávných písmet: {0}".format(str(incorrect_letters)))
if life > 0:
    print("Paráda, uhodl jsi to")
else:
    print("Sorry, třeba přítě.")
    
