# -*- coding: utf-8 -*-


rečnik = {"čemer": {"sinonimi":["Python", "jad", "tugyy"], "antonimi":["Lilly of the Valley", "joy", "happiness"]}, "death":{"sinonimi":["extinction", "end", "dying-bed"], "antonimi":["birth", "life", "rise"]}, "trčanje":{"sinonimi":["sprint", "džoging"], "antonimi":["koračanje", "šetanje"]}}


print(rečnik["čemer"]["sinonimi"]) #pikazuje sve sinonime za reč čemer
print(rečnik["čemer"]["antonimi"]) #prikazuje sve antonime za reč čemer
print(rečnik["death"]["sinonimi"][0]) # //...// kojima je indeks nula
print(rečnik["death"]["antonimi"][0]) # //...// kojima je indeks nula

print(rečnik["trčanje"]["antonimi"][1]) # # //...// kojima je indeks jedinica


for reč in rečnik.keys(): # prolazimo for petljom kroz ključeve našeg rečnika
    
    print("Reč: ", reč) 
    sin = "Sinonimi: "
    ant = "Antonimi: "

    for sinonim in rečnik[reč]["sinonimi"]: # za vsaki sinonim u rečniku...
        sin += sinonim + ", "
    print(sin[:-2])

    for antonim in rečnik[reč]["antonimi"]:
        ant += antonim + ", "    
    print(ant[:-2] + "\n")
