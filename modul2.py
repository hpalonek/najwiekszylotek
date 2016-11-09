#! /usr/bin/env python
# -*- coding: utf-8 -*-

import random
import os

def ustawienia():
	nick = raw_input('podaj nick ')
	nazwapliku = nick + '.ini'
	gracz = czytaj_ust(nazwapliku)
	if gracz:
		print "Twoje ustawienia:"
		print "Liczb:", gracz[1]
		print "Z Maks:", gracz[2]
		print "Losowań:", gracz[3]
		odp = raw_input("Zmieniasz (t/n)? ")

	if not gracz or odp.lower() == 't':
		while 1:
			try:
				ileliczb = int(raw_input('ile liczb chcesz losować? '))
				maxliczb = int(raw_input('jaka ma być maksymalna losowana liczba? '))
				ilelos = int(raw_input('ile razy chcesz typowac? '))
				if ileliczb>maxliczb:
					print 'bledne dane'
					continue
				break
				
			except:
				print 'bledne dane'
				continue
		gracz = zapisz_ust(nazwapliku, [nick, str(ileliczb), str(maxliczb), str(ilelos)])

	return gracz[0:1] + map(lambda x: int(x), gracz[1:4])

	#print 'ustaliles ze chcesz losować', ileliczb, ' liczby ', 'a maksymalna liczba to ', maxliczb

def czytaj_ust(nazwapliku):
	if os.path.isfile(nazwapliku):
		plik = open(nazwapliku, "r")
		linia = plik.readline()
		if linia:
			return linia.split(";")
		return False

def zapisz_ust(nazwapliku, gracz):
	plik = open(nazwapliku, 'w')
	plik.write(';'.join(gracz))
	plik.close()
	return gracz


def losowanie(ileliczb, maxliczb):
	liczby = []
	i = 0
	while i < ileliczb:
		liczba = random.randint(0, maxliczb)
	
		if liczby.count(liczba)==0:
			liczby.append(liczba);
			i=i+1
	return liczby


def typowanie(ileliczb, maxliczb):
	print "Wytypuj", ileliczb, "z", maxliczb, "liczb:"

	typy = set()
	i = 0
	while i < ileliczb:
		try:
			typ = int(raw_input('wytypuj liczbę '  + str(i + 1) + ': '))
	
		except ValueError:
			print 'bledne dane'
			continue
		if 0<typ<maxliczb and typ not in typy:
			typy.add(typ)
			i = i + 1
		else:
			print 'cos nie tak jeszcz raz'
			continue
	return typy

def wyniki(liczby, typy):
	trafione = set(liczby) & typy

	print 'wytypowales', typy
	print 'trafione', trafione
	print 'trafiles', len(trafione), 'razy'

	#print 'wylosowano', liczby

	return len(trafione)

