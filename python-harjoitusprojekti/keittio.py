import questionary


def keittio(pelaaja, kyna, omena):
    print("")
    print("=== KEITTIÖ ===")
    print("Menet keittiöön.")
    print("Pöydällä on lappu ja kynä.")
    print("Sinulla alkaa olla vähän nälkä.")

    while True:
        komento = questionary.select(
            "Mitä haluat tehdä?",
            choices=[
                "Lue äidin lappu",
                "Ota kynä",
                "Keitä kahvia",
                "Keitä teetä",
                "Avaa jääkaappi",
                "Tutki laatikot",
                "Poistu keittiöstä"
            ]
        ).ask()

        if komento == "Lue äidin lappu":
            print("")
            print("Luet äidin jättämän lapun:")
            print("")
            print("'Huomenta!'")
            print("'Voileipäsi on jääkaapissa.'")
            print("")
            print("'Älä unohda ottaa mukaan:'")
            print("- kannettava")
            print("- kynä")
            print("- vihko")
            print("")
            print("'Ja Lauri-opettaja sanoi, että älä vaan myöhästy!'")
            print("'Älä nyt mokaa tätä!'")
            print("")
            print("- Äiti")

        elif komento == "Ota kynä":
            if kyna not in pelaaja.tavarat:
                pelaaja.tavarat.append(kyna)
                print("Otat kynän pöydältä.")
            else:
                print("Kynä on jo mukana.")

        elif komento == "Keitä kahvia":
            if pelaaja.juonut == False:
                pelaaja.juonut = True
                print("Keität kupin kahvia.")
                print("Juot kahvin nopeasti.")
                print("Nyt olet vähän enemmän hereillä.")
            else:
                print("Olet jo juonut jotain.")

        elif komento == "Keitä teetä":
            if pelaaja.juonut == False:
                pelaaja.juonut = True
                print("Keität kupin teetä.")
                print("Juot teen nopeasti.")
            else:
                print("Olet jo juonut jotain.")

        elif komento == "Avaa jääkaappi":
            print("")
            print("Avaat jääkaapin.")
            print("Siellä on voileipä ja omena.")

            valinta = questionary.select(
                "Mitä haluat tehdä?",
                choices=[
                    "Syö voileipä",
                    "Ota omena",
                    "Sulje jääkaappi"
                ]
            ).ask()

            if valinta == "Syö voileipä":
                if pelaaja.syonyt == False:
                    pelaaja.syonyt = True
                    print("Syöt voileivän.")
                    print("Nyt et ainakaan lähde kouluun tyhjällä vatsalla.")
                else:
                    print("Olet jo syönyt voileivän.")

            elif valinta == "Ota omena":
                if omena not in pelaaja.tavarat:
                    pelaaja.tavarat.append(omena)
                    print("Otat omenan mukaan.")
                else:
                    print("Omena on jo mukana.")

            elif valinta == "Sulje jääkaappi":
                print("Suljet jääkaapin.")

        elif komento == "Tutki laatikot":
            print("Tutkit keittiön laatikot.")
            print("Lusikoita, haarukoita, veitsiä...")
            print("Ei avaimia.")

        elif komento == "Poistu keittiöstä":
            print("Poistut keittiöstä.")
            break