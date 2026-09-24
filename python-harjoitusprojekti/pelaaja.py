class Pelaaja:
    def __init__(self, nimi, sijainti):
        self.nimi = nimi
        self.tavarat = []
        self.sijainti = sijainti
        self.pukeutunut = False
        self.sanky_pedattu = False
        self.syonyt = False
        self.juonut = False
        self.lukenut_viestin = False

    def inventaario(self):
        print("")
        print("Inventaario:")

        if len(self.tavarat) == 0:
            print("Inventaario on tyhjä.")
        else:
            for esine in self.tavarat:
                print("-", esine.nimi)