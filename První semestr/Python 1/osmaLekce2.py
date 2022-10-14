puzzle = "computer science"
my_solution = ""
tips = []
round = 10
def formatSolution(tip=""):
    global puzzle
    global my_solution
    global tips
    global round
    re = 0
    if my_solution == "":
        word = puzzle
        re = 1
    else:
        word = my_solution
    tips.append(tip)
    my_solution = list(word)
    for i in range(len(word)):
        if puzzle[i] in tips:
            if puzzle[i] is tip: 
                my_solution[i] = tip
                re = 1
        elif(word[i]!=" "):
            my_solution[i] = "_"
    if re == 0:
        round -= 1
    my_solution = "".join(my_solution)
    print(my_solution)
    if round > 0:
        print(f"Zbývá ti {round} pokusů")
    if my_solution == puzzle:
        round = 0
        print("Vyhrál jsi")
    return re

print("Ahoj, vítej ve hře Hangman\nZkus uhádnout následující slovo")
formatSolution()
while(round > 0):
    formatSolution(input("Hádej: \n"))
