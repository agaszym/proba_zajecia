def dysjunkcja(wartosc_pierwsza, wartosc_druga):
    wynik = int()
    if wartosc_pierwsza == wartosc_druga:
        return "False"
    else:
        return "True"

for i in range(4):
    print("Podaj wartość pierwszego elementu (1 = True, 0 = False).")
    wartosc_pierwsza = int(input())
    print("Podaj wartość drugiego elementu (1 = True, 0 = False).")
    wartosc_druga = int(input())
    wynik = dysjunkcja(wartosc_pierwsza, wartosc_druga)
    print("Podane elementy złączone spójnikiem dysjunkcji tworzą zdanie o wartości:", wynik)
