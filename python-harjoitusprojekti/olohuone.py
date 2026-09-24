import questionary


def olohuone(pelaaja, kannettava):
    print("")
    print("=== OLOHUONE ===")
    print("Menet olohuoneeseen.")
    print("Sohvalla on kannettava tietokone.")

    while True:
        komento = questionary.select(
            "Mitä haluat tehdä?",
            choices=[
                "Tutki sohva",
                "Lue sähköposti",
                "Ota kannettava",
                "Tutki olohuone",
                "Poistu olohuoneesta"
            ]
        ).ask()

        if komento == "Tutki sohva":
            print("Tutkit sohvan.")
            print("Katsot myös tyynyjen välistä.")
            print("Löydät vähän roskaa, mutta et avaimia.")

        elif komento == "Lue sähköposti":
            pelaaja.lukenut_viestin = True

            print("")
            print("Avaat tietokoneen.")
            print("Sinulla on uusi sähköposti opettaja Laurilta.")
            print("")
            print("'Huomenta!'")
            print("'Muistutus: tänään on uusintakoe.'")
            print("'Tule ajoissa paikalle.'")
            print("")
            print("No niin...")
            print("Nyt tuli vielä enemmän kiire.")

        elif komento == "Ota kannettava":
            if kannettava not in pelaaja.tavarat:
                pelaaja.tavarat.append(kannettava)
                print("Otat kannettavan mukaan.")
            else:
                print("Kannettava on jo mukana.")

        elif komento == "Tutki olohuone":
            print("Tutkit olohuoneen tarkasti.")
            print("Avaimet eivät ole täällä.")

        elif komento == "Poistu olohuoneesta":
            print("Poistut olohuoneesta.")
            break
        