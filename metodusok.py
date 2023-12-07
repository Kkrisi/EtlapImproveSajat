




# ------ Üdvözlő szöveg ------

def Udvozles():
	felirat = """
							                                                                           
	\ \        /    |                            __ __|                                  
	 \ \  \   / _ \ |  __|  _ \  __ `__ \   _ \     |  _` | __ \   _` |  __| __ \   _ \  
	  \ \  \ /  __/ | (    (   | |   |   |  __/     | (   | |   | (   | |    |   | (   | 
	   \_/\_/ \___|_|\___|\___/ _|  _|  _|\___|    _|\__,_|_|  _|\__,_|_|   _|  _|\___/  
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






def Kerdesek(felirat):
	valasztott = int(input(f"Kérem gépelje be a választott étel számát: \nEllenben ha kihagyná a {felirat} választást,\n nyomjon egy 'Entert': "))








# ------ Étel/ár megjelnítés ------

def EtelValasztas(etlap, etlapAr, etlapCim):
	csillagsor, jel = EtlapSzelesseg(etlap)[0], EtlapSzelesseg(etlap)[1]
	for etelTipus, etelAr, felirat in zip(etlap, etlapAr, etlapCim):
		cimsor = jel*round(((csillagsor-len(felirat))/2))
		print(f"{cimsor} {felirat.upper():^} {cimsor}")

		for etel, ar in zip(etelTipus,etelAr):
			print(f"{jel} {etel:<{csillagsor-(len(str(ar)))-5}}{ar} Ft {jel}")
		print(f"{jel*(csillagsor+2)}\n")
		Kerdesek(felirat)











'''

#ETLAP
def EtlapMegjelenit(lista, listaAr, szoveg):
	etlap.jelsor("*", etlap_meret)
	etlap.cimsor("*",szoveg,"*", etlap_meret)

	for i in range(len(lista)):	
		etlap.szoveg_ar(lista[i], str(listaAr[i])+" Ft", etlap_meret)
	etlap.jelsor("=", etlap_meret)


EtlapMegjelenit(etelekNev, etelekAr, "Főételek")
EtlapMegjelenit(dessertNev, dessertAr, "Desszertek")


#RENDELÉS/SZÁMOLÁS

import modulok

modulok.rendeles(halar,husar,fagyiar,browniear,etlap_meret)
'''






#def Nyugta():
	# penznem valasztas
	# jatt % adás
	# Köszönjuk hogy nalunk evett
	#return alma


















