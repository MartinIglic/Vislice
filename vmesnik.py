import model


igra = model.nova_igra()

def izpis_poraza(igra):
    return f'IZGUBIL SI, pravilno geslo je bilo {igra.geslo}'


def izpis_zmaga(igra):
    return (f'ZMAGAL SI, geslo je bilo {igra.geslo}' + 
            'potreboval si {len(igra.napacne_crke())} ugibov')

def izpis_igre(igra):
    text = (
        f'Stanje gesla : {igra.pravlni_ugibi()} \n'
        f'Imaš še {model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak()} možnosti za napake.'
    )

    return text

def zahtevaj_vnos():
    return input('vpiši naslednjo črko:')

    print(izpis_poraza(trenutna_igra))


def šozeni_vmesnik():

    trenutna_igra = model.nova_igra()
    while True:
        #pokažemo stanje
        print(izpis_igre(trenutna_igra))

        crka = zahtevaj_vnos()

        trenutna_igra.ugibaj(crka)

        if trenutna_igra.zmaga():
            print(izpis_zmaga(trenutna_igra))
            break
        if trenutna_igra.poraz():
            print(izpis_poraza(trenutna_igra))
            break



    

    #naredimo novo igro

    #ponavljamo:
    #vnos
    # preveri zmago in poraz
    #nazaj na vnos
