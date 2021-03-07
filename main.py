import sys as system
import math

# Zad 1.Napisz skrypt, w którym tworzysz listę z ulubionymi filmami, a następnie odwróć całą listę.
# Po odwróceniu listy dodaj kilka pozycji (dodane pozycje mają zostać dodane od 5 indeksu, cała lista mam zawierać 10 pozycji)

print("zadanie 1:\n")
Filmy = ["Film1", "Film2", "Film3", "Film4"]
Filmy.reverse()
Filmy.append("Film5")
Filmy.append("Film6")
Filmy.append("Film7")
Filmy.append("Film8")
Filmy.append("Film9")
Filmy.append("Film10")
print(Filmy)
print("\n")

# Zad 2. Stwórz skrypt, w którym utworzysz słownik z filmami z zadania 1. Pomyśl co może być kluczem

print("zadanie 2:\n")
slownik = {"Film-1" : "Film1", "Film-2" : "Film2", "Film-3" : "Film3", "Film-4" : "Film4", "Film-5" : "Film5", "Film-6" : "Film6", "Film-7" : "Film7", "Film-8" : "Film8", "Film-9" : "Film9", "Film-10" : "Film10"}
print(slownik)
print("\n")

# Zad 3. Stwórz skrypt, gdzie utworzysz słownik z nazwami przedmiotów z obecnego semestru oraz ich skrótami. Policz liczbę elementów w słownik

print("zadanie 3:\n")
slownik_przedmioty = {"KWP" : "komputerowe wspomaganie programowania", "WD" : "Wizualizacja Danych", "RRiC" : "Rachunek różniczkowy i całkowy", "PS" : "Programowanie Strukturalne", "EMD" : "Elementy matematyki dyskretnej"}
print(len(slownik_przedmioty))
print("\n")

# Zad 4. Napisz skrypt gdzie wczytasz liczbę dowolnego typu i podnieś ją do tej samej potęgi. Użyj funkcji input.

print("zadanie 4:\n")
liczba = input("Wpisz liczbe: ")
liczba2 = int(liczba)**int(liczba)
print(liczba2)
print("\n")

# Zad 5. Napisz skrypt gdzie wczytasz dowolny ciąg znaków, i policzysz wystąpienie litery a. Użyj instrukcji readline() i write()).

print("zadanie 5:\n")
system.stdout.write("Wpisz dowolne słowo: ")
string1 = system.stdin.readline()
print(string1.count("a"))
print("\n")

# Zad 6. Wczytaj trzy liczby całkowite a,b,c i sprawdź czy liczba a jest parzysta oraz czy jednocześnie b>c 

print("zadanie 6:\n")
print("Wpisz 3 liczby: \n")
a = input()
b = input()
c = input()
reszta = int(a)%2
if (reszta==1):
    print("a nie jest parzyste")
else:
    print("a jest parzyste")
if (b>c):
    print("b jest większe od c")
else:
    print("b nie jest większe od c")

# Zad 7. Napisz skrypt, gdzie stworzysz listę składającą się z liczb typu int i float. Następnie za pomocą pętli for oblicz sumę elementu obecnego z poprzednim.


# Zad 8. Napisz skrypt, który za pomocą pętli while pobiera 10 liczb, a następnie dodaje do listy tylko liczby całkowite

print("zadanie 8:\n")
calkowite = []
i = 0
print("Wpisz 10 liczb: \n")
while i < 10:
    a = input()
    a = int(a)
    if a%1==0:
        calkowite.append(a)
    i+=1
print(calkowite)
print("\n")

# Zad 9. Napisz skrypt, który rysuje następującą literę

#OOOOOO
#O    O
#O    O
#O    O
#O    O
#OOOOOO

lista = [1,2,3,4,5,6]
i = 1
for i in range(6):
   if lista[i] % 5 == 1:
       print("000000")
   if lista[i] % 5 != 1:
       print("O    O")

# Zad 10. Napisz skrypt, w którym użytkownik ma podać liczbę i który będzie wyłapywał błąd gdy użytkownik poda literę zamiast cyfry.

print("zadanie 10:\n")
i = input("Podaj liczbe i: \n")
if i.isalpha()==True:
    print("Błąd, nie jest liczbą!")
else:
    print("OK!")