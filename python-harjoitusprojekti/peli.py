import time
import questionary

from pelaaja import Pelaaja
from huone import Huone
from esine import Esine

from makuuhuone import makuuhuone
from keittio import keittio
from olohuone import olohuone
from eteinen import eteinen
from kylpyhuone import kylpyhuone


def kirjoita(teksti):
    for kirjain in teksti:
        print(kirjain, end="", flush=True)
        time.sleep(0.03)
    print()


kirjoita("Hei ja tervetuloa peliin!")
time.sleep(0.5)

kirjoita("Ennen kuin aloitamme, haluan tietää sinusta vähän.")
time.sleep(0.5)

print("")
nimi = input("Mikä sinun nimesi on? ")

print("")
ika = int(input("Kuinka vanha olet? "))


if ika < 12:
    print("")
    kirjoita("Voi ei, " + nimi + "!")
    time.sleep(0.5)
    kirjoita("Olet liian nuori pelaamaan.")
    time.sleep(0.5)
    kirjoita("Sinun pitää vielä kasvaa!")

else:
    makuuhuone_obj = Huone("Makuuhuone")
    keittio_obj = Huone("Keittiö")
    olohuone_obj = Huone("Olohuone")
    eteinen_obj = Huone("Eteinen")
    kylpyhuone_obj = Huone("Kylpyhuone")

    vihko = Esine("vihko", 0.3)
    kyna = Esine("kynä", 0.1)
    kannettava = Esine("kannettava", 2.0)
    omena = Esine("omena", 0.2)
    laukku = Esine("laukku", 0.5)
    avaimet = Esine("avaimet", 0.1)

    pelaaja = Pelaaja(nimi, makuuhuone_obj)

    print("")
    kirjoita("Tervetuloa, " + nimi + "!")
    time.sleep(1)

    print("")
    kirjoita("Heräät ja katsot kelloa...")
    time.sleep(1)

    kirjoita("Kello on 8.40.")
    time.sleep(1.5)

    print("")
    kirjoita("Voi ei...")
    time.sleep(1)

    kirjoita("Olet nukkunut liian pitkään.")
    kirjoita("Olet myöhästymässä koulusta.")
    time.sleep(1)

    print("")
    kirjoita("Ja tietenkin juuri tänään on uusintakoe.")
    time.sleep(1)

    kirjoita("Jos et pääse ajoissa paikalle, olet pulassa.")
    time.sleep(1)

    print("")
    kirjoita("Sinun pitää valmistautua nopeasti,")
    kirjoita("pakata opiskelutavarat ja lähteä kouluun!")
    time.sleep(1)

    print("")
    kirjoita("Ja vielä yksi pieni ongelma...")
    time.sleep(1.5)

    kirjoita("Et löydä avaimiasi.")
    time.sleep(1.5)

    print("")
    kirjoita("Etsi avaimet, pakkaa tavarasi ja lähde kouluun!")
    time.sleep(1)

    makuuhuone(pelaaja, vihko)

    peli_kaynnissa = True

    while peli_kaynnissa == True:
        print("")
        print("Nykyinen sijainti:", pelaaja.sijainti.nimi)

        komento = questionary.select(
            "Minne haluat mennä?",
            choices=[
                "Makuuhuone",
                "Keittiö",
                "Olohuone",
                "Eteinen",
                "Kylpyhuone",
                "Inventaario",
                "Lähde kouluun",
                "Lopeta peli"
            ]
        ).ask()

        if komento == "Makuuhuone":
            pelaaja.sijainti = makuuhuone_obj
            makuuhuone(pelaaja, vihko)

        elif komento == "Keittiö":
            pelaaja.sijainti = keittio_obj
            keittio(pelaaja, kyna, omena)

        elif komento == "Olohuone":
            pelaaja.sijainti = olohuone_obj
            olohuone(pelaaja, kannettava)

        elif komento == "Eteinen":
            pelaaja.sijainti = eteinen_obj
            eteinen(pelaaja, laukku)

        elif komento == "Kylpyhuone":
            pelaaja.sijainti = kylpyhuone_obj
            kylpyhuone(pelaaja, avaimet)

        elif komento == "Inventaario":
            pelaaja.inventaario()

        elif komento == "Lähde kouluun":
            nimet = []

            for esine in pelaaja.tavarat:
                nimet.append(esine.nimi)

            if "laukku" not in nimet:
                print("")
                kirjoita("Hetkinen...")
                time.sleep(1)
                kirjoita("Missä laukku on?")
                kirjoita("Et kai aio kantaa kaikkea käsissäsi?")
                kirjoita("Etsi laukku eteisestä.")

            elif (
                "vihko" not in nimet
                or "kynä" not in nimet
                or "kannettava" not in nimet
            ):
                print("")
                kirjoita("Oletko tosissasi?")
                kirjoita("Sinua ei päästetä uusintakokeeseen ilman tavaroita!")

                print("")
                kirjoita("Sinulta puuttuu:")

                if "vihko" not in nimet:
                    print("- vihko")

                if "kynä" not in nimet:
                    print("- kynä")

                if "kannettava" not in nimet:
                    print("- kannettava")

                print("")
                kirjoita("Kerää tavarasi ensin.")
                kirjoita("Tarvittavien tavaroiden lista löytyy keittiön lapusta.")

            else:
                valinta = questionary.select(
                    "Kaikki opiskelutavarat ovat mukana. Haluatko lähteä?",
                    choices=[
                        "Kyllä, lähden kouluun",
                        "Ei, tarkistan vielä asunnon"
                    ]
                ).ask()

                if valinta == "Ei, tarkistan vielä asunnon":
                    print("")
                    kirjoita("Päätät tarkistaa vielä, että kaikki on kunnossa.")

                elif valinta == "Kyllä, lähden kouluun":
                    print("")
                    kirjoita("Laukku on pakattu.")
                    kirjoita("Puet kengät jalkaan ja suljet oven.")
                    time.sleep(1)

                    print("")
                    kirjoita("Lähdet kiireesti kohti koulua.")
                    time.sleep(1)

                    print("")
                    kirjoita("Matkalla alat miettiä aamun tapahtumia...")
                    time.sleep(1.5)

                    if "avaimet" not in nimet:
                        print("")
                        kirjoita("Hetkinen...")
                        time.sleep(1)

                        kirjoita("Avaimet.")
                        time.sleep(1)

                        kirjoita("Ne jäivät kotiin.")
                        time.sleep(1)

                        print("")
                        kirjoita("Hienoa!")
                        kirjoita("Nyt saat maksaa illalla noin 200 euroa")
                        kirjoita("oven avaamisesta ja uusista avaimista.")

                    else:
                        print("")
                        kirjoita("Tarkistat taskusi.")
                        kirjoita("Avaimet ovat mukana!")
                        kirjoita("Ainakin yksi asia meni tänään oikein.")

                    if pelaaja.syonyt == False:
                        print("")
                        kirjoita("Et syönyt aamulla mitään.")
                        kirjoita("Kokeessa vatsasi murisee.")
                        kirjoita("Keskittyminen on vaikeaa.")

                    else:
                        print("")
                        kirjoita("Onneksi söit aamupalan.")
                        kirjoita("Et ainakaan tee koetta tyhjällä vatsalla.")

                    if pelaaja.juonut == False:
                        print("")
                        kirjoita("Et juonut edes kahvia tai teetä.")
                        kirjoita("Olet vieläkin vähän unessa.")

                    else:
                        print("")
                        kirjoita("Aamukahvi tai tee auttoi vähän heräämään.")

                    if pelaaja.sanky_pedattu == False:
                        print("")
                        kirjoita("Ja sänkykin jäi petaamatta.")
                        time.sleep(1)

                        kirjoita("Ehkä huono päivä alkoi jo siitä...")
                        kirjoita("Kuka tietää.")

                    else:
                        print("")
                        kirjoita("Ja hei, ainakin muistit pedata sängyn.")
                        kirjoita("Äiti olisi ylpeä.")

                    if pelaaja.lukenut_viestin == False:
                        print("")
                        kirjoita("Et myöskään lukenut opettaja Laurin sähköpostia.")
                        kirjoita("Toivottavasti siellä ei ollut mitään tärkeää...")

                    else:
                        print("")
                        kirjoita("Onneksi tarkistit myös opettaja Laurin viestin.")

                    if "omena" in nimet:
                        print("")
                        kirjoita("Ja sinulla on vielä omena mukana.")
                        kirjoita("Ehkä tästä päivästä sittenkin selvitään.")

                    print("")
                    time.sleep(1)

                    kirjoita("Saavut lopulta koululle.")
                    time.sleep(1)

                    kirjoita("Uusintakoe alkaa...")
                    time.sleep(2)

                    print("")

                    if (
                        "avaimet" in nimet
                        and pelaaja.syonyt == True
                    ):
                        kirjoita("Selvisit kaoottisesta aamusta!")
                        kirjoita("Sinulla on opiskelutavarat ja avaimet mukana.")
                        kirjoita("Et myöskään lähtenyt kouluun tyhjällä vatsalla.")

                        print("")
                        time.sleep(1)

                        kirjoita("Nyt ei auta muu kuin yrittää läpäistä koe.")

                        print("")
                        kirjoita("HYVÄ LOPPU!")

                    else:
                        kirjoita("Koe ei mennyt ihan suunnitelmien mukaan.")
                        time.sleep(1)

                        print("")
                        kirjoita("Ehkä syynä oli nälkä.")
                        kirjoita("Ehkä unohdetut avaimet.")
                        kirjoita("Ehkä petaamaton sänky.")
                        time.sleep(1)

                        print("")
                        kirjoita("Tai ehkä olisi vain pitänyt herätä ajoissa.")

                        print("")
                        kirjoita("Parempi onni ensi kerralla!")

                    peli_kaynnissa = False

        elif komento == "Lopeta peli":
            print("")
            kirjoita("Päätät, että tämä aamu saa riittää.")
            kirjoita("Peli loppui ;()")
            peli_kaynnissa = False