

pripony = ["X","ný", "natý", "itý", "ičitý", "ičny/ečný", "ový", "istý", "ičelý"]   #list z priponami
skratky = ["Na", "Li", "K", "Be", "Mg", "Ca", "Ba", "Ti", "V", "Cr", "W", "Mn", "Fe", "Ni", "Cu", "Ag", "Au", "B", "Al", "Pb", "Si", "C", "P"]
nazvy = ["Sod", "Lít", "Drasel", "Beryl", "Horeč", "Váp", "Bár", "Titán", "Vanád", "Chróm", "Wolfrám", "Mangán", "Želez", "Nikel", "Meď", "Striebor", "Zlat", "Bór", "Hlin", "Olov", "Kremi", "Uhl", "Fosfor"]

user = input(
"""
Vzorec zadavajte vo formate: X(číslo)Y(číslo)
Názov zadávajte s diakritikou, zaciatočné písmena veľké.

Zadajte vzorec alebo názov: 
"""

)            #input vzorca/názvu




#vzorec na nazov
#pridavam priponu na prvok
def prvok_pripona(user):                    # funkcia pre pridanie pripony
  if len(user) == 6:
    cislo = user[-1]                        #zisti posledne cislo, podla toho vybera priponu z listu
    cislo = int(cislo)
    skratka = skratky.index(user[0:2])      #zistuje index skratky aby ten index nasielv nazvoch
    skratka = int(skratka)
    prvok = nazvy[skratka] + pripony[cislo] #finalny prvok; zoberie nazov z listu a najde index ktory je v liste (skratka ma taky isty index ako nazov) + prida priponu podla posledneho čísla
    print(prvok, end=" ")
  elif len(user) == 5:                      #ked ma vzorec len 5 pismen
    cislo2 = user[-1]                        
    cislo2 = int(cislo2)
    if user[0:2].isalpha():                 #musim detekovat ci su pismena, lebo vie oznacit aj cislo
      skratka = skratky.index(user[0:2])      
      skratka = int(skratka)
      prvok = nazvy[skratka] + pripony[cislo2]
      print(prvok, end=" ")
    elif user[0].isalpha():                 # ked neprejde hore, tak tu uz 100% viem ze skratka je prve pismeno
      cislo4 = user[-1]
      cislo4 = int(cislo4)
      skratka = skratky.index(user[0])      
      skratka = int(skratka)
      prvok = nazvy[skratka] + pripony[cislo4]
      print(prvok, end=" ")
  elif len(user) == 4:                      #ked ma vzorec 4 pismena
    cislo3 = user[-1]
    cislo3 = int(cislo3)
    skratka = skratky.index(user[0])      
    skratka = int(skratka)
    prvok = nazvy[skratka] + pripony[cislo3]
    print(prvok, end=" ")
#meniim halogenid na nazov
def halogenid(user):                        #funkcia pre pridanie halogenidu
  if len(user) == 6:
    if user[3:5] == "Cl":
      halog = "Chlorid"
      print(halog, end=" ")
    elif user[3:5] == "Br":
        halog4 = "Bromid"
        print((halog4), end=" ")
  elif len(user) == 5:                      # ked ma vzorec len 5 pismen 
    if user[3] == "F":
      halog2 = "Fluorid"
      print((halog2), end=" ")
    elif user[3] == "I":
      halog3 = "Iodit"
      print((halog3), end=" ")
    elif user[2:4] == "Cl":
      halog5 = "Chlorid"
      print((halog5), end=" ")
    elif user[2:4] == "Br":
      halog4 = "Bromid"
      print((halog4), end=" ")
  elif len(user) == 4:                       # ked ma vzorec len 4 pismena
    if user[2] == "F":
      halog2 = "Fluorid"
      print((halog2), end=" ")
    elif user[2] == "I":
      halog3 = "Iodit"
      print(halog3, end=" ")

