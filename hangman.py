word = "logiscool"
guessed = False
letters = []
chances = 10
while not guessed:
    guess = str(input("Hádej písmeno ve slově: ")).lower()
    if guess in word:
        print("Správně! {0} je ve slově.".format(guess))
        letters.append(guess)
        temp = list(word)
        for i in range(len(temp)):
            for let in letters:
                if temp[i] not in letters:
                    temp[i] = "_"
        print("".join(temp))
        if "".join(temp) is word:
            guessed = True
    else:
        chances -= 1;
        print("Neuhodl jsi to, ztrácíš jeden pokus! Zbývá ti {0} pokusů.".format(chances))

