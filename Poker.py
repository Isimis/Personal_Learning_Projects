# Wgranie potrzebnych modułów
import random
import math

# Listy które będą nam potrzebne w grze
karty_gracza = []
karty_gracza2 = []
karty_na_stole = []
zetony_gracza = int(0)
zetony_gracza2 = int(0)
pula = int(0)
reszta_puli = int(0)
reszta = int(0)
licznik_rund = int(0)
stawka = int(0)
podbicie = int(0)
koniec = True
pasuj = False
talia = [
    "2S",
    "3S",
    "4S",
    "5S",
    "6S",
    "7S",
    "8S",
    "9S",
    "TS",
    "JS",
    "QS",
    "KS",
    "AS",
    "2H",
    "3H",
    "4H",
    "5H",
    "6H",
    "7H",
    "8H",
    "9H",
    "TH",
    "JH",
    "QH",
    "KH",
    "AH",
    "2D",
    "3D",
    "4D",
    "5D",
    "6D",
    "7D",
    "8D",
    "9D",
    "TD",
    "JD",
    "QD",
    "KD",
    "AD",
    "2C",
    "3C",
    "4C",
    "5C",
    "6C",
    "7C",
    "8C",
    "9C",
    "TC",
    "JC",
    "QC",
    "KC",
    "AC",
]
slownik_kart = {
    talia[0]: "2 PIK",
    talia[1]: "3 PIK",
    talia[2]: "4 PIK",
    talia[3]: "5 PIK",
    talia[4]: "6 PIK",
    talia[5]: "7 PIK",
    talia[6]: "8 PIK",
    talia[7]: "9 PIK",
    talia[8]: "10 PIK",
    talia[9]: "Walet PIK",
    talia[10]: "Dama PIK",
    talia[11]: "Król PIK",
    talia[12]: "As PIK",
    talia[13]: "2 KIER",
    talia[14]: "3 KIER",
    talia[15]: "4 KIER",
    talia[16]: "5 KIER",
    talia[17]: "6 KIER",
    talia[18]: "7 KIER",
    talia[19]: "8 KIER",
    talia[20]: "9 KIER",
    talia[21]: "10 KIER",
    talia[22]: "Walet KIER",
    talia[23]: "Dama KIER",
    talia[24]: "Król KIER",
    talia[25]: "As KIER",
    talia[26]: "2 KARO",
    talia[27]: "3 KARO",
    talia[28]: "4 KARO",
    talia[29]: "5 KARO",
    talia[30]: "6 KARO",
    talia[31]: "7 KARO",
    talia[32]: "8 KARO",
    talia[33]: "9 KARO",
    talia[34]: "10 KARO",
    talia[35]: "Walet KARO",
    talia[36]: "Dama KARO",
    talia[37]: "Król KARO",
    talia[38]: "As KARO",
    talia[39]: "2 TREFL",
    talia[40]: "3 TREFL",
    talia[41]: "4 TREFL",
    talia[42]: "5 TREFL",
    talia[43]: "6 TREFL",
    talia[44]: "7 TREFL",
    talia[45]: "8 TREFL",
    talia[46]: "9 TREFL",
    talia[47]: "10 TREFL",
    talia[48]: "Walet TREFL",
    talia[49]: "Dama TREFL",
    talia[50]: "Król TREFL",
    talia[51]: "As TREFL",
}


# Statystyki wyświetlane w trakcie rozgrywki
def statystyki():
    global pula, zetony_gracza, zetony_gracza2, reszta_puli
    print()
    print(f"Żetony w puli: {pula}")
    print(f"Twoje żetony: {zetony_gracza}")
    print(f"Żetony gracza 2: {zetony_gracza2}")
    if reszta_puli > 0:
        print(f"Reszta puli: {reszta_puli}")


# Padowanie gracza
def gracz_pasuje():
    global pula, zetony_gracza2
    print(f"Pasujesz. Rundę wygrywa gracz 2. Zyskuje {pula} żetonów.")
    zetony_gracza2 += pula


# Padowanie bota
def gracz2_pasuje():
    global pula, zetony_gracza
    print(f"Gracz 2 pasuje. Wygrywasz rundę. Zyskujesz {pula} żetonów.")
    zetony_gracza += pula


