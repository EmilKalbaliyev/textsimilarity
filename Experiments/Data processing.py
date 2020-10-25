import pandas as pd
import numpy as np
import algorithms
from random import randrange


def clear_text(a):
    a = a.lower()
    a = a.replace("\n", "")
    a = a.replace(".", "")
    a = a.replace("?", "")
    a = a.replace("!", "")
    a = a.replace("\"", "")
    a = a.replace(":", "")
    a = a.replace(",", "")
    a = a.replace("-", "")
    a = a.replace("|", "")
    a = a.replace("”", "")
    a = a.replace("“", "")
    return a


dataset=["cemiyyet","hadise","idman","iqtisadiyyat","maraqli","medeniyyet","siyaset","texnologiya"]
data1=data2=""
for name in dataset:
    with open("../dataset/"+name+".txt","r") as file:
        data2 = file.read()
        data1 += "\n"
        data1 += data2 
with open ('whole_data.txt', 'w') as fp: 
    fp.write(data1) 



with open("whole_data.txt","r") as file:
    same = []
    data = [[]]
    i = 0
    for ln in file:
        if ln.startswith("#"):
            num = int(ln[1:(int(ln[0:6].find(':')))])
            if (i == num):
                a = ln[int(ln[0:6].find(':')) + 1:]
                a = clear_text(a)
                a = a.replace("\n", "")
                same.append(a)
            elif (i != num):
                data.insert(i, same)
                i = num
                same = []
                a = ln[int(ln[0:6].find(':')) + 1:]
                a=clear_text(a)
                a = a.replace("\n", "")
                same.append(a)
    data.insert(i, same)



file_object = open('labeled_data.txt', 'a')
from random import choice
for m in range (8):
    for i in range(50*m+1,(m+1)*50+1):
        for j in range(4):
            numbers = []
            for k in range(4):
                if (j != k):
                    file_object.write(data[i][j]+" ,"+ data[i][k]+", 1"+"\n")
            for k in range(2):
                random1 = choice([g for g in range(50*m, (m+1)*50+1) if g not in [0,i]])
                random2 = randrange(0, 4)
                if (random1 == i):
                    random1 = randrange(50*m, (m+1)*50+1)
                file_object.write(data[i][j]+" , "+data[random1][random2]+", 0"+"\n")
            random1 = choice([g for g in range(0, 8) if g not in [0,m]])
            random2 = choice([g for g in range(0, 50) if g not in [0,m]])
            random3 = randrange(0, 4)
            file_object.write(data[i][j]+" , "+data[50*random1+random2][random3]+", 0"+"\n")
file_object.close() 



pro_data=pd.read_csv('labeled_data.txt',delimiter=",",header=None)



file_object2 = open('res.txt', 'a')
file_object2.write("similar,Jaro,Winkler,Levenshtein,Ratcliff_Obershelp,Damerau-Levenshtein,LCSubstring,LCSubsequence\n")
for i in range(0,pro_data.shape[0]):
    similar=pro_data.iloc[i][2]
    jaro=algorithms.Jaro(pro_data.iloc[i][0],pro_data.iloc[i][1])
    winkler=algorithms.Jaro_Winkler(pro_data.iloc[i][0],pro_data.iloc[i][1])
    levenshtein=algorithms.Levenshtein(pro_data.iloc[i][0],pro_data.iloc[i][1])
    ratcliff_obershelp=algorithms.Ratcliff_Obershelp(pro_data.iloc[i][0],pro_data.iloc[i][1])
    damerau_levenshtein=algorithms.Damerau_Levenshtein(pro_data.iloc[i][0],pro_data.iloc[i][1])
    lcsubstring=algorithms.LCStr(pro_data.iloc[i][0],pro_data.iloc[i][1])
    lcsubsequence=algorithms.LCSeq(pro_data.iloc[i][0],pro_data.iloc[i][1])
    file_object2.write(str(similar)+","+str(jaro)+","+str(winkler)+","+str(levenshtein)+","+str(ratcliff_obershelp)+","+str(damerau_levenshtein)+","+str(lcsubstring)+","+str(lcsubsequence)+"\n")
file_object2.close() 

