import random

#lista létrehozása
szamok = []

# Lista feltöltése 100 db random kétjegyű egész számokkal
for i in range(100):
    szam=random.randint(10,99)
    szamok.append(szam)
    
#Ellenőrzés
print(szamok)

#EGYSZÁM JÁTÉK

jatek_szam = 0
nem_talaldDB = 0

kitalalando_szam = szamok[random.randint(0, len(szamok))]

# A JÁTÉK ------------------------------------------

jatszol = True

while(jatszol):
    tipp = int(input("Tipped?: (egész szám): "))

    while(tipp != kitalalando_szam):
        tipp = int(input("Tipped?: (egész szám): "))
   
    print("Kitalatad a kitalalando szamt!")

    folytatas = input("Akarsz-e még jatszani? [I/N]")
    if(folytatas == "N"):
        jatszol = False
        



""" tipp = int(input("Tipped?: (egész szám): "))

while(tipp != kitalalando_szam):
    tipp = int(input("Tipped?: (egész szám): "))
   
print("Kitalatad a kitalalando szamt!")

folytatás = input("Akarsz-e még jatszani? [I/N]")

if(folytatás == "I"):
    #??????
    pass
else:
    exit() """


