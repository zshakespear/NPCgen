# -*- coding: utf-8 -*-
"""
Created on Sun March 20, 2022

@author: Zac Shakespear
The purpose of this program is to assist in generating
NPCs for the CDS setting

TO-DO:
    -Add appearances unique to species
    -Allow user to select varying levels of randomness
    
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

Arandlimit = Agen.size - 1
Qrandlimit = Qgen.size - 1
Mrandlimit = Mgen.size - 1
Irandlimit = Igen.size - 1

npcA = pd.DataFrame([['Appearance: ', Agen.at[random.randint(0,Arandlimit)]]])
npcI = pd.DataFrame([['Items: ', Igen['General'].at[random.randint(0,Irandlimit)]]])
npcQ = pd.DataFrame([['Quirk: ', Qgen.at[random.randint(0,Qrandlimit)]]])
npcM = pd.DataFrame([['Motivation: ', Mgen.at[random.randint(0,Mrandlimit)]]])


npcProf = pd.concat([npcA,npcI,npcQ,npcM])

with open("newNPC.txt", 'w') as file:
        textDummy = npcProf.to_string(header=False, index = False)
        file.write(textDummy)

del Agen
del Arandlimit
del file
del Igen
del Irandlimit
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