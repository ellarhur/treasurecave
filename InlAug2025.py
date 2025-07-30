# Svarsfil till inlämningsuppgiften i Grundläggande programmering i Python augusti
2025.

# Denna rad används för att namnge CSV-filen i koden. Använd sedan variabeln "filnamn" när du skapar din kod.
filnamn ='skattresultat.csv'

# Skriv din kod här: 

filnamn = 'skattresultat.csv'

import random
import csv
import matplotlib.pyplot as plt

# Text som introducerar spelets koncept och regler
print("*" * 30)
print("Välkommen till Templets Tio Dörrar!")
print("Du befinner dig i en grotta långt under jordens yta. Enligt sägnen finns här en enorm skatt gömd, men ingen vet var.")
print("Du står framför tio dörrar, numrerade 1-10. Öppna en i taget för att hitta skatten.")
print("Men här är haken: För varje dörr du öppnar som är fel, halveras skatten.")
print("Skattens värde krymper alltså när du gissar fel. Just nu är skatten värd 10 000 SEK.")
print("Lycka till!")
print("*" * 30)


#Spelmeny
startmessage = "Välj ett alternativ (1-4):"

def startmenu():
    while True:
        print("SPELETS STARTMENY")
        print("1. Spela Skattjakten")
        print("2. Visa topplistan")
        print("3. Visa ett diagram över tidigare resultat")
        print("4. Avsluta spelet")
        print("*" * 30)

        print(startmessage)
        choice = input()
        if choice == '1':
            play()
        elif choice == '2':
            chart()
        elif choice == '3':
            diagram()
        elif choice == '4':
            print("Du har valt att avsluta spelet, men tack för att du spelade!")
            break
        else: print(startmessage)

# Om användaren väljer att starta spelet

def play():
    treasuredoor = random.randint(1,10)
    treasurevalue = 10000
    försök = 0
    openeddoors = []
    print("Spelet är startat, du står just nu i templet framför de tio dörrarna. Skatten är värd 10 000 SEK. Välj din första dörr genom att skriva ett tal mellan 1-10.")

    while True:
        try:
            choice = int(input())
            if choice < 1 or choice > 10:                   
                print("Välj ett heltal mellan 1-10, inte högre eller lägre. Välj en ny dörr!")
                continue

            if choice in openeddoors: 
                print("Du har redan valt den dörren, välj en annan dörr!")
                continue
                
        except ValueError:
            print("Välj ett heltal mellan 1-10, inte något annat tecken. Välj en ny dörr!")
            continue
        
        openeddoors.append(choice)
        if choice != treasuredoor:
            försök += 1
            treasurevalue = treasurevalue / 2
            print("Du valde tyvärr fel dörr. Skatten är nu värd", treasurevalue, "SEK. Välj en ny dörr!")

        if choice == treasuredoor:
            print("Grattis, du har hittat skatten när den var värd", treasurevalue, "SEK, efter", försök, "försök!")
            namn = input("Ange ditt namn för att skrivas in på topplistan: ")
            spararesultat(namn, försök)
            break

# Spara namn och antal försök i CSV-filen
def spararesultat(namn, försök):
    try:
        with open(filnamn, 'r'):
            filen_finns = True
    except FileNotFoundError:
        filen_finns = False


    with open(filnamn, mode='a', newline='') as csv_fil:
        writer = csv.writer(csv_fil)
        if not filen_finns:
            writer.writerow(["Namn", "Försök"])
        writer.writerow([namn, försök])


# Öppnar CSV-filen vid menyval 2
def chart():
    try: 
        with open(filnamn, 'r') as csv_fil:
            reader = csv.reader(csv_fil)
            data = list(reader)

            if len(data) == 0:
                print("Det finns ännu ingen data att visa, spela först för att skapa data!")
                return

# F-sträng för att skriva ut rubriken snyggt åt höger
            print(f"{'Spelares namn:':} {'Antal försök:'}")
            print("*" * 30)

            for namn, försök in data:
                    print(f"{namn:} {försök}")
            print()

    except FileNotFoundError:
        print("Ingen data finns att visa ännu. Spela först för att skapa data!")

# Felmeddelande som gör min kod mindre upprepad
diagram_message = "Det finns ingen data ännu - spela först för att se diagrammet sen!"

# Hämtar informationen från CSV-filen så att diagrammet kan skapas
def kolla_csv_data():
    try:
        with open(filnamn, 'r') as csv_fil:
            reader = csv.reader(csv_fil)
            return list(reader)
    except FileNotFoundError:
        return diagram_message

# Öppnar diagrammet vid menyval 3
def diagram():
    data = kolla_csv_data()
    if data is None or len(data) <= 1:
        print(diagram_message)
        return

    resultat = data[1:]  # 1: hoppar över första raden, som är rubriken
    y = [0] * 10  # för försök 1–10

    for rad in resultat:
        try:
            försök = int(rad[1])
            if 1 <= försök <= 10:
                y[försök - 1] += 1
        except (IndexError, ValueError):
            continue

    x = list(range(1, 11)) # Listan måste vara 1-11 för i programmering är första värdet 0
    plt.bar(x, y)
    plt.title("Stapeldiagram över resultat")
    plt.xlabel("Antal försök (dörrar öppnade)")
    plt.ylabel("Antal spelare")
    plt.xticks(x)
    plt.show()

# Menyn som ska synas alltid förutom vid spelets start och slut
startmenu()