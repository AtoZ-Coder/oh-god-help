pripony = ["X","ný", "natý", "itý", "ičitý", "ičny/ečný", "ový", "istý", "ičelý"]   #list z priponami
skratky = ["Na", "Li", "K", "Be", "Mg", "Ca", "Ba", "Ti", "V", "Cr", "W", "Mn", "Fe", "Ni", "Cu", "Ag", "Au", "B", "Al", "Pb", "Si", "C", "P"]
nazvy = ["Sod", "Lít", "Drasel", "Beryl", "Horeč", "Váp", "Bár", "Titán", "Vanád", "Chróm", "Wolfrám", "Mangán", "Želez", "Nikel", "Meď", "Striebor", "Zlat", "Bór", "Hlin", "Olov", "Kremi", "Uhl", "Fosfor"]
cisla = []
prvky = {"Na":"Sod", "Li":"Lít", "K":"Drasel", "Be":"Beryl", "Mg":"Horeč", "Ca":"Váp", "Ba":"Bár", "Ti":"Titán", "V":"Vanád", "Cr":"Chróm", "W":"Wolfrám", "Mn":"Mangán", "Fe":"Želez", "Ni":"Nikel", "Cu":"Meď", "Ag":"Striebor", "Au":"Zlat", "B":"Bór", "Al":"Hlin", "Pb":"Olov", "Si":"Krem", "C":"Uhl", "P":"Fosfor", "F":"Fluór", "Cl":"Chlór", "Br":"Bróm", "I":"Jód" }
user = input(
"""
Vzorec zadavajte vo formate: X(číslo)Y(číslo)
Názov zadávajte s diakritikou, zaciatočné písmena veľké.

Zadajte vzorec alebo názov: 
"""

)            #input vzorca/názvu

#vzorec na nazov
def vzorec_na_nazov():
    for i in range(len(user)):
        if user[i].isnumeric() == True:
            cisla.append(user[i])
            if cisla[0] == "1":
                #vieme ze je to halogenid
                dlzka = len(user)
                dlzka = int(dlzka/2)
                
                nazov = prvky.get()
            elif cisla[0] == "2":
                #vieme, ze to je oxid
                print("je to oxid")
            else:
                print("help")                



vzorec_na_nazov()
