# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 17:14:55 2017

@author: Win 7
"""

brojPriloga = 0
prilozi = ["ovde", "tamo", "tu", "desno", "negde"]
korpus = "Ovde mi je baš lepo. Džunglu ne volim. Ne bih volela da sam tamo. Moje mesto je tu. Tu se osećam kao da sam kod kuće. Stavila sam svoju šoljicu kafe desno, e baš tu."

tokeniziraniKorpus = korpus.split(" ")

for reč in tokeniziraniKorpus:
    # prebacivanje reči u mala slova
    reč = reč.lower()
    # uklanjanje interpunkcijskih znaka
    reč = reč.strip(",.")
    if reč in prilozi: # MOŽE I: if (reč=="ovde") or (reč=="tamo") or (reč=="tu") or (reč=="desno") or ....
        brojPriloga += 1 # brojPriloga = brojPriloga + 1

print(brojPriloga)


# Korekcije:
    
    
