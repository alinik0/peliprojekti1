import questionary


def kylpyhuone(pelaaja, avaimet):
    print("")
    print("=== KYLPYHUONE ===")
    print("Menet kylpyhuoneeseen.")
    print("Nurkassa on kasa likaisia vaatteita.")

    while True:
        komento = questionary.select(
            "Mitä haluat tehdä?",
            choices=[
                "Tutki kaapit",
                "Tutki likaiset vaatteet",
                "Tarkista farkut",
                "Poistu kylpyhuoneesta"
            ]
        ).ask()

        if komento == "Tutki kaapit":
            print("Tutkit kylpyhuoneen kaapit.")
            print("Hammastahnaa, pyyhkeitä ja muuta tavaraa.")
            print("Ei avaimia.")

        elif komento == "Tutki likaiset vaatteet":
            print("Tutkit likaisia vaatteita.")
            print("Löydät farkut, joita käytit eilen.")
            print("Hmm... ehkä taskut kannattaa tarkistaa.")

        elif komento == "Tarkista farkut":
            if avaimet not in pelaaja.tavarat:
                print("Tarkistat farkkujen taskut...")
                print("")
                print("Hetkinen...")
                print("")
                print("AVAIMET!")
                print("Ne olivat koko ajan farkkujen taskussa.")
                print("Tietenkin.")

                pelaaja.tavarat.append(avaimet)
            else:
                print("Olet jo löytänyt avaimet.")

        elif komento == "Poistu kylpyhuoneesta":
            print("Poistut kylpyhuoneesta.")
            break