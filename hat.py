gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0
Do_you_like_Dawn_or_Dusk = int(input(" do you like dawn or dusk?(1 for dawn and 2 for dusk) "))
if Do_you_like_Dawn_or_Dusk == 1:
    gryffindor +=2
    ravenclaw +=2
elif Do_you_like_Dawn_or_Dusk == 2:
    hufflepuff +=2
    slytherin +=2
else : print("Wrong input.")
When_Im_dead_I_want_people_to_remember_me_as = int(input(" When Im dead, I want people to remember me as(1 for The Good and 2 for the Great and 3 for the Wise and 4 for the Bold)"))
if When_Im_dead_I_want_people_to_remember_me_as == 1: hufflepuff += 2
elif When_Im_dead_I_want_people_to_remember_me_as == 2: slytherin += 2
elif When_Im_dead_I_want_people_to_remember_me_as == 3: ravenclaw += 2
elif When_Im_dead_I_want_people_to_remember_me_as == 4: gryffindor += 2
else: print("Wrong input.")
q3 = int(input("Which kind of instrument most pleases your ear(1 for The violin and 2 for The trumpet and 3 for The piano and 4 for The drum)"))
if q3 == 1 : slytherin +=4
elif q3 == 2 : hufflepuff +=4
elif q3 == 3 : ravenclaw +=4
elif q3 == 4 : gryffindor +=4
else : print("Wrong input.")
if gryffindor > ravenclaw and gryffindor > hufflepuff and gryffindor > slytherin: 
    print("You are in Gryffindor")
elif ravenclaw > gryffindor and ravenclaw > hufflepuff and ravenclaw > slytherin:
    print("You are in Ravenclaw")
elif hufflepuff > gryffindor and hufflepuff > ravenclaw and hufflepuff > slytherin:
    print("You are in Hufflepuff")
else : 
    print("You are in Slytherin")