nimi = input("Anna pelaajan nimi: ")
ika = int(input("Anna pelaajan ikä: "))

#print("Pelaajan nimi:", nimi)
#print("Pelaajan ikä:", ika)

tavarat = []


def tutki():
    print("Tutkit huonetta.")


def liiku():
    print("Liikut eteenpäin.")


def ota_esine(tavarat):
    esine = input("Mitä esinettä haluat ottaa? ")
    tavarat.append(esine)


def inventaario(tavarat):
    print("Inventaario:")
    for esine in tavarat:
        print("-", esine)


def apu():
    print("Sinun pitää löytää kadonneet avaimet.")


if ika < 12:
    print("Olet liian nuori pelaamaan.")

else:
    print("Tervetuloa,", nimi)

    print("Kello on 8.00.")
    print("Olet nukkunut vähän liian pitkään.")
    print("Oppitunnit alkavat pian.")
    print("Sinun täytyy valmistautua nopeasti.")
    print("Mutta et löydä avaimiasi.")

    komento = ""

    while komento != "lopeta":
        print("Päävalikko:")
        print("tutki")
        print("liiku")
        print("ota")
        print("inventaario")
        print("apu")
        print("lopeta")

        # jouduin kirjoittamaan komennot aina samalla tavalla, mikä oli ärsyttävää...
        # lisäsin lower() toiminnon, jotta pääsen tästä ongelmasta eroon
        komento = input("Anna komento: ").lower()

        if komento == "tutki":
            tutki()

        elif komento == "liiku":
            liiku()

        elif komento == "ota":
            ota_esine(tavarat)

        elif komento == "inventaario":
            inventaario(tavarat)

        elif komento == "apu":
            apu()

        elif komento == "lopeta":
            print("Peli loppui ;()")

        else:
            print("Tuntematon komento")
