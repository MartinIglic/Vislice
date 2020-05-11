import random


STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'
ZMAGA = 'W'
PORAZ = 'X'

bazen_besed =[]

with open('vislive/besede.txt') as datoteka_bazena:
    for beseda in datoteka_bazena:
        bazen_besed.append(beseda.strip().lower())
class igra:

    

    def __init__(self, geslo, crke=None):
        self.geslo = geslo
        if crke is None:
            self.crke = []
        else:
            self.crke = crke.lower


    def napacne_crke(self):
        napacne = []
        for crka in self.crke:
            if crka not in geslo:
                napacne.append(crka)
        return napacne

    def pravilne_crke(self,):
        pravilne = []
        for crka in self.crke:
            if crka in self.geslo:
                pravilne.append(crka)
        return pravilne

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        for c in self.geslo:
            if c not in self.crke:
                return False
        return True

    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK

    def nepravilni_ugibi(self):
        return ' ',join(self.napacne_crke())


    def pravilni_del_gesla(self):
        trenutno = ''
        for crka in self.geslo:
            if crka in self.crka:
                trenutno += crka
            else:
                trenutno += '_'
        return trenutno

    
    def ugibaj(self, ugibana_crka):
        ugibana_crka = ugibana_crka.lower()

        if ugibana_crka in self.crke:
            return PONOVLJENA_CRKA
        
        self.crke.append(ugibana_crka)

        if ugibana_crka in self.geslo:
            if self.zmaga():
                return ZMAGA
            else:
                if self.poraz():
                    return PORAZ
                else: 
                    NAPACNA_CRKA
            

    def nova_igra(self):
        nakljucna_beseda = random.choice(bazen_besed)
        return Igra(nakljucna_beseda)



        PRAVILNA_CRKA, NAPACNA_CRKA, ZMAGA, PORAZ





        pass







    