# Podbicie przez bota
def gracz2_podbija():
    global pula, zetony_gracza, zetony_gracza2, podbicie, pasuj
    podbicie = random.randint(1, math.ceil(zetony_gracza2 / 2))
    print(f"Gracz 2 podbija o {podbicie}")
    pula += podbicie
    zetony_gracza2 -= podbicie
    print()
    while True:
        if pasuj == True:
            break
        decyzja = input("Co robisz? (wyrównaj/pasuj): ")
        if decyzja.lower() == "wyrównaj":
            zetony_gracza -= podbicie
            pula += podbicie
            podbicie = 0
            print("Wyrównujesz")
            while True:
                if pasuj == True:
                    break
                wybor = input("Czy chcesz zrobić coś jeszcze? (czekaj/pasuj/podbij): ")
                if wybor.lower() == "czekaj":
                    print("Czekasz")
                    break
                elif wybor.lower() == "pasuj":
                    gracz_pasuje()
                    pasuj = True
                    break
                elif wybor.lower() == "podbij":
                    while True:
                        try:
                            podbicie = int(input("O ile chcesz podbić? "))
                        except ValueError:
                            print("Podaj liczbę całkowitą!")
                        if (podbicie > 0) and (podbicie <= zetony_gracza):
                            print(f"Podbijasz o {podbicie}.")
                            zetony_gracza -= podbicie
                            pula += podbicie
                            gracz2_reaguje_na_podbicie()
                            break
                        elif podbicie > zetony_gracza:
                            print("Nie możesz postawić więcej żetonów niż posiadasz!")
                            continue
                        elif podbicie <= 0:
                            print("Ilość musi być większa niż 0")
                            continue
                else:
                    print("Proszę o poprawną odpowiedź!")
                    continue
            break
        elif decyzja.lower() == "pasuj":
            gracz_pasuje()
            pasuj = True
            break
        else:
            print("Proszę o poprawną odpowiedź!")
            continue


# Reakcja bota na podbicie
def gracz2_reaguje_na_podbicie():
    global pula, zetony_gracza, zetony_gracza2, podbicie, reszta, pasuj
    ruchy_gracza_2_przy_podbiciu = ("wyrównaj", "pasuj")
    ruch_gracza_2_przy_podbiciu = random.choices(
        ruchy_gracza_2_przy_podbiciu, weights=(78, 22), k=1
    )
    if ruch_gracza_2_przy_podbiciu[0] == "wyrównaj":
        if podbicie > zetony_gracza2:
            podbicie = zetony_gracza2 + reszta
            pula += zetony_gracza2
            reszta = reszta_puli
            zetony_gracza2 -= podbicie
            podbicie = 0
            print(f"Gracz 2 nie może wyrównać. Pula wynosi {pula}, a reszta puli to {reszta_puli}.")
        else:
            zetony_gracza2 -= podbicie
            pula += podbicie
            podbicie = 0
            if zetony_gracza2 > 0:
                opcje_gracza_2_po_wyrównaniu_gdy_ma_jeszcze_zetony = (
                    "podbij",
                    "nic nie rób",
                )
                if zetony_gracza2 <= 1:
                    wybór_gracza_2_po_wyrównaniu_gdy_ma_jeszcze_zetony = random.choices(
                        opcje_gracza_2_po_wyrównaniu_gdy_ma_jeszcze_zetony,
                        weights=(0, 100),
                        k=1,
                    )
                    if wybór_gracza_2_po_wyrównaniu_gdy_ma_jeszcze_zetony[0] == "podbij":
                        print("Grasz 2 wyrównuje")
                        gracz2_podbija()
                    else:
                        print("Grasz 2 wyrównuje")
                else:
                    wybór_gracza_2_po_wyrównaniu_gdy_ma_jeszcze_zetony = random.choices(
                        opcje_gracza_2_po_wyrównaniu_gdy_ma_jeszcze_zetony,
                        weights=(14, 86),
                        k=1,
                    )
                    if wybór_gracza_2_po_wyrównaniu_gdy_ma_jeszcze_zetony[0] == "podbij":
                        print("Grasz 2 wyrównuje")
                        gracz2_podbija()
                    else:
                        print("Grasz 2 wyrównuje")
            else:
                return
    else:
        gracz2_pasuje()
        pasuj = True


