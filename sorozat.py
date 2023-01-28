"""
minta:
II/A, B, C:
           	20;28;124;166;15;188;174;243
II/D, E:
           	Tízzel osztható számok száma: 1.
kimutatas.txt tartalma:
II/F:
Tízzel osztható számok száma: 1.
A.	Írasson ki a konzolra pontosvessző jelel (;) elválasztva 8 számból álló véletlen számsorozatot [-100,859] zárt intervallumon a mintának megfelelően! (4p)
B.	A generált értékeket tárolja lista adatszerkezetben! (1p)
C.	A ; jel csak az értékek között szerepeljen (a végén, elején ne)! (2p)
D.	Írjon függvényt tizel_osztahatoak_szama néven, amiben számolja meg, hogy hány olyan elem van, ami tízzel osztható. A visszatérési érték legyen egy egész szám! (3p)
E.	A tizel_osztahatoak_szama függvény eredményét írassa ki a mintának megfelelően a konzolra, amit konzol_ir nevű metódusban fogalmazzon meg! (2p)
F.	A tizel_osztahatoak_szama függvény eredményét írassa ki a mintának megfelelően a vegeredmeny.txt nevű fájlba, amit fajlba_ir nevű metódusban fogalmazzon meg! (2p)

"""
import random

szamok_lista=[]
def generalt_szamok():
    i=0
    j=0

    while i<8:
        szamok_lista.append(random.randint(-100,859))
        i+=1
    print(';'.join(str(szamok) for szamok in szamok_lista))
def tizel_osztahatoak_szama():
    i=0
    db=0
    while i< len(szamok_lista):
        if szamok_lista[i]%10==0:
            db+=1
        i+=1
    return db
    konzol_ir(db)
def konzol_ir(db):
    print(f"Tízzel osztható számok száma: {db}")
    iras=open("vegeredmeny.txt","w",encoding="utf-8")
    iras.write(f"Tízzel osztható számok száma: {db}")
    iras.close()



