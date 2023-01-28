class Hatoslotto:
    def __init__(self,sor):
        self.huzas=sor[0]
        self.ev=int(sor[1])
        self.het=int(sor[2])
        self.szam=int(sor[3])
    def __str__(self):
        return f"{self.huzas},{self.ev},{self.het},{self.szam}"