# Licytacja
def licytacja():
    global pula, zetony_gracza, zetony_gracza2, podbicie, pasuj
    ruchy_gracza_2_w_licytacji = ("czekaj", "pasuj", "podbij")
    if zetony_gracza2 <= 1:
        ruch_gracza_2_w_licytacji = random.choices(
            ruchy_gracza_2_w_licytacji, weights=(89, 11, 0), k=1
        )
        if ruch_gracza_2_w_licytacji[0] == "czekaj":
            print("Grasz 2 czeka")
            while True:
                if pasuj == True:
                    break
                wybor = input("Co chciałbyś teraz zrobić? (czekaj/pasuj/podbij): ")
                if wybor.lower() == "czekaj":
                    print("Czekasz")
                    break
                elif wybor.lower() == "pasuj":
                    gracz_pasuje()
                    pasuj = True
                    break
                elif wybor.lower() == "podbij":
                    while True:
                        try:
                            podbicie = int(input("O ile chcesz podbić? "))
                        except ValueError:
                            print("Podaj liczbę całkowitą!")
                        if (podbicie > 0) and (podbicie <= zetony_gracza):
                            print(f"Podbijasz o {podbicie}.")
                            zetony_gracza -= podbicie
                            pula += podbicie
                            gracz2_reaguje_na_podbicie()
                            break
                        elif podbicie > zetony_gracza:
                            print("Nie możesz postawić więcej żetonów niż posiadasz!")
                            continue
                        elif podbicie <= 0:
                            print("Ilość musi być większa niż 0")
                            continue
                else:
                    print("Proszę o poprawną odpowiedź!")
                    continue
        elif ruch_gracza_2_w_licytacji[0] == "pasuj":
            gracz2_pasuje()
            pasuj = True
        elif ruch_gracza_2_w_licytacji[0] == "podbij":
            gracz2_podbija()
    else:
        ruch_gracza_2_w_licytacji = random.choices(
            ruchy_gracza_2_w_licytacji, weights=(45, 5, 55), k=1
        )
        if ruch_gracza_2_w_licytacji[0] == "czekaj":
            print("Grasz 2 czeka")
            while True:
                if pasuj == True:
                    break
                wybor = input("Co chciałbyś teraz zrobić? (czekaj/pasuj/podbij): ")
                if wybor.lower() == "czekaj":
                    print("Czekasz")
                    break
                elif wybor.lower() == "pasuj":
                    gracz_pasuje()
                    pasuj = True
                    break
                elif wybor.lower() == "podbij":
                    while True:
                        try:
                            podbicie = int(input("O ile chcesz podbić? "))
                        except ValueError:
                            print("Podaj liczbę całkowitą!")
                        if (podbicie > 0) and (podbicie <= zetony_gracza):
                            print(f"Podbijasz o {podbicie}.")
                            zetony_gracza -= podbicie
                            pula += podbicie
                            gracz2_reaguje_na_podbicie()
                            break
                        elif podbicie > zetony_gracza:
                            print("Nie możesz postawić więcej żetonów niż posiadasz!")
                            continue
                        elif podbicie <= 0:
                            print("Ilość musi być większa niż 0")
                            continue
                else:
                    print("Proszę o poprawną odpowiedź!")
                    continue
        elif ruch_gracza_2_w_licytacji[0] == "pasuj":
            gracz2_pasuje()
            pasuj = True
        elif ruch_gracza_2_w_licytacji[0] == "podbij":
            gracz2_podbija()


# Zabieranie pozostałych kart z rąk graczy z powrotem do talii
def czyszczenie_po_rundzie():
    global karty_gracza, karty_gracza2, talia, pasuj, karty_na_stole
    for karta in karty_gracza.copy():
        karty_gracza.remove(karta)
        talia.append(karta)
    for karta in karty_gracza2.copy():
        karty_gracza2.remove(karta)
        talia.append(karta)
    for karta in karty_na_stole.copy():
        karty_na_stole.remove(karta)
        talia.append(karta)
    pasuj = False


# Start rundy
def start_rundy():
    global pula, zetony_gracza, zetony_gracza2, licznik_rund, reszta_puli
    licznik_rund += 1
    print()
    print("Runda ", licznik_rund)
    print()
    print("Każdy gracz płaci 1 żeton za udział w rundzie.")
    zetony_gracza -= 1
    zetony_gracza2 -= 1
    pula = 2
    reszta_puli = 0


