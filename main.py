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
    input("\n Naciśnij ENTER aby wejść do MENU")
    os.system("cls")


def menu():
    while True:
        czysc_ekran()
        print("MENU\n1. Wyświetl aktualny stan magazynowy\n2. Wyszukaj towar\n3. Dodaj towar\n4. Usuń towar\n5. Zmien ilosc towaru\n6. Pokaż aktualną wartość wszystkich towarów w magazynie\n7. Wyjdź\n")

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
                # czysc_ekran()

            case 2:
                try:
                    szukany = input(
                        "Podaj nazwe towaru jaki chcesz sprawdzić: ")
                    funkcje.wyszukaj(szukany)
                except PowrotDoMenu:
                    print("Operacja anulowana")

                # czysc_ekran()
            case 3:
                try:
                    while True:
                        nazwa = pobierz("Podaj nazwe produktu: ")
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

                        pyt = pobierz(
                            " Czy chcesz zmienić jego ilość? t/n").lower()
                        while pyt not in ("t", "n"):
                            pyt = pobierz(
                                "Towar o takiej nazwie istnieje już w bazie! Czy chcesz zmienić jego ilość? t/n").lower()
                        if pyt == 't':
                            while True:
                                d_cz_u = pobierz(
                                    "Chcesz dodać ilosc twarów (d) czy ująć (u)? Napisz d bądź u: ").lower()
                                if d_cz_u in ("d", "u"):
                                    break

                            while True:
                                try:
                                    ile = int(pobierz("Podaj ilość: "))
                                    break
                                except ValueError:
                                    print("Pdaj wartość liczbową! ")

                            funkcje.zmien_ilosc(nazwa, d_cz_u, ile)

                    else:
                        while True:
                            try:
                                ile = int(pobierz("Podaj ilość: "))
                                break
                            except ValueError:
                                print("Podaj wartosc liczbowa!")

                        while True:
                            try:
                                cena = float(pobierz("Podaj cene: "))
                                if cena <= 0:
                                    while True:
                                        print("Cena musi być większa od 0!")
                                        cena = float(pobierz("Podaj cene: "))
                                        if cena > 0:
                                            break
                                break
                            except ValueError:
                                print("Podaj wartosc liczbowa!")

                        funkcje.dodaj_produkt(nazwa, ile, cena)
                        funkcje.wyswietl_wszystko()
                except PowrotDoMenu:
                    print("Operacja anulowana")
                czysc_ekran()
            case 4:
                funkcje.wyswietl_wszystko()
                try:
                    nazwa = pobierz(
                        "\nPodaj nazwe towaru który chcesz usunąć: \n")

                    funkcje.usun_produkt(nazwa)
                except PowrotDoMenu:
                    print("Operacja anulowana")
                # czysc_ekran()
            case 5:
                try:
                    nazwa = pobierz(
                        "Podaj nazwe towaru którego ilość chcesz zmodyfikować: ")
                    if nazwa not in funkcje.data:
                        print(
                            "Nie ma takiego towaru na stanie. Aby go dodac wejdź w Menu i wybierz opcje 3.")
                    else:
                        while True:
                            d_cz_u = pobierz(
                                "Chcesz dodać ilosc twarów (d) czy ująć (u)? Napisz d bądź u: ").lower()
                            if d_cz_u in ("d", "u"):
                                break
                        while True:
                            try:
                                ile = int(pobierz("Podaj ilość: "))
                                break
                            except ValueError:
                                print("Pdaj wartość liczbową! ")

                        funkcje.zmien_ilosc(nazwa, d_cz_u, ile)
                except PowrotDoMenu:
                    print("Operacja anulowana")
                # czysc_ekran()

            case 6:
                funkcje.wartosc_magazynu()
                # czysc_ekran()
            case 7:
                print("\nPrgram kończy działanie\n")
                os.system("cls")
                break


menu()
