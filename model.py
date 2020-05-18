import random

ZACETEK = 'Z'

STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'
ZMAGA = 'W'
PORAZ = 'X'

bazen_besed =[]

with open('vislice/besede.txt') as datoteka_bazena:
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






class Vislice:
    '''
    skrbi za trenutno stanje več iger (imel bo več objektov tipa iger)
    '''
    def __init__(self,):
        # slovar, ki ID-ju  pririredi objekt njegove igre
        self.igre = {}   #    int -> (Igra, stanje)
        
    def prosti_od_igre(self):
        '''Vrne nek ID, ki ga ne uporablja nobena igra'''
        if len(self.igre) == 0:
            return 0
        else:
            return max(self.igre.keys()) + 1
            
    def nova_igra(self):

        # dobimo svež ID
        nov_id = self.prosti_id_igre()
        # naredimo navo igro 
        sveza_igra = nova_igra()
        # vse to shranimo v self.igre
        self.igre[nov_id] = (sveza_igra, ZACETEK)

        # Vrnemo nov ID
        return nov_id
        pass
        
    def ugibaj(self, id_igre, crka):
        # Dobimo staro igro ven
        trenutna_igra, _ = self.igra(id_igre)

        #ugibamo crko, dobimo novostanje
        novo_stanje = trenutna_igra.ugibaj(crka)

        #zapišemo posodobljeno stanje in igro nazaj
        self.igre([id_igre])


