# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 23:08:41 2019

@author: David Bestue
"""

import pandas as pd
import numpy as np
import easygui

 ## Open .xlsx
path_file = easygui.fileopenbox(msg=None, title=None, default=None)
df = pd.read_excel(path_file) 
list_subjects = df.columns


### function to count
def contar_votos(v):
    if v[0]=='1':
        p1 = -1
    elif v[0]=='2':
        p1=0
    elif v[0]=='3':
        p1=2
    else:
        print('Error in p1')
    ###
    if v[1]=='1':
        p2=-1
    elif v[1]=='2':
        p2=1
    elif v[1]=='3':
        p2=2
    else:
        print('Error in p2')
    ###
    if v[2]=='1':
        p3=1
    elif v[2]=='2':
        p3=0.5
    elif v[2]=='3':
        p3=0
    elif v[2]=='4':
        p3=0
    elif v[2]=='5':
        p3=0.5
    else:
        print('Error in p3')
    ###
    if v[3]=='1':
        p4=1
    elif v[3]=='2':
        p4=0.5
    elif v[3]=='3':
        p4=0
    elif v[3]=='4':
        p4=-1
    else:
        print('Error in p4')
    ###
    return p1 + p2 + p3 + p4


#### Save results
dict_punt = {}

for subj in list_subjects:
    df_s = df[subj][~np.isnan(df[subj])] 
    resultados_subj = []
    for votaciones in range(len(df_s)):
        votos = str(int(df_s.iloc[votaciones]))
        total = contar_votos(votos)
        ###
        resultados_subj.append(total)
    ###
    dict_punt[subj]=np.mean(resultados_subj) ### mean por si nos descontamos y alguno tiene mas votos
    ###


### print the output in the terminal 
sorted_x = sorted(dict_punt.items(), key=lambda kv: kv[1]) 
sorted_x.reverse() 
print(sorted_x)
        

### Message 
msg ='Ganadores: ' + sorted_x[0][0] + ', ' +sorted_x[1][0] + ' and ' + sorted_x[2][0]

######################## python 2 ###########################
#import tkMessageBox  ## if python 2
#tkMessageBox.showinfo("", msg) ### if python 2

######################## python 3 ###########################
from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("300x300+400+250")
def winners_msg():
   messagebox.showinfo("", msg)


B1 = Button(top, text = "Los ganadores son...", command = winners_msg)
B1.place(x = 100,y = 100)
top.mainloop()