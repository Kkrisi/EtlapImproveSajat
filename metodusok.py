
import time



# ------ Üdvözlő szöveg ------

def Felirat1():
	felirat = """
																									   
	\ \        /    |                            __ __|                                  
	 \ \  \   / _ \ |  __|  _ \  __ `__ \   _ \     |  _` | __ \   _` |  __| __ \   _ \  
	  \ \  \ /  __/ | (    (   | |   |   |  __/     | (   | |   | (   | |    |   | (   | 
	   \_/\_/ \___|_|\___|\___/ _|  _|  _|\___|    _|\__,_|_|  _|\__,_|_|   _|  _|\___/  
			"""
	print(f"{felirat}\n\n")







# ------ "Rendelés tölt" szöveg ------

def Felirat2():
	felirat = """
																										   
	 |                     |_)              _)  / 
	 |      _ \   _` |  _` | | __ \   _` |     /  
	 |     (   | (   | (   | | |   | (   |    /   
	_____|\___/ \__,_|\__,_|_|_|  _|\__, |  _/ _) 
					|___/       

			"""
	print(f"{felirat}\n\n")











# ------ Étlapmenü szélesség megállapítása ------

def EtlapSzelesseg(etlap):
	jel = "*"
	csillagsor = 0
	for etelTipus in etlap:
		for etel in etelTipus:
			if len(etel) > csillagsor:
				csillagsor = len(etel)
	return csillagsor+17, jel









# ----- Választott étel bekérése -----

def Kerdesek(felirat):

	while True:
		try:
			valasztott = int(input(f"Kérem gépelje be a választott étel számát: \nEllenben ha kihagyná a {felirat} választását,\n nyomjon egy 'Entert': "))
		except ValueError:
			print("\nKérlek a megadott számok közül válassz! :)\n")
			continue
		if valasztott >= 0 and valasztott <= 4:
			break
		else:
			print("\nA beírt számnak 1-4 között kell lennie! :)\n")

	return valasztott












# ------ Étel/ár megjelnítés ------

def EtelValasztas(etlap, etlapAr, etlapCim):

	EtlapSzelesseg(etlap)
	csillagsor, jel = EtlapSzelesseg(etlap)[0], EtlapSzelesseg(etlap)[1]
	valasztottLista, vegOsszeg = [], 0

	for etelTipus, etelAr, felirat in zip(etlap, etlapAr, etlapCim):
		cimsor = jel*round(((csillagsor-len(felirat))/2))
		print(f"\n\n{cimsor} {felirat.upper():^} {cimsor}")

		for etel, ar in zip(etelTipus,etelAr):
			print(f"{jel} {etelTipus.index(etel)+1}. {etel:<{csillagsor-(len(str(ar)))-8}}{ar} Ft {jel}")
		print(f"{jel*(csillagsor+2)}")

		sorszam = Kerdesek(felirat)-1
		if sorszam == -1:
			pass
		else:
			valasztottLista.append(etelTipus[sorszam])
			vegOsszeg += etelAr[sorszam]

	return valasztottLista, vegOsszeg











# ------ Nyugta megjelnítés ------

def MegrendelésPluszNyugta(etlap, etlapAr, etlapCim):
	EtlapSzelesseg(etlap)
	csillagsor, jel = EtlapSzelesseg(etlap)[0], EtlapSzelesseg(etlap)[1]

	Felirat1()
	time.sleep(2)
	valasztottEtel, osszeg =  EtelValasztas(etlap, etlapAr, etlapCim)
	Felirat2()
	time.sleep(3)

	felirat = "Megrendelt"
	cimsor = jel*round(((csillagsor-len(felirat))/2))

	print(f"\n\n{cimsor} {felirat.upper():^} {cimsor}")

	for etel in valasztottEtel:
		print(f"{jel} -- {etel:<{csillagsor-4}}{jel}")

	szervizdij = round(osszeg*0.1)
	print(f"{jel*(csillagsor+2)}\n\n    Összeg: {osszeg} Ft\n    +szervízdíj: {szervizdij} Ft\n\n Végösszeg: {osszeg+szervizdij} Ft")

	



	






