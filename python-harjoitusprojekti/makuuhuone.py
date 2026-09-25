import questionary


def makuuhuone(pelaaja, vihko):
    print("")
    print("=== MAKUUHUONE ===")
    print("Olet makuuhuoneessa.")
    print("Sänky on petaamatta ja vaatteita on siellä täällä.")

    while True:
        komento = questionary.select(
            "Mitä haluat tehdä?",
            choices=[
                "Petaa sänky",
                "Tutki vaatekaappi",
                "Ota vihko",
                "Pukeudu",
                "Poistu makuuhuoneesta"
            ]
        ).ask()

        if komento == "Petaa sänky":
            if pelaaja.sanky_pedattu == False:
                pelaaja.sanky_pedattu = True
                print("Petaat sängyn.")
                print("Nyt huone näyttää vähän paremmalta.")
            else:
                print("Sänky on jo pedattu.")

        elif komento == "Tutki vaatekaappi":
            print("Tutkit vaatekaapin.")
            print("Löydät paljon vaatteita, mutta et avaimia.")

        elif komento == "Ota vihko":
            if vihko not in pelaaja.tavarat:
                pelaaja.tavarat.append(vihko)
                print("Otat vihkon mukaan.")
                print("Tarvitset sitä uusintakokeessa.")
            else:
                print("Vihko on jo mukana.")

        elif komento == "Pukeudu":
            if pelaaja.pukeutunut == False:
                pelaaja.pukeutunut = True
                print("Vaihdat nopeasti vaatteet.")
                print("Nyt olet valmis lähtemään makuuhuoneesta.")
            else:
                print("Olet jo pukeutunut.")

        elif komento == "Poistu makuuhuoneesta":
            if pelaaja.pukeutunut == False:
                print("Oletko tosissasi?")
                print("Olet edelleen yövaatteissa.")
                print("Pukeudu ensin!")
            else:
                print("Poistut makuuhuoneesta.")
                break