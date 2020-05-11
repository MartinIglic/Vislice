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
            self.crke = crke


    def napacne_crke(self):
        napacne = []
        for crka in crke:
            if crka not in geslo:
                napacne.append(crka)
        return napacne

    def pravilne_crke(self):
        pravilne = []
        for crka in crke:
            if crka in geslo:
                pravilne.append(crka)
        return pravilne

    def stevilo_napak(self):
        return len(napacne_crke(geslo, crke))

    def zmaga(geslo):

