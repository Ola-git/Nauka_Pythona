#print("Hello World!")

# imie = "Aleksandra"
# ilosc_ksiazek = 10
# srednia = 4.5
#
# print("Hello World!" + imie)
# print("Ma" + str(ilosc_ksiazek))
# print("Srednia: " + str(srednia))


# imie_psa = "Burek"
# kolor = "brazowy"
# wiek = 10
#
# print(imie_psa + " ma " + str(wiek) + " lat i jest " + kolor + ".")

# marka = "Pegeout"
# ilosc_drzwi = 5
# pojemnosc = 1.3
#
# marka_up = marka.upper()
# marka_low = marka.lower()
#
# print(marka_up)
# print(marka_low)
#
# print(marka[1:-1])
# print(marka[1:-1])
#
# str = input("Podaj haslo")
# len = len(str) - 2
# stars = len * "*"
#
# if len >= 3:
#     print(str[0] + stars + str[-1])
#
# if len <2 and str != "":
#     print("Podane haslo jest za krotkie")
#
# if str == "":
#     print("Nie podano hasla")
#
# imie = "Ala"
# zwierze = "kot"
# print("{0} ma {1}a".format(imie, zwierze))

# samochody = ['syrena', 'polonez', 'fiat', 'kia']
# ilosc = [3, 5, 3, 5]
#
# # print(samochody[0])
# # print(samochody[1])
#
# # for s in samochody:
# #     print(s)
#
# for idx in range(len(samochody)):
#     print("idx: " + str(idx) + " : " + samochody[idx])
#     print(samochody[idx] + " ma ilosc drzwi " + str(ilosc[idx]))

# samolot = {'name' : 'boeing',
#             'przebieg' : 10000,
#             'type' : 'pasazerski'}

# for key, value in samolot.iteritems():
#     print("{0} : {1}".format(key, value))
#
# for key in samolot:
#     print("{0} : {1}".format(key, samolot[key]))

# def print_dict(d):
#     for key in samolot:
#         print("{0} : {1}".format(key, d[key]))
#
# if __name__ == "__main__":
#     samolot = {'name' : 'boeing',
#     'przebieg' : 10000,
#     'type' : 'pasazerski'}
#
#     print_dict(samolot)

# def calculate_vat(netto):
#     vat = float(netto * 23)/100
#     return vat
#
# if __name__ == "__main__":
#     vat = calculate_vat(1000)
#     print("{0}".format(vat))

# def main():
#     print "Tutaj program"
#
# if __name__ == "__main__":
#     main()

# file = open("testfile.txt", "w")
# file.write("Hello world!")
# file.close()

# file = open("testfile.txt", "r")
# print(file.read())
# file.close()

with open("testfile.txt", 'w') as f:
    print(f.read())
