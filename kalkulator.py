#definicje działań
def dodawanie(a, b):
    print(f"Dodaję {a} i {b}")
    wynikus = a + b
    dodatkowa = False
    c = 0
    while (dodatkowa == 0):
        print("Możesz dodać jeszcze jakąś liczbe: ['0' = wyjście]")
        cc = input("Podaj składnik ")
        if czy_liczba(cc) and cc != '0':
            c = float(cc)
            wynikus += c
            dodatkowa = 0
        else:
            print(f"{cc} nie jest liczbą")
            break

    return(wynikus)

def odejmowanie(a, b):
    print(f"Odejmuję {a} od {b}")
    return(a-b)

def mnozenie(a, b):
    print(f"Mnożę {a} i {b}")
    return(a*b)

def dzielenie(a, b):
    if b == 0:
        print(f"Pamiętaj ... nie dziel przez zero")
        exit()
    else:
        print(f"Dzielę {a} przez {b}")
        wyndz = ("{:.2f}".format(a/b))
        return(wyndz)
   
def czy_liczba(c):
    try:
        float(c)
        return True
    except ValueError:
        return False


#start programu
wynik = 0
dzialanie = input("Podaj działanie, posługując się odpowiednią liczbą: "
"1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")

#czy poprawnie podano nr działania
if (dzialanie != '1' and dzialanie != '2' and dzialanie != '3' and dzialanie != '4'):
    print(f"Nie ma przypisanego działania do podanych wartości!!")
    exit()

#Podanie 1 wartości    
aa = input("Podaj składnik ")
if czy_liczba(aa):
    a = float(aa)
else:
    print(f"{aa} nie jest liczbą")
    exit()

#Podanie 2 wartości
bb = input("Podaj składnik ")
if czy_liczba(bb):
    b = float(bb)
else:
    print(f"{bb} nie jest liczbą")
    exit()

#Działania
if (dzialanie == '1'):
    wynik = dodawanie(a, b)
elif (dzialanie == '2'):
    wynik = odejmowanie(a, b)
elif (dzialanie == '3'):
    wynik = mnozenie(a, b)
elif (dzialanie == '4'):
    wynik = dzielenie(a, b)

print(f"Wynik to {wynik}")
