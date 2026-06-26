
# dodaj produkt do slownika produkty:


# def wyswietl_wszystkie():
#     for i, emement in enumerate(produkty.keys(), start=1):
#         print(i, emement)


# def dodaj(nazwa, ilosc, cena):
#     produkty[nazwa] = {"ilość": ilosc, "cena": cena}
#     wyswietl_wszystkie()


# dodaj("kiwi", 12, 25)


# def zapisz():
#     with open(PLIK, "w", encoding="utf-8")as w:
#         json.dump(data, w)


# with open(PLIK, "r", encoding="utf-8") as f:
#     data = json.load(f)


# def dodaj_produkt(nazwa, ile, cena):
#     data[nazwa] = {
#         "ilość": ile,
#         "cena": cena

#     }
#     zapisz()

#     print(data.keys())


# def usun_produkt(nazwa):
#     if nazwa not in data:
#         print("Nie ma takiego produktu w stanie magazynowym!")
#     else:
#         del data[nazwa]
#         zapisz()

#     print(data.keys())


# def zmien_ilosc(nazwa, d_cz_u, ile):
#     if d_cz_u == 'd':
#         data[nazwa]["ilość"] += ile
#     else:
#         if data[nazwa]["ilość"] - ile <= 0:
#             print(
#                 f"Nie można wykonac operacji! Na stanie jest {data[nazwa]} produktu: {nazwa}")
#         else:
#             data[nazwa]["ilość"] -= ile
#     wyswietl_wszystko()
#     zapisz()


# def wyswietl_wszystko():
#     posortowane = sorted(data.items())
#     for i, (keys, values) in enumerate(posortowane, start=1):
#         print(i, keys, values)


# def wyszukaj(szukany):
#     if szukany in data:
#         print(
#             f"towar: {szukany}, ilość: {data[szukany]["ilość"]}, cena: {data[szukany]["cena"]}")
#     else:
#         print("Nie ma takiego towaru w bazie")


# def wartosc_magazynu():
#     ile = 0
#     ceny = []
#     for element in data:
#         ile += data[element]["cena"]
#         ceny.append(data[element]["cena"])
#     print(f"Wartość wszystkich towatow wynosi {ile}")
#     print(ceny)

# import funkcje
# import json

# PLIK = "data.json"
# with open(PLIK, "r", encoding="utf-8") as f:
#     data = json.load(f)

# funkcje.dodaj_produkt("Ziemia", 2, 11)
# funkcje.usun_produkt("mleko")
# funkcje.zmien_ilosc("Ziemia", 'd', 12)
# funkcje.dodaj_produkt("Adam", 2, 0)
# print("")
# funkcje.wyswietl_wszystko()
# print("")
# funkcje.wyszukaj("Adam")
# funkcje.wyszukaj("Kokoszka")
# data = json.load(PLIK)
# print(data)

# with open(PLIK, "w") as f:
#     json.dump(data, f)
# funkcje.wartosc_magazynu()

# print("DZIALAM AL CHUJ JeSTeM!!!")

import os
import funkcje
import json


class PowrotDoMenu(Exception):
    pass


def pobierz(komunikat):
    tekst = input(f"{komunikat} (q - anuluj): ")

    if tekst.lower() == "q":
        raise PowrotDoMenu

    return tekst


def czysc_ekran():
    input("\n Naciśnij ENTER aby wrcic do MENU")
    os.system("cls")


def menu():
    while True:
        print("MENU\n1.Wyświetl aktualny stan magazynowy\n2.Wyszukaj towar\n3. Dodaj towar\n4.Usuń towar\n5.Zmien ilosc towaru\n6. Pokaż aktualną wartość wszystkich towarów w magazynie\n7. Wyjdź\n")

        while True:
            try:
                wybor = int(input("Wybierz co chcesz robić! "))
                print("")
                if wybor in range(1, 8):
                    break
            except ValueError:
                print(
                    "Musisz wybrac opcje 1-6 poprzez wprowadzenie przy pomocy klawiatory znakow 1-6 i zatwierdzenie klawiszem ENTER")

        match wybor:
            case 1:
                print("\nAKTUALNY STAN MAGAZYNU:\n")
                funkcje.wyswietl_wszystko()
                czysc_ekran()

            case 2:
                szukany = input("Podaj nazwe towaru jaki chcesz sprawdzić: ")
                funkcje.wyszukaj(szukany)
                czysc_ekran()
            case 3:

                while True:
                    nazwa = input("Podaj nazwe produktu: ")
                    sprawdzenie_poprawnosci = nazwa.isalnum()

                    if sprawdzenie_poprawnosci == False:
                        print(
                            "Nazwa towaru nie moze zawierac innych znakow niz litery i cyfry")
                    else:
                        break

                if nazwa in funkcje.data:
                    print("Towar o takiej nazwie istnieje już w bazie!")
                    print(
                        f"{nazwa} ilość {funkcje.data[nazwa]["ilość"]} cena: {funkcje.data[nazwa]["cena"]}")

                    pyt = input(
                        " Czy chcesz zmienić jego ilość? t/n").lower()
                    while pyt not in ("t", "n"):
                        pyt = input(
                            "Towar o takiej nazwie istnieje już w bazie! Czy chcesz zmienić jego ilość? t/n").lower()
                    if pyt == 't':
                        while True:
                            d_cz_u = input(
                                "Chcesz dodać ilosc twarów (d) czy ująć (u)? Napisz d bądź u: ").lower()
                            if d_cz_u in ("d", "u"):
                                break

                        while True:
                            try:
                                ile = int(input("Podaj ilość: "))
                                break
                            except ValueError:
                                print("Pdaj wartość liczbową! ")

                        funkcje.zmien_ilosc(nazwa, d_cz_u, ile)

                else:
                    while True:
                        try:
                            ile = int(input("Podaj ilość: "))
                            break
                        except ValueError:
                            print("Podaj wartosc liczbowa!")

                    while True:
                        try:
                            cena = float(input("Podaj cene: "))
                            if cena <= 0:
                                while True:
                                    print("Cena musi być większa od 0!")
                                    cena = float(input("Podaj cene: "))
                                    if cena > 0:
                                        break
                            break
                        except ValueError:
                            print("Podaj wartosc liczbowa!")

                    funkcje.dodaj_produkt(nazwa, ile, cena)
                czysc_ekran()
            case 4:
                nazwa = input("Podaj nazwe towaru który chcesz usunąć: ")

                funkcje.usun_produkt(nazwa)
                czysc_ekran()
            case 5:
                nazwa = input(
                    "Podaj nazwe towaru którego ilość chcesz zmodyfikować: ")
                while True:
                    d_cz_u = input(
                        "Chcesz dodać ilosc twarów (d) czy ująć (u)? Napisz d bądź u: ").lower()
                    if d_cz_u in ("d", "u"):
                        break
                while True:
                    try:
                        ile = int(input("Podaj ilość: "))
                        break
                    except ValueError:
                        print("Pdaj wartość liczbową! ")

                funkcje.zmien_ilosc(nazwa, d_cz_u, ile)
                czysc_ekran()

            case 6:
                funkcje.wartosc_magazynu()
                czysc_ekran()
            case 7:
                print("\nPrgram kończy działanie\n")
                os.system("cls")
                break


menu()
