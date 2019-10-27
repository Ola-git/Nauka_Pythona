import pprint

def main():


    koszyk = [{'nazwa' : 'mlekowita', 'cena' : 5, 'vat' : 23, 'jednostka' : "litr", "ilosc" : 10},
            {'nazwa' : 'cukier','cena' : 6, 'vat' : 23, 'jednostka' : "kg", "ilosc" : 5},
            {'nazwa' : 'ser', 'cena' : 5, 'vat' : 23, 'jednostka' : "kg", "ilosc" : 3}]



    for idx in range(len(koszyk)):
        print((koszyk[idx]["nazwa"]) + " , " + str(koszyk[idx]["ilosc"]))

    file = open("koszyk.csv", "w")
    for poz in koszyk:
        linia = "{0},{1}\n".format(poz['nazwa'], poz['cena'])
        file.write(linia)
    file.close()

    koszyk2 = []
    f2 = open("koszyk.csv", "r")
    calosc = f2.read()
    linie = calosc.split("\n")
    for l in linie:
        produkt = {}
        if len(l) > 0:
            pola = l.split(",")
            produkt['nazwa'] = pola[0]
            produkt['cena'] = pola[1]
            koszyk2.append(produkt)

    pprint.pprint(koszyk2)


if __name__ == "__main__":
    main()
