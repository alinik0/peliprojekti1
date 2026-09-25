import questionary


def eteinen(pelaaja, laukku):
    print("")
    print("=== ETEINEN ===")
    print("Menet eteiseen.")
    print("Ulko-ovi on aivan edessäsi.")
    print("Eteisessä on kaappi, takki ja opiskelulaukku.")

    while True:
        komento = questionary.select(
            "Mitä haluat tehdä?",
            choices=[
                "Tutki kaappi",
                "Tarkista takki",
                "Ota laukku",
                "Poistu eteisestä"
            ]
        ).ask()

        if komento == "Tutki kaappi":
            print("Tutkit eteisen kaapin.")
            print("Löydät kenkiä, vanhan sateenvarjon ja muuta tavaraa.")
            print("Avaimia ei näy.")

        elif komento == "Tarkista takki":
            print("Tarkistat takin taskut.")
            print("Ei avaimia.")

        elif komento == "Ota laukku":
            if laukku not in pelaaja.tavarat:
                pelaaja.tavarat.append(laukku)
                print("Otat opiskelulaukun mukaan.")
            else:
                print("Laukku on jo mukana.")

        elif komento == "Poistu eteisestä":
            print("Poistut eteisestä.")
            break