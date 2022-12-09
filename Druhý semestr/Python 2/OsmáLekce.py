import datetime as dt
import pendulum as p

schedule = [
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],
    ["SLEEP","SLEEP","SLEEP","SLEEP","SLEEP","SLEEP","SLEEP","SLEEP","ANG","ČJL","MAT","TEV","TEV","PRG","LUNCH","FREE","FREE","FREE","FREE","FREE","FREE","FREE","SLEEP","SLEEP"],
    ["SLEEP","SLEEP","SLEEP","SLEEP","SLEEP","SLEEP","SLEEP","SLEEP","ANG","ČJL","MAT","TEV","TEV","PRG","LUNCH","FREE","FREE","FREE","FREE","FREE","FREE","FREE","SLEEP","SLEEP"],
    ["SLEEP","SLEEP","SLEEP","SLEEP","SLEEP","SLEEP","SLEEP","SLEEP","ANG","ČJL","MAT","TEV","TEV","PRG","LUNCH","FREE","FREE","FREE","Python II","Python II","FREE","FREE","SLEEP","SLEEP"],
    ["SLEEP","SLEEP","SLEEP","SLEEP","SLEEP","SLEEP","SLEEP","SLEEP","ANG","ČJL","MAT","TEV","TEV","PRG","LUNCH","FREE","FREE","FREE","FREE","FREE","FREE","FREE","SLEEP","SLEEP"],
    ["SLEEP","SLEEP","SLEEP","SLEEP","SLEEP","SLEEP","SLEEP","SLEEP","ANG","ČJL","MAT","TEV","TEV","PRG","LUNCH","FREE","FREE","FREE","FREE","FREE","FREE","FREE","SLEEP","SLEEP"],
    ["SLEEP","SLEEP","SLEEP","SLEEP","SLEEP","SLEEP","SLEEP","SLEEP","ANG","ČJL","MAT","TEV","TEV","PRG","LUNCH","FREE","FREE","FREE","FREE","FREE","FREE","FREE","SLEEP","SLEEP"],
    ["SLEEP","SLEEP","SLEEP","SLEEP","SLEEP","SLEEP","SLEEP","SLEEP","ANG","ČJL","MAT","TEV","TEV","PRG","LUNCH","FREE","FREE","FREE","FREE","FREE","FREE","FREE","SLEEP","SLEEP"],
]

"""for line in schedule:    
    print('\t'.join(map(str, line)))"""

now = dt.datetime.now()

day = now.isoweekday()
hod = now.hour
minu = now.minute

def getCurrentTask(schedule,time,correction=0):
    day = time.isoweekday()
    hod = time.hour
    minu = time.minute

    return schedule[day][hod+correction],60-minu


curTask = getCurrentTask(schedule,now)[0]

if curTask == "FREE":
    curTask = "osobní volno"

nextTask = getCurrentTask(schedule,now,+1)[0]

if nextTask == "FREE":
    nextTask = "osobní volno"

minLeft = getCurrentTask(schedule,now)[1]

print(f"Nyní máš {curTask}, za {minLeft} minut máš {nextTask}")



print(f"Nyní máš {'osobní volno' if getCurrentTask(schedule,now)[0] == 'FREE' else getCurrentTask(schedule,now)[0]}, následuje {'osobní volno' if getCurrentTask(schedule,now,+1)[0] == 'FREE' else getCurrentTask(schedule,now,+1)[0]} za {getCurrentTask(schedule,now,+1)[1]} minut.")


list = ["AHOJ","JAK","SE","MÁŠ"]

print(list[1:3])