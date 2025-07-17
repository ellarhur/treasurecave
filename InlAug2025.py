# Svarsfil till inlämningsuppgiften i Grundläggande programmering i Python augusti
2025.

# Denna rad används för att namnge CSV-filen i koden. Använd sedan variabeln "filnamn" när du skapar din kod.
filnamn ='skattresultat.csv'

# Skriv din kod här:

import random
import csv
import os

# Introduktion till spelet
print("Välkommen till Templets Tio Dörrar!")
print("Enligt sägnen finns här en enorm skatt gömd, men ingen vet exakt var. Templet består av ett hemligt kammarsystem med tio massiva dörrar – och bakom endast en av dem vilar skatten.")
print("Men här är haken: För varje fel dörr du öppnar, halveras skatten.")
print("Skattens värde krymper alltså för varje gång du chansar fel.")
print("Lycka till!\n")

# Startmenyn
startmessage = "Välj ett alternativ (1-4):"

def startmenu():
    while True:
        print("SPELETS STARTMENY")
        print("1. Spela Skattjakten")
        print("2. Visa topplistan")
        print("3. Visa ett diagram över tidigare resultat")
        print("4. Avsluta spelet")

        print(startmessage)
        choice = input()
        if choice == '1':
            play()
        elif choice == '2':
            chart()
        elif choice == '3':
            diagram()
        elif choice == '4':
            print("Spelet är avslutat, tack för att du spelade - se resultatet i csv-filen!")
            break
        else: print(startmessage)

# Själva spelet, hur det är uppbyggt
def play():
    treasuredoor = random.randint(1,10)
    treasurevalue = 10000
    tries = 0
    openeddoors = []
    print("Spelet är startat. Du står just nu i templet framför de tio dörrarna. Skatten är värd 10 000 kr. Den halveras varje gång du väljer fel dörr.")
    
    while True:
        try:
         choice = int(input( "Skriv ett tal mellan 1-10 för att välja att öppna dörren med det numret."))
        except ValueError:
            print("Ogiltigt val, skriv ett heltal mellan 1 och 10.")
            continue
        
        if choice < 1 or choice > 10:
            print("Ogiltigt val, skriv ett heltal mellan 1 och 10.")
            continue
            
        if choice in openeddoors:
            print("Du har redan öppnat den dörren! Välj en annan dörr.")
            continue
        else:
            openeddoors.append(choice)
        if choice != treasuredoor:
            tries += 1
            treasurevalue = treasurevalue /2
            print("Du valde tyvärr fel dörr. Skatten är nu värd", treasurevalue, "kr. Välj en ny dörr!")
        if choice == treasuredoor:
            print("Grattis, du har hittat skatten när den var värd", treasurevalue, "kr, efter", tries, "gånger!")
            name = input("Ange ditt namn för topplistan: ")
            save_to_file(name, tries)
            break


def save_to_file(name, tries):
    createfile = not os.path.exists(filnamn)
    with open(filnamn, mode='a', newline='') as fil:
        printer = csv.writer(fil)
        if createfile:
            printer.writerow(["Namn", "Försök"])
        printer.writerow([name, tries])

def chart():
    print("Topplistan kommer här...")

def diagram():
    try:
        with open(filnamn, 'r') as fil:
            reader = csv.reader(fil)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("Ingen data finns att visa ännu. Spela först för att skapa data!")


startmenu()