#nazov na vzorec
#rozdelenie nazvu
def rozdelenie_nazvu(user):               #rozdelujem si nazov na dve slova
  hl_cislo_medzery = user.find(" ")       #rozdelujem dve slova podla medzery ktoru hladam
  global prvok_halog                      #deklarujem globalnu premennu lebo by inak bola len lokolna v danom def
  prvok_halog = user[:hl_cislo_medzery]   #do premennej prvok_halog zapisujem vsetky pismena od 0 az po medzeru
  global prvok_prvok                      #deklarujem globalnu premennu lebo by inak bola len lokolna v danom def
  hl_cislo_medzery += 1                   #pridavam +1 lebo nechcem mat v stringu medzeru  
  prvok_prvok = user[hl_cislo_medzery:]   #do premennej prvok_prvok zapisujem vsetky pismena medzery az po koniec

#vyroba z nazvu na prvok
def prvok_nazov(prvok_prvok):                           
  global proton                                         #urobim si globalnu premennu aby som ju potom mohol pouzit
  if prvok_prvok[-2:] == "ný":                          #kontrolujem posledne dve pismena pre string -ný
    proton = "1"                                        
    upraveny_prvok = prvok_prvok.replace("ný", "")      #vymazujem -ný lebo viem že to je prvý sklon
    skratka_index = nazvy.index(upraveny_prvok)         #zistujem index nazvu lebo viem ze nazov a skratka indexu su rovnake
    print(skratky[skratka_index] +"1", end="")          #vypisujem prvok
  elif prvok_prvok[-4:] == "natý":                      #a znova, kontrolujem pre posledne pismena
    proton = "2"
    upraveny_prvok = prvok_prvok.replace("natý", "")  
    skratka_index = nazvy.index(upraveny_prvok)
    print(skratky[skratka_index] +"1", end="")
  elif prvok_prvok[-2:] == "itý":
    proton = "3"
    upraveny_prvok = prvok_prvok.replace("itý", "")  
    skratka_index = nazvy.index(upraveny_prvok)
    print(skratky[skratka_index] +"1", end="")
  elif prvok_prvok[-5:] == "ičitý":
    proton = "4"
    upraveny_prvok = prvok_prvok.replace("ičitý", "")  
    skratka_index = nazvy.index(upraveny_prvok)
    print(skratky[skratka_index] +"1", end="")
  elif prvok_prvok [-9:] == "ičny/ečny":
    proton = "5"
    upraveny_prvok = prvok_prvok.replace("ičny/ečny", "")  
    skratka_index = nazvy.index(upraveny_prvok)
    print(skratky[skratka_index] +"1", end="")
  elif prvok_prvok[-3:] == "ový":
    proton = "6"
    upraveny_prvok = prvok_prvok.replace("ový", "")  
    skratka_index = nazvy.index(upraveny_prvok)
    print(skratky[skratka_index] +"1", end="")
  elif prvok_prvok[-4:] == "istý":
    proton = "7"
    upraveny_prvok = prvok_prvok.replace("istý", "")  
    skratka_index = nazvy.index(upraveny_prvok)
    print(skratky[skratka_index] +"1", end="")
  elif prvok_prvok[-5:] == "ičelý":
    proton = "8"
    upraveny_prvok = prvok_prvok.replace("ičelý", "")  
    skratka_index = nazvy.index(upraveny_prvok)
    print(skratky[skratka_index] +"1", end="")
#vyroba z nazvu halogenidu na skratku
def halogenid2(prvok_halog, proton):
  if prvok_halog == "Chlorid":                              #zitujem ci sa rozdeleny nazov rovna danemu stringu
    upraveny_user = prvok_halog.replace("Chlorid", "Cl")    #zamienam string na skratku
    print(upraveny_user + proton)                           #vypisujem skratku s protonom alisa globalnou premennou
  elif prvok_halog == "Bromid":                             # a to iste stale
    upraveny_user2 = prvok_halog.replace("Bromid", "Br")
    print(upraveny_user2 + proton)
  elif prvok_halog == "Fluorid":
    upraveny_user3 = prvok_halog.replace("Fluorid", "F")
    print(upraveny_user3 + proton)
  elif prvok_halog == "Iodid":
    upraveny_user4 = prvok_halog.replace("Iodid","I")
    print(upraveny_user4 + proton)
    
    

proton = ""

rozdelenie_nazvu(user)
halogenid(user)
prvok_pripona(user)
prvok_nazov(prvok_prvok)
halogenid2(prvok_halog, proton)