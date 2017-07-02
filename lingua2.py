# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 16:43:17 2017

@author: Win 7
"""

lavica = 0
tigrica = 0

sve reči=set()

korpus = "Juče sam bio u zoo vrtu. Video sam tri lava i bila je tu jedna lavica. Lavica nije imala grivu, jer to imaju samo muški lavovi. Bila je u zoo vrtu i jedna tigrica. Ona je imala jako lepo krzno. Bilo mi je žao što tigrica i lavica ne mogu da se druže, jer mislim da bi se baš lepo slagale pošto su obe mačke."

tokeniziraniKorpus = korpus.split(" ") #podela korpusa na listu reči

for reč in tokeniziraniKorpus: #
    # prebacivanje reči u mala slova
    reč = reč.lower() 
    # uklanjanje interpunkcijskih znakova
    reč = reč.strip(",.") # komanda strip, stavimo sve simbole koje želimo da uklonimo SA DESNE STRANE REČI
    if reč == "lavica": 
        lavica += 1 # lavica = lavica + 1    
    elif reč == "tigrica":
        tigrica += 1 # tigrica = tigrica + 


        

print("Broj javljanja reči lavica:", lavica)
print("Broj javljanja reči tigrica:", tigrica)




# Korekcija:
    
lavica = 0
tigrica = 0

sve_reči = set() #u skupu se svaki element može naći samo jednom

korpus = "Juče sam bio u zoo vrtu. Video sam tri lava i bila je tu jedna lavica. Lavica nije imala grivu, jer to imaju samo muški lavovi. Bila je u zoo vrtu i jedna tigrica. Ona je imala jako lepo krzno. Bilo mi je žao što tigrica i lavica ne mogu da se druže, jer mislim da bi se baš lepo slagale pošto su obe mačke."

tokeniziraniKorpus = korpus.split(" ") 

for reč in tokeniziraniKorpus: 
    reč = reč.lower() 
    reč = reč.strip(",.") 
    
    # reč treba dodati nakon uklanjanja nepotrebnih karaktera
    sve_reči.add(reč)
    
    if reč == "lavica": 
        lavica += 1    
        
    elif reč == "tigrica":
        tigrica += 1 
        
print(len(sve_reči))

print("Broj javljanja reči lavica:", lavica)
print("Broj javljanja reči tigrica:", tigrica)

