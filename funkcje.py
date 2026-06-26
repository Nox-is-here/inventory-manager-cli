import json
import os

PLIK = "data.json"

if os.path.exists(PLIK):
    with open(PLIK, "r", encoding="utf-8") as f:
        data = json.load(f)
else:
    data = {}
    with open(PLIK, "w", encoding="utf-8") as f:
        json.dump(data, f)


def zapisz():
    with open(PLIK, "w", encoding="utf-8")as w:
        json.dump(data, w)


def dodaj_produkt(nazwa, ile, cena):
    data[nazwa] = {
        "ilość": ile,
        "cena": cena

    }
    zapisz()


def usun_produkt(nazwa):
    # wyswietl_wszystko()
    if nazwa not in data:
        print("Nie ma takiego produktu w stanie magazynowym!")
    else:
        del data[nazwa]
        zapisz()
        print("\nTowar został usunięty\n")
        wyswietl_wszystko()


def zmien_ilosc(nazwa, d_cz_u, ile):
    if d_cz_u == 'd':
        data[nazwa]["ilość"] += ile
    else:
        if data[nazwa]["ilość"] - ile <= 0:
            print(
                f"Nie można wykonac operacji! Na stanie jest {data[nazwa]} produktu: {nazwa}")
        else:
            data[nazwa]["ilość"] -= ile
    print(f"{nazwa} ilość: {data[nazwa]["cena"]} cena: {data[nazwa]["ilość"]}")
    zapisz()


def wyswietl_wszystko():
    posortowane = sorted(data.items())
    for i, (keys, values) in enumerate(posortowane, start=1):
        print(
            f"{i}. {keys:20} cena: {values['cena']:<30} ile: {values['ilość']:<10}")


def wyszukaj(szukany):
    if szukany in data:
        print(
            f"towar: {szukany:20} ilość: {data[szukany]["ilość"]:<30} cena: {data[szukany]["cena"]:<10}")
    else:
        print("Nie ma takiego towaru w bazie")


def wartosc_magazynu():
    ile = 0
    # ceny = 0
    for element in data:
        ile += (data[element]["cena"]*data[element]["ilość"])
    print(f"Wartość wszystkich towatow wynosi {ile}")
