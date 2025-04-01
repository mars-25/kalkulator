import logging

# Konfiguracja loggingu
logging.basicConfig(level=logging.INFO, format='%(message)s')

# Definicje działań
def dodawanie(a, b):
    logging.info(f"Dodaję {a} i {b}")
    return a + b

def odejmowanie(a, b):
    logging.info(f"Odejmuję {b} od {a}")
    return a - b

def mnozenie(a, b):
    logging.info(f"Mnożę {a} i {b}")
    return a * b

def dzielenie(a, b):
    if b == 0:
        logging.error(f"Pamiętaj ... nie dziel przez zero!")
        return None  # Zwracamy None dla błędu dzielenia przez zero
    else:
        logging.info(f"Dzielę {a} przez {b}")
        return round(a / b, 2)

# Funkcja do pobierania liczb od użytkownika
def pobor_liczb():
    a = float(input("Podaj składnik 1: "))
    b = float(input("Podaj składnik 2: "))
    return a, b

# Słownik działań
kalkulator = {
    1: dodawanie,
    2: odejmowanie,
    3: mnozenie,
    4: dzielenie
}

# Główna część programu
if __name__ == "__main__":
    logging.info("Uruchamianie kalkulatora...")  # Informacja na starcie programu

    # Pobranie działania od użytkownika
    try:
        dzialanie = int(input("Podaj działanie, posługując się odpowiednią liczbą: "
                              "1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
    except ValueError:
        logging.error("Podano niepoprawny numer działania!")
        exit()

    # Sprawdzenie, czy działanie znajduje się w słowniku
    if dzialanie in kalkulator:
        a, b = pobor_liczb()  # Pobranie składników
        funkcja = kalkulator[dzialanie]  # Pobranie odpowiedniej funkcji
        wynik = funkcja(a, b)  # Wykonanie obliczenia
        if wynik is not None:
            logging.info(f"Wynik działania: {wynik}")
            print(f"Wynik to: {wynik}")
        else:
            logging.warning("Nie można wykonać obliczenia.")
    else:
        logging.error("Wybrano niepoprawne działanie!")
        print("Niepoprawny wybór działania!")