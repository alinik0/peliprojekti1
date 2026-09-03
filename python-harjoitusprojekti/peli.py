nimi = input("Anna pelaajan nimi: ")
ika = int(input("Anna pelaajan ikä: "))

#print("Pelaajan nimi:", nimi)
#print("Pelaajan ikä:", ika)

if ika < 12:
    print("Olet liian nuori pelaamaan.")

else:
    print("Tervetuloa,", nimi)

    komento = ""

    while komento != "lopeta":
        print("\nPäävalikko:")
        print("tutki")
        print("liiku")
        print("apu")
        print("lopeta")

        komento = input("Anna komento: ")

        if komento == "tutki":
            print("Tutkit huonetta.")

        elif komento == "liiku":
            print("Liikut eteenpäin")

        elif komento == "apu":
            print("Sinun pitää löytää uloskäynti")

        elif komento == "lopeta":
            print("Peli loppui ;()")

        else:
            print("Tuntematon komento")