# Rozdawanie kart graczom
def pocket_cards():
    global karty_gracza, karty_gracza2
    for i in range(2):
        rozdaj_karte(karty_gracza)
        rozdaj_karte(karty_gracza2)


# Wyświetlenie kart gracza
def reka_gracza():
    global karty_gracza
    karty_do_wyswietlenia = ", ".join([slownik_kart[karta] for karta in karty_gracza])
    print("Twoje karty: " + karty_do_wyswietlenia)
    print()


# Czy kontynuować
def czy_kontynuowac():
    global koniec
    while True:
        print()
        wybor = input("Czy chcesz kontynuować? (tak/nie): ")
        if wybor.lower() == "tak":
            koniec = False
            break
        elif wybor.lower() == "nie":
            koniec = True
            break
        else:
            print("Niepoprawna odpowiedź! Wybierz 'tak' lub 'nie'.")


# Rozdawanie kart
def rozdaj_karte(karty_wybranego_gracza):
    global talia, karty_gracza, karty_gracza2, karty_na_stole
    losowa_karta = random.choice(talia)
    talia.remove(losowa_karta)
    karty_wybranego_gracza.append(losowa_karta)


# Start pierwszej rundy
def start():
    global pula, zetony_gracza, zetony_gracza2
    print("Witaj w grze Texas Holdem!")
    print()
    stawka = 100
    print(f"Każdy gracz o3muje {stawka} żetonów")
    zetony_gracza = stawka
    zetony_gracza2 = stawka


# Runda floop
def flop():
    global karty_na_stole, talia
    print()
    for i in range(3):
        rozdaj_karte(karty_na_stole)
    karty_do_wyswietlenia = ", ".join([slownik_kart[karta] for karta in karty_na_stole])
    print("Karty na stole: ", karty_do_wyswietlenia)
    karty_do_wyswietlenia = ", ".join([slownik_kart[karta] for karta in karty_gracza])
    print("Twoje karty: ", karty_do_wyswietlenia)
    print()


# Runda turn
def turn():
    global karty_na_stole, talia
    print()
    rozdaj_karte(karty_na_stole)
    karty_do_wyswietlenia = ", ".join([slownik_kart[karta] for karta in karty_na_stole])
    print("Karty na stole: ", karty_do_wyswietlenia)
    karty_do_wyswietlenia = ", ".join([slownik_kart[karta] for karta in karty_gracza])
    print("Twoje karty: ", karty_do_wyswietlenia)
    print()


# Runda river
def river():
    global karty_na_stole, talia
    print()
    rozdaj_karte(karty_na_stole)
    karty_do_wyswietlenia = ", ".join([slownik_kart[karta] for karta in karty_na_stole])
    print("Karty na stole: ", karty_do_wyswietlenia)
    karty_do_wyswietlenia = ", ".join([slownik_kart[karta] for karta in karty_gracza])
    print("Twoje karty: ", karty_do_wyswietlenia)
    print()


# Obliczanie kombinacji
def wyznaczanie_kombinacji(wybrana_reka):
    VALUES = "23456789TJQKA"
    ROYAL_FLUSH = 9
    STRAIGHT_FLUSH = 8
    FOUR_OF_A_KIND = 7
    FULL_HOUSE = 6
    FLUSH = 5
    STRAIGHT = 4
    THREE_OF_A_KIND = 3
    TWO_PAIR = 2
    PAIR = 1
    HIGH_CARD = 0

    values = sorted([VALUES.index(card[0]) for card in wybrana_reka])
    suits = [card[1] for card in wybrana_reka]
    set_values = sorted(set(values))

    flush = len(set(suits)) == 1
    straight = (
        (len(set(set_values)) == 7 and set_values[6] - set_values[2] == 4)
        or (len(set(set_values)) == 7 and set_values[5] - set_values[1] == 4)
        or (len(set(set_values)) == 7 and set_values[4] - set_values[0] == 4)
        or (len(set(set_values)) == 6 and set_values[5] - set_values[1] == 4)
        or (len(set(set_values)) == 6 and set_values[4] - set_values[0] == 4)
        or (len(set(set_values)) == 5 and set_values[4] - set_values[0] == 4)
    )
    pairs = [(values.count(value), value) for value in set(values)]
    pairs.sort(reverse=True)

    if straight and flush and values[7] == 12:
        return ROYAL_FLUSH, values[-1]
    elif straight and flush:
        return STRAIGHT_FLUSH, values[-1]
    elif pairs[0][0] == 4:
        return FOUR_OF_A_KIND, pairs[0][1]
    elif pairs[0][0] == 3 and pairs[1][0] == 2:
        return FULL_HOUSE, pairs[0][1], pairs[1][1]
    elif flush:
        return FLUSH, values[-1]
    elif straight:
        return STRAIGHT, values[-1]
    elif pairs[0][0] == 3:
        return THREE_OF_A_KIND, pairs[0][1], pairs[1][1]
    elif pairs[0][0] == 2 and pairs[1][0] == 2:
        return (
            TWO_PAIR,
            max(pairs[0][1], pairs[1][1]),
            min(pairs[0][1], pairs[1][1]),
            pairs[2][1],
        )
    elif pairs[0][0] == 2:
        return PAIR, pairs[0][1], pairs[1][1], pairs[2][1]
    else:
        return HIGH_CARD, values[-1], values[-2], values[-3], values[-4], values[-5]


