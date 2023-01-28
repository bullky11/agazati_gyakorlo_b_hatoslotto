"""
I/A, B:
Hét napja: Hétfő
Óra neve: Programozás alapjai
Értékelés (1-5): 5

I/C:
Köszönjük az értékelést!

A.	Kérje be az alábbi adatokat a fenti mintának megfelelően:
hét napja, óra neve és értékelés!  (2p)
B.	A program az adatbekérés után írja ki, ha az értékelés nem a megfelelő határokon belül lett megadva ( [1,5], zárt intervallum értendő):
Amennyiben negatív számot adott meg:
“Az értékelés nem lehet negatív!”,
Amennyiben 5 feletti egész számot adott meg:
“5 pont feletti értékelés nem elfogadható!”
Helyes pont-adat esetén:
“Köszönjük az értékelést!”
Feltételezzük, hogy csak egész számokat adnak meg. (4p)
C.	A mintának megfelelően írassa ki az eredményt! (1p)

"""
def beker():
    nap=input("Hát Napja: ")
    ora_nev=input("Óra Neve: ")
    osztalyzat=int(input("Értékelés (1-5): "))
    i=0
    while osztalyzat not in range(1,5):
        if osztalyzat < 0:
            osztalyzat =int(input("Az értékelés nem lehet negatív!"))
        elif osztalyzat==0:
            osztalyzat =int(input("Az értékelés nem lehet 0 "))
        elif osztalyzat >5:
            osztalyzat = int(input("5 pont feletti értékelés nem elfogadható!"))
    print("Köszönjük az értékelést!")
