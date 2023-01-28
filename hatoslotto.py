"""A huzott.txt forrásállomány, hatos lottó hűzások adatait tartalmazza, a feladatok megoldása során ezeket az adatokat használja!
A huzott.txt állomány szerkezete:
·         id (azonosító): pl: 1
·         huzasid (húzási azonosító): pl.: 44
·         szam (kihúzott szám): pl.: 21
Az állomány első sora a mezőneveket tartalmazza kukac jellel elválasztva.
A megoldás mintája:
III/A, B:
            	A húzások száma: 6780
III/C:
            	A 42 héten húzott számok átlag: 23,13
III/D:
            	A legnagyobb kihúzott szám értéke: 45, a 74. héten húzták ki, ez volt a 129. húzás.
A.	Olvassa be osztály segítségével (utóbbit hozza létre külön modulban) a huzott.txt fájlból a játékosok adatait, és tárolja el összetett adatszerkezetben, ami elősegíti a további feladatok könnyű megoldását! Ügyeljen arra, hogy az állomány első sora az adatok fejlécét tartalmazza! (7p)
B.	Írassa ki a húzások számát a mintának megfelelően a konzolra! (2p)
C.	Határozza meg és írassa ki a konzolra a minta szerint, hogy a 42 héten (huzasid) húzott számoknak mennyi az átlaga, két tizedesjegyre kerekítve. (4p)
D.	Írassa ki konzolra a mintának megfelelően a legnagyobb kihúzott szám adatait (ha több is van, akkor az első legnagyobb adatait).(4p)

"""
from Hatoslottoclass import Hatoslotto
huzasok_lista=[]
def beolvas():
    fajlom=open("huzasok.txt","r",encoding="utf-8")
    fajlom.readline()
    fajltartalom=fajlom.readlines()
    #print(fajltartalom)
    i=0
    while i< len(fajltartalom):
        sor=fajltartalom[i].strip().split("@")
        huzasok_lista.append(Hatoslotto(sor))
        i+=1
    print(f" A húzások száma: {len(fajltartalom)}")
def negyvenkettedikhet():
    i=0
    ossz=0
    db=0
    while i<len(huzasok_lista):
        if huzasok_lista[i].het==42:
            ossz+=huzasok_lista[i].szam
            db+=1
        i+=1
    print(f"A 42 héten húzott számok átlag: {(ossz/db):.2f}")
def legnagyobbszam():
    i=0
    legnagyobb=0
    while i<len(huzasok_lista):
        if huzasok_lista[legnagyobb].szam < huzasok_lista[i].szam:
           legnagyobb=i
        i+=1
    print(f"A legnagyobb szám értéke: {huzasok_lista[legnagyobb].szam},ez volt a {huzasok_lista[legnagyobb].huzas}.húzás ")


