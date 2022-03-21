# -*- coding: utf-8 -*-
"""
Created on Sun March 20, 2022

@author: Zac Shakespear
The purpose of this program is to assist in generating
NPCs for the CDS setting

TO-DO:
    
"""

import pandas as pd
import random
import os

wd = os.getcwd()
wd+='\GenNPC.xlsx'

Agen = pd.read_excel(wd, sheet_name='Appearance')
Qgen = pd.read_excel(wd, sheet_name='Quirks')
Mgen= pd.read_excel(wd, sheet_name='Motivations')
Igen = pd.read_excel(wd, sheet_name='Items&Clothing')

"""
What do I want to do here?
If the user selects yes, then the code
can just execute. 
If the user selects no, then we will want
the user to pick the species first.
Once the species is picked, then they can have
the option to add an item or not.
After that, they can select if they want a quirk or not
After that, they can select a motivation
Functionally, we'll want the user to be picking the col values
"""

isrand = input('Would you like a completely random NPC? \ny or n\n')
while isrand!='y' and isrand!='n' :
    isrand = input('Invalid input \nWould you like a completely random NPC? \ny or n\n')
if isrand == 'y' :
        numcol = len(Agen.axes[1])
        acol = random.randint(0, numcol - 1)
        
        
        numcol = len(Qgen.axes[1])
        qcol = random.randint(0, numcol - 1)
       

        numcol = len(Mgen.axes[1])
        mcol = random.randint(0,numcol-1)
        
else:
    #eventually we will want to do away with these magic numbers/strings
    acol = input('Select a species \n0: General\n1: Human\n2: Lutran\n3: Drake\n4: Xencoles\n5: Random\n')
    while acol != '0' and acol != '1' and acol!='2' and acol!='3' and acol!='4' and acol!='5':
        acol = input('Invalid input \nSelect a species \n0: General\n1: Human\n2: Lutran\n3: Drake\n4: Xencoles\n')
    if acol == '5':
        numcol = len(Agen.axes[1])
        acol = random.randint(0, numcol - 1)
    else:
        acol = int(acol)
    #next we will want to decide if we want an item
    iwant = input('Would you like this NPC to have an item? \ny or n?\n')
    while iwant != 'y' and iwant != 'n':
        iwant = input('Invalid input \nWould you like this NPC to have an item? \ny or n?\n')
    if iwant == 'y':
        iwant = True
    else:
        iwant == False
    #then we will want to decide if we want a quirk and if so, what kind of quirk
    qwant = input('Would you like this NPC to have a quirk? \ny or n?\n')
    while qwant != 'y' and qwant !='n':
        qwant = input('Invalid input \nWould you like this NPC to have a quirk? \ny or n?\n')
    if qwant == 'y':
        qwant = True
    else:
        qwant = False
    if qwant:
        qcol = input('What kind of quirk would you like this NPC to have?\n0: Fear\n1: Mannerism\n2: Random\n')
        while qcol != '0' and qcol != '1' and qcol!='2':
            qcol = input('Invalid input \nWhat kind of quirk would you like this NPC to have?\n0: Fear\n1: Mannerism\n2: Random\n')
        if qcol == '2':
            numcol = len(Qgen.axes[1])
            qcol = random.randint(0, numcol - 1)
        else:
            qcol = int(qcol)
    #finally we will want to decide what kind of motivation
    mcol = input('Select a motivation \n0: Relationships\n1: Belief\n2: Personal Cause\n3: Personal Cause\n4: Social Cause\n5: Obligation\n6: Random\n')
    while mcol != '0' and mcol != '1' and mcol != '2' and mcol != '3' and mcol != '4' and mcol !=  '5' and mcol != '6':
        mcol = input('Invalid input \nSelect a motivation \n0: Relationships\n1: Belief\n2: Personal Cause\n3: Personal Cause\n4: Social Cause\n5: Obligation\n6: Random\n')
    if mcol == '6':
        numcol = len(Mgen.axes[1])
        mcol = random.randint(0, numcol - 1)
    else:
        mcol = int(mcol)


Agen = Agen.iloc[:, acol]
Agen = Agen[Agen.notna()]

del acol


Mgen = Mgen.iloc[:, mcol]
Mgen = Mgen[Mgen.notna()]

del mcol

"""
numcol = len(Agen.axes[1])
acol = random.randint(0, numcol - 1)
Agen = Agen.iloc[:, acol]
Agen = Agen[Agen.notna()]

del acol

numcol = len(Qgen.axes[1])
qcol = random.randint(0, numcol - 1)
Qgen = Qgen.iloc[:, qcol]
Qgen = Qgen[Qgen.notna()]

del qcol

numcol = len(Mgen.axes[1])
mcol = random.randint(0,numcol-1)
Mgen = Mgen.iloc[:, mcol]
Mgen = Mgen[Mgen.notna()]

del mcol


del numcol

"""

if qwant:
    #We'll have to do something about this if qwant is false
    Qgen = Qgen.iloc[:, qcol]
    Qgen = Qgen[Qgen.notna()]
    Qrandlimit = Qgen.size - 1
    npcQ = pd.DataFrame([['Quirk: ', Qgen.at[random.randint(0,Qrandlimit)]]])
    del qcol

if iwant:
    Irandlimit = Igen.size - 1
    npcI = pd.DataFrame([['Items: ', Igen['General'].at[random.randint(0,Irandlimit)]]])
    del Irandlimit

Arandlimit = Agen.size - 1
Mrandlimit = Mgen.size - 1


npcA = pd.DataFrame([['Appearance: ', Agen.at[random.randint(0,Arandlimit)]]])
npcM = pd.DataFrame([['Motivation: ', Mgen.at[random.randint(0,Mrandlimit)]]])

if iwant and qwant:
    npcProf = pd.concat([npcA,npcI,npcQ,npcM])

else: 
    if iwant:
        npcProf = pd.concat([npcA,npcI,npcM])
    if qwant:
        npcProf = pd.concat([npcA,npcQ,npcM])
    else:
        npcProf = pd.concat([npcA,npcM])
        
with open("newNPC.txt", 'w') as file:
        textDummy = npcProf.to_string(header=False, index = False)
        file.write(textDummy)

del Agen
del Arandlimit
del file
del Igen
del Mgen
del Mrandlimit
del npcA
del npcI
del npcM
del npcQ
del npcProf
del Qgen
del Qrandlimit
del textDummy
del wd
"""
period = input("Enter the number of years for the timeline: ")
period = int(period)
numyears = input("Enter the start year for the timeline: ")
numyears = int(numyears)
it = input("Enter the number of years between each event: ")
it = int(it)
enddate = numyears + period

eventlist = pd.DataFrame(columns = ['Year', 'Event'])
while numyears < enddate:
    event = random.randint(0,randlimit)
    newevent = pd.DataFrame([[numyears, gen.at[event,'Events']]], 
                            columns = ['Year','Event'])
    eventlist = eventlist.append(newevent)
    numyears += it
    


"""