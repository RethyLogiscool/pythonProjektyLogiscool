import random 
word = random.choice(["logiscool","auto","lednice"])
guessed = []
tips = 0
bads = 0
maxBads = 10
def generateGuessed(word, guessed):
    guessedPrint = ""
    done = False
    for pismeno in word:
        if pismeno in guessed:
            guessedPrint += pismeno
        else:
            guessedPrint += "_"
    if guessedPrint == word:
        done = True
    return guessedPrint, done
print("Vítej ve hře Hangman")
while True:
    genGuess = generateGuessed(word,guessed)
    if genGuess[1]:
        print(f"Hurá, vyhrál jsi! \n Hádané slovo bylo: {genGuess[0]} \n Měl jsi {bads} chyb a slovo jsi uhádl na {tips} pokusů")
        break
    else: 
        print(f"Hádané slovo: {genGuess[0]} \n Máš {maxBads-bads} pokusů")
    tip = input("Tipni si píseno: \n")
    if tip in word:
        print("Ano! Trefil ses")
        tips += 1
        guessed.append(tip)
    else:
        bads += 1
        if bads >= maxBads:
            print("Bohužel jsi vyčerpal pokusy, třeba příště")
            break
        else:
            print("Bohužel, zkus to znovu")

