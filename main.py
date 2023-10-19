print("zadanie 1")
print("a)")
def ciagA(n):
    if n == 1:
        return 4
    else:
        return print(n, ' wyraz ciagu: ', 4 + (3 * (n - 1)))
ciagA(5)
print("b)")
def ciagB(n):
    if n == 1:
        return 2
    else:
        return print(n, ' wyraz ciagu: ',   2** (n))
ciagB(5)

print("c)")
def ciagC(n):
    if n == 1:
        return 2
    else:
        return print(n, ' wyraz ciagu: ', 2 * ((-3) ** (n-1)))
ciagC(5)
print("d)")
def ciagD(n):
    if n == 1:
        return 10
    else:
        return print(n, ' wyraz ciagu: ', -10 * ((-0.5)) ** (n - 1))
ciagD(5)

print("zadanie 2")


def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n-1)

def newton(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return silnia(n) // (silnia(k) * silnia(n-k))
n = int(input("n: "))
k = int(input("k: "))
if k <= 0 or n <= k:
    print("złe dane!")
else:
    wynik = newton(n, k)
    print(f"Wynikiem jest {wynik}")

print("zadanie 3")
print("a)")
lista = [1,2,3,4,5,6,7,8,9,10,15,20,-2,5]
def wypisz(lista):
    for element in lista:
        print(element)

wypisz(lista)
print("b)")
def przez_p(lista):
    licznik = 0
    for element in range(len(lista)):
        if element % 5 != 0:
            licznik += 1
    return licznik
print(przez_p(lista), "elementow jest niepodzielne przez 5")
print("c)")
def funkcja(lista2):
    for i, elem in enumerate(lista2):
        if 3 <= i <= 8 and i % 2 != 0:
            lista2[i] += 2
    print(lista2)
lista2 = [1,2,3,4,5,6,7,8,9]
funkcja(lista2)
print("d)")
def ujemne(lista):
    for element in lista:
        if element < 0:
            return False
        else:
            return True
if ujemne(lista) == True:
    print("w liście nie ma elementu ujemnego")
else:
    print("w liście jest element ujemny")
print("e)")
def razy_p(lista):
    iloczyn = 1
    for element in lista:
        if element == 5:
            iloczyn *= element
    return iloczyn
print("iloczyn 5 w liście to:", razy_p(lista))
print("f)")
def czy_w_liscie(lista):
    for element in lista:
        if not 5 <= element <= 8:
            return True
        else:
            return False
listabez = [6,7]
if czy_w_liscie(lista) == True:
    print("w liście są liczby poza przedziałem 5 - 8")
else:
    print("w liście nie ma liczb poza przedziałem 5 - 8")

print("zadanie 4")
tabdwym = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]]
tabdwym2 = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]]
print("a)")
def wypis(tabdwym):
    for rzad in tabdwym:
        print(rzad)
wypis(tabdwym)
print("b)")
def zamiana(tabdwym2, kol1, kol2):
    for rzad in tabdwym2:
        rzad[kol1], rzad[kol2] = rzad[kol2], rzad[kol1]
zamiana(tabdwym2, 0, 1)
wypis(tabdwym2)
print("c)")
def zamiana2(tabdwym, rzad1, rzad2):
    tabdwym[rzad1], tabdwym[rzad2] = tabdwym[rzad2], tabdwym[rzad1]
print("kolumny do zamiany:")
x = int(input("Podaj wartosc 1: "))
y = int(input("Podaj wartosc 2: "))
zamiana(tabdwym, x, y)
wypis(tabdwym)


print("zadanie 6")
tab6 = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]]
print("a)")
def wypis(tab6):
    for rzad in tab6:
        print(rzad)
wypis(tab6)
print("b)")

def ilo_pon_p(tab6):
    iloczyn = 1
    for rzad in tab6:
        for element in rzad:
            if element > 5:
                iloczyn *= element
    return iloczyn
print("Iloczyn liczb ponad 5:", ilo_pon_p(tab6))
print("c)")
def nie_zilch(tab6):
    licznik = 0
    for rzad in tab6:
        for element in rzad:
            if element != 0:
                licznik += 1
    return licznik
print("liczba liczb nie bedacych 0:", nie_zilch(tab6))