# -*- coding: utf-8 -*-
"""
Created on Sun March 20, 2022

@author: Zac Shakespear
The purpose of this program is to assist in generating
NPCs for the CDS setting

TO-DO:
    -Create random NPCs which have a random physical appearance, 
    a quirk, and a motivation without respect to species
    -Add unique to species
    -Split Appearance Tab into physical appearance and items tabs
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
Arandlimit = Agen['General'].size - 1
Qrandlimit = Qgen['Mannerisms'].size - 1
Mrandlimit = Mgen['Relationships'].size - 1

npcA = pd.DataFrame([['Appearance: ', Agen['General'].at[random.randint(0,Arandlimit)]]])
npcQ = pd.DataFrame([['Quirk: ', Qgen['Mannerisms'].at[random.randint(0,Qrandlimit)]]])
npcM = pd.DataFrame([['Motivation: ', Mgen['Relationships'].at[random.randint(0,Mrandlimit)]]])

npcProf = pd.concat([npcA,npcQ,npcM])

with open("newNPC.txt", 'w') as file:
        textDummy = npcProf.to_string(header=False, index = False)
        file.write(textDummy)

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