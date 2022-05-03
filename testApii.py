import requests

base_url = f"https://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt"
respon = requests.get(base_url)
resp = respon.content
procenta = 0.02
print(" __ ")
list = str(resp).replace(",", ".").split("\\n")
print("POČET | MĚNA | WE BUY | WE SELL")
for i in range(2,list.__len__()-1):
    line = list[i].split("|")
    print(line[2] + " | " + line[3] + " | " + str(round(float(line[4])*(1+procenta),2)) + "  |  " + str(round(float(line[4])*(1-procenta),2)))
