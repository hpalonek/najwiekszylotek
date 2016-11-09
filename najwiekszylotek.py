#! /usr/bin/env python
# -*- coding: utf-8 -*-

from modul2 import ustawienia, losowanie, typowanie, wyniki

# program główny

# ustalamy trudność gry
nick, ileliczb, maksliczba, ilerazy = ustawienia()

print ileliczb
# losujemy liczby
liczby = losowanie(ileliczb, maksliczba)

# trzy razy pobieramy typy użytkownika i sprawdzamy, ile liczb trafił
for i in range(ilerazy):
    typy = typowanie(ileliczb, maksliczba)
    wyniki(liczby, typy)

print "Wylosowane liczby:", liczby