# Porównywanie która kombinacja jest lepsza
def porównanie_kart(karty_gracza, karty_gracza2, karty_na_stole):
    wszystkie_karty_gracza = karty_gracza + karty_na_stole
    wszystkie_karty_gracza2 = karty_gracza2 + karty_na_stole
    wynik_gracza = wyznaczanie_kombinacji(wszystkie_karty_gracza)
    wynik_gracza2 = wyznaczanie_kombinacji(wszystkie_karty_gracza2)

    if wynik_gracza > wynik_gracza2:
        return 1
    elif wynik_gracza2 > wynik_gracza:
        return 2
    else:
        return 0


# Ujawnienie wyników
def porownanie_wynikow():
    global pula, zetony_gracza, zetony_gracza2, reszta_puli, karty_gracza, karty_gracza2, karty_na_stole
    print()
    print(f"Żetony w puli: {pula}")
    if reszta_puli > 0:
        print(f"Reszta puli: {reszta_puli}")
    print()
    karty_do_wyswietlenia = ", ".join([slownik_kart[karta] for karta in karty_na_stole])
    print("Karty na stole: ", karty_do_wyswietlenia)
    karty_do_wyswietlenia = ", ".join([slownik_kart[karta] for karta in karty_gracza])
    print("Twoje karty: ", karty_do_wyswietlenia)
    karty_do_wyswietlenia = ", ".join([slownik_kart[karta] for karta in karty_gracza2])
    print("Karty gracza 2: ", karty_do_wyswietlenia)

    print()
    wszystkie_karty_gracza_do_wyznaczania_kombinacji = karty_gracza + karty_na_stole
    wszystkie_karty_gracza2_do_wyznaczania_kombinacji = karty_gracza2 + karty_na_stole
    if (wyznaczanie_kombinacji(wszystkie_karty_gracza_do_wyznaczania_kombinacji)[0]) == 9:
        uklad_do_wyswietlenia = "POKER KRÓLEWSKI"
    elif (wyznaczanie_kombinacji(wszystkie_karty_gracza_do_wyznaczania_kombinacji)[0]) == 8:
        uklad_do_wyswietlenia = "Poker"
    elif (wyznaczanie_kombinacji(wszystkie_karty_gracza_do_wyznaczania_kombinacji)[0]) == 7:
        uklad_do_wyswietlenia = "Kareta"
    elif (wyznaczanie_kombinacji(wszystkie_karty_gracza_do_wyznaczania_kombinacji)[0]) == 6:
        uklad_do_wyswietlenia = "Ful"
    elif (wyznaczanie_kombinacji(wszystkie_karty_gracza_do_wyznaczania_kombinacji)[0]) == 5:
        uklad_do_wyswietlenia = "Kolor"
    elif (wyznaczanie_kombinacji(wszystkie_karty_gracza_do_wyznaczania_kombinacji)[0]) == 4:
        uklad_do_wyswietlenia = "Strit"
    elif (wyznaczanie_kombinacji(wszystkie_karty_gracza_do_wyznaczania_kombinacji)[0]) == 3:
        uklad_do_wyswietlenia = "Trójka"
    elif (wyznaczanie_kombinacji(wszystkie_karty_gracza_do_wyznaczania_kombinacji)[0]) == 2:
        uklad_do_wyswietlenia = "Dwie pary"
    elif (wyznaczanie_kombinacji(wszystkie_karty_gracza_do_wyznaczania_kombinacji)[0]) == 1:
        uklad_do_wyswietlenia = "Para"
    elif (wyznaczanie_kombinacji(wszystkie_karty_gracza_do_wyznaczania_kombinacji)[0]) == 0:
        uklad_do_wyswietlenia = "Wysoka karta"
    print("Twój najwyższy układ:", uklad_do_wyswietlenia)
    if (wyznaczanie_kombinacji(wszystkie_karty_gracza2_do_wyznaczania_kombinacji)[0]) == 9:
        uklad_do_wyswietlenia = "POKER KRÓLEWSKI"
    elif (wyznaczanie_kombinacji(wszystkie_karty_gracza2_do_wyznaczania_kombinacji)[0]) == 8:
        uklad_do_wyswietlenia = "Poker"
    elif (wyznaczanie_kombinacji(wszystkie_karty_gracza2_do_wyznaczania_kombinacji)[0]) == 7:
        uklad_do_wyswietlenia = "Kareta"
    elif (wyznaczanie_kombinacji(wszystkie_karty_gracza2_do_wyznaczania_kombinacji)[0]) == 6:
        uklad_do_wyswietlenia = "Ful"
    elif (wyznaczanie_kombinacji(wszystkie_karty_gracza2_do_wyznaczania_kombinacji)[0]) == 5:
        uklad_do_wyswietlenia = "Kolor"
    elif (wyznaczanie_kombinacji(wszystkie_karty_gracza2_do_wyznaczania_kombinacji)[0]) == 4:
        uklad_do_wyswietlenia = "Strit"
    elif (wyznaczanie_kombinacji(wszystkie_karty_gracza2_do_wyznaczania_kombinacji)[0]) == 3:
        uklad_do_wyswietlenia = "Trójka"
    elif (wyznaczanie_kombinacji(wszystkie_karty_gracza2_do_wyznaczania_kombinacji)[0]) == 2:
        uklad_do_wyswietlenia = "Dwie pary"
    elif (wyznaczanie_kombinacji(wszystkie_karty_gracza2_do_wyznaczania_kombinacji)[0]) == 1:
        uklad_do_wyswietlenia = "Para"
    elif (wyznaczanie_kombinacji(wszystkie_karty_gracza2_do_wyznaczania_kombinacji)[0]) == 0:
        uklad_do_wyswietlenia = "Wysoka karta"
    print("Najwyższy układ gracza 2:", uklad_do_wyswietlenia)

    print()
    if porównanie_kart(karty_gracza, karty_gracza2, karty_na_stole) == 1:
        print("Wygrałeś rundę. Gratulacje!")
        zetony_gracza += pula
        zetony_gracza += reszta_puli
        print(f"Otrzymujesz {pula} żetonów")
    elif porównanie_kart(karty_gracza, karty_gracza2, karty_na_stole) == 2:
        print("Przegrałeś rundę. Wygrywa gracz 2!")
        zetony_gracza2 += pula
        print(f"Gracz 2 otrzymuje {pula} żetonów")
    else:
        print("Remis!")
        pol_puli = pula / 2
        zetony_gracza += pol_puli
        zetony_gracza2 += pol_puli
        pula = 0

        zetony_gracza = int(zetony_gracza)
        zetony_gracza2 = int(zetony_gracza2)

    print(f"Twoje żetony: {zetony_gracza}")
    print(f"Żetony gracza 2: {zetony_gracza2}")


# Układ gry
def gra():
    start_rundy()
    statystyki()
    pocket_cards()
    reka_gracza()
    licytacja()
    if pasuj == False:
        statystyki()
        flop()
        licytacja()
        if pasuj == False:
            statystyki()
            turn()
            licytacja()
            if pasuj == False:
                statystyki()
                river()
                licytacja()
                if pasuj == False:
                    porownanie_wynikow()
    czyszczenie_po_rundzie()
    czy_kontynuowac()


# Główna pętla gry
def main():
    while True:
        start()
        while True:
            gra()
            if zetony_gracza == 0:
                print("Skończyły Ci się żetony. Przegrywasz!")
                break
            elif zetony_gracza2 == 0:
                print("Przeciwnikowi skończyły się żetony. Wygrywasz!")
                break
            if koniec == True:
                break
        break


# Program
main()
