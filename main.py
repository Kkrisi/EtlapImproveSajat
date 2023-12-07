# pip install colorama
import colorama
from colorama import Fore, Back, Style
import metodusok
import time

colorama.init()

#print(Fore.RED + 'some red text')
#print(Back.WHITE + 'and with a green background')








# ------ Étel/ital választék és áraik ------

eloEtel = ["Burgonyás tallérok", "Libatepertő krém", "Kínaikel saláta almával", "Szezámmagos pulykaérmék salátával"]
eloEtelAr = [900, 600, 1100, 1300]

foEtel = ["Zöldborsófőzelék, kukoricabundás csirkecsíkok", "Rántott sertés máj, rizi-bizi", "Szezámmagos rakott bulgur pulykahússal", "Sertéssült, baconos, parmezános kelbimbó"]
foEtelAr = [1495, 1195, 1395, 1895]

desszert = ["Karamella puding ribizlivel", "Madártej", "Aranygaluska, vanília öntet", "Eszterházy szelet"]
desszertAr = [590, 690, 790, 790]

ital = ["Rostos kajszibaracklé", "Pepsi Lime Cola", "Ásványvíz", "Szamóca szörp"]
italAr = [579, 620, 280, 450]


etlap = [eloEtel,foEtel,desszert,ital]
etlapAr = [eloEtelAr, foEtelAr, desszertAr, italAr]
etlapCím = ["Előételek", "Főételek", "Desszertek", "Italok"]








# ------ Rendelés leadása ------

metodusok.Udvozles()
time.sleep(1) #4re állítani!!!!

metodusok.EtlapSzelesseg(etlap)
metodusok.EtelValasztas(etlap, etlapAr,etlapCím)









# ------ Fizetés és távozás ------

#metodusok.Nyugta()








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















