# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 23:30:14 2017

@author: Win 7
"""

"""
DOMAĆI ZADATAK 1:
Izmenite priču tako što ćete poslednju rečenicu obrisati i umesto nje dodati
vaših nekoliko rečenica kojima ćete promeniti ishod priče.
Nakon toga podelite priču na rečenice funkcijom .split() (Hint: Razmislite koji
kriterijum za razdvajanje vam je sada potreban umesto dosadašnjeg " "). i
funkcijom len() proverite koliko rečenica sada ima priči.
"""




story = "I odjednom žaba poče da govori: \"Once Upon a Time.. in an old, but beautiful Kingdom, called Petnica, lived a witch, also beautiful, who not so beautyfully treated everyone. She tortured 'em with such a thing that no one could ever speak of. Python. PYTHON. What a monsterous... name for.. a... MONSTER! But there was a knight. A knight willing to fight. Well, this one IS a lie. He was a boy. (And she was a witch. Can I make it anymore.. HELL, NEVERMIND)  He was just a boy who had accidentally found a long lost sword in the stone. You may think it was the Excalibur, but no.  That is another story, the one I cannot tell you now. IT'S BLOODY 3 AM.  The Rock said C# and that's what the boy said. Anyway, the boy decided to take out the sword and he failed.  After failing, he just took the bloody rock. Long story short, dozen of obstacles later, a thousands of mega bytes to be exact, the boy found a witch in her tower, and threw the rock at her. After two months in hospital called Trash Bin, she woke up, realized what she'd done and made up her mind letting every single soul to do the C#. She even got her fairy wings. The End. Almost. WE HAVE JUST BEGUN...\""

splitedStory= story.split(". ")

print(len(splitedStory))