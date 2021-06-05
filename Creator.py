from AFD import *
import os
"""
Function that load the ATG file and distributed
"""
def load(url):
    chrs = []
    keys = []
    toks = []
    temp = []
    prd=[]
    wht = 0
    fls = []
    fls2 = open(url, "r")
    for i in fls2.readlines():
        if i[-1:] == "\n":
            fls.append((i[:-1]))
        else:
            fls.append(i)
    fls2.close() 
    for i in fls:
        if i.strip() == "TOKENS":
            wht = 1
        if i.strip() == "CHARACTERS":
            wht = 2
        if i.strip() == "KEYWORDS":
            wht = 3
        if i.strip() == "PRODUCTIONS":
            wht = 4
        if wht == 1:
            toks.append(i)
        if wht == 0:
            temp.append(i)
        if wht == 2:
            chrs.append(i)
        if wht == 3:
            keys.append(i)
        if wht == 4:
            prd.append(i)
    return temp, chrs, keys, toks, prd
"""
Function that make the new python program
"""
def npgm(temp, chrs, keys, toks, prd):
    holis=[]
    keys2=[]
    toks2=[]
    chara=[]
    aut = []
    chars = []
    autk = []
    if temp[0] != "":
        nombre = temp[0].split(" ")
        if nombre[0] == "COMPILER":
            file = open(nombre[1]+".py",'w')
    file.write("from AFD import * ")
    file.write("\n")
    file.write("from Evaluator import *")
    file.write("\n")
    keywordss = []
    for i in range(len(keys)):
        if keys[i].strip() == "KEYWORDS":
            pass
        else:
            if keys[i] != "":
                x = keys[i].split("=")
                y = x[1].replace(chr(34), "")
                y = y.replace(chr(39), "")
                y = y.replace(".", "")
                keywordss.append(y.strip())
    file.write("keywords ="+str(keywordss)+"\n")
    holis.append(["keywords",str(keywordss)])
    keys2.append(["keywords",str(keywordss)])
    for i in range(len(chrs)):
        if chrs[i].strip() == "CHARACTERS":
            pass
        else:
            lst = chrs[i].rfind(".")
            nstr = chrs[i][:lst] + "" + chrs[i][lst+1:]
            if nstr != "":
                y = nstr.split("=")
                if "chr(" in y[1] or "CHR(" in y[1] :
                    chars.append(y[1].lower())
                    file.write(nstr.lower())
                    chara.append([y[0],nstr.lower()])
                    file.write("\n")
                    file.write(y[0]+"= character("+y[0].strip().lower()+")")
                    file.write("\n")
                elif y[1].strip() == "'A' . 'Z'" or y[1].strip() == "'A' . 'Z'." or y[1].strip()== chr(34)+"A"+chr(34)+ ".." +chr(34)+"Z"+chr(34):
                    y[1]=chr(34)+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"+chr(34)
                    file.write(y[0]+'='+y[1])
                    file.write("\n")
                    file.write(y[0]+"= character("+y[0].strip()+")")
                    chara.append([y[0],y[1]])
                    file.write("\n")
                elif y[1].strip()== "'a' . 'z'" or y[1].strip()== "'a' . 'z'." or y[1].strip()== chr(34)+"a"+chr(34)+ ".." +chr(34)+"z"+chr(34):
                    y[1] =chr(34)+"abcdefghijklmnopqrstuvwxyz"+chr(34)
                    file.write(y[0]+'='+y[1])
                    file.write("\n")
                    file.write(y[0]+"= character("+y[0].strip()+")")
                    chara.append([y[0],y[1]])
                    file.write("\n")
                else:
                    file.write(nstr)
                    file.write("\n")
                    file.write(y[0]+"= character("+y[0].strip()+")")
                    chara.append([y[0],y[1]])
                    file.write("\n")
    if toks[-1][0:3] == "END":
        toks.pop()
    for i in range(len(toks)):
        if toks[i].strip() == "TOKENS":
            pass
        else:
            if len(toks[i]) != 0:
                nstr = lst_str(toks[i],1)
                if nstr[len(nstr)-1] == ".":
                    nstr.pop()
                nstr = lst_str(nstr,0)
                nstr = nstr.strip()
                nstr = nstr.replace(chr(34), "+")
                nstr = nstr.replace("(H)", chr(34)+"H"+chr(34))
                nstr = nstr.replace("(","+"+chr(34)+" ("+chr(34)+"+")
                nstr = nstr.replace(")","+"+chr(34)+")"+chr(34))
                nstr = nstr.replace("|","+"+chr(34)+"|"+chr(34)+"+")
                nstr = nstr.replace(".", chr(34)+". "+chr(34))
                nstr = nstr.replace("{", "+"+chr(34)+" (("+chr(34)+"+")
                nstr = nstr.replace("[", "+"+chr(34)+" (("+chr(34)+"+")
                nstr = nstr.replace("}", "+"+chr(34)+")*) "+chr(34)+"+")
                nstr = nstr.replace("]", "+"+chr(34)+")*) "+chr(34)+"+")
                nstr2 = nstr.split()
                if len(nstr2)>2 and nstr2[len(nstr2)-1] == "KEYWORDS" and nstr2[len(nstr2)-2] == "EXCEPT" :
                     nstr2.pop()
                     nstr2.pop()
                     autk.append(nstr2[0])
                else:
                    aut.append(nstr2[0])
                nstr2 = lst_str(nstr2,0)
                nstr2 = nstr2.split("=")
                nstr2[1]= nstr2[1].replace(")*)", ")*) ")
                if nstr2[1][0]== "+":
                    nstr2[1] = nstr2[1].replace("+","",1)
                if nstr2[1][-1] == "+":
                    nstr2[1] = nstr2[1][:-1]
                temp = lst_str(nstr2[1],1)
                if temp[-2] == " ":
                    temp.pop(len(temp)-2)
                for i in range(len(temp)):
                    if temp[i] == "." or temp[i] == ",":
                        temp.insert(i+1, " ")
                nstr2[1] = lst_str(temp,0)
                rsts = nstr2[0]+"="+lst_str(nstr2[1],0)
                rsts = rsts.replace("((", " ((")
                rsts = rsts.replace("+++", " +")
                rsts = rsts.replace("++", " +")
                rsts = rsts.replace(chr(34)+"("+chr(34), chr(34)+" ("+chr(34))
                temp2 = rsts.split("=")
                if lst_str(temp2[1],1)[1] == " ":
                    x = lst_str(temp2[1],1)
                    x.pop(1)
                    temp2[1] = lst_str(x,0)
                rsts = temp2[0]+"="+lst_str(temp2[1],0)
                rsts2 = temp2[0],lst_str(temp2[1],0)
                file.write(rsts)
                toks2.append([rsts2])
                file.write("\n")
    file.write("autk=" +strL(autk))
    holis.append([strL(autk)])
    file.write("\n")
    file.write("aut ="+strL(aut))
    holis.append([strL(aut)])
    file.write("\n")
    file.write("charss ="+strL(chars))
    holis.append([strL(chars)])
    file.write("\n")
    file.write("scanner(keywords, aut , autk, charss)")
    if prd[-1][0:3] == "END":
        prd.pop()
    temp = []
    cor =[]
    for i in range(len(prd)):
        if prd[i]== "" or prd[i] == "PRODUCTIONS" :
            pass
        else:
            temp.append(prd[i])
            if prd[i] =="." or prd[i] =="\t.":
                cor.append(temp)
                temp = []
    for i in range(len(cor)):
        if cor[i][0] != "\t":
            x1 = cor[i][0].split("=",1)
            x2 = x1[0].replace("<", "(")
            x2 = x2.replace(">", "):")
            x2 = x2.replace("ref int", "")
            x1[0] = x2
            if x1[0].find("(") >=0:
                cor[i][0] = "def "+x1[0]+x1[1]
            else:
                cor[i][0] = "def "+x1[0]+"():"+x1[1]
        else:
            x1 = cor[i][1].split("=",1)
            x2 = x1[0].replace("<", "(")
            x2 = x2.replace(">", "):")
            x2 = x2.replace("ref int", "")
            x1[0] = x2
            if x1[0].find("(") >=0:
                cor[i][1] = "def "+x1[0]+x1[1]
            else:
                cor[i][1] = "\ndef "+x1[0]+"():"+x1[1]
    for i in range(len(cor)):
        for j in range(len(cor[i])):
            cor[i][j] = cor[i][j].replace("\t", "")
            cor[i][j] = cor[i][j].replace(".)", "")
            cor[i][j] = cor[i][j].replace(";", "")
            cor[i][j] = cor[i][j].replace("<", "(")
            cor[i][j] = cor[i][j].replace(">", ")")
            cor[i][j] = cor[i][j].replace("ref int", "")
            cor[i][j] = cor[i][j].replace("ref", "")
            cor[i][j] = cor[i][j].replace("(.", "\n")
            cor[i][j] = cor[i][j].replace(":", ":")
    temp2 = []
    temp3 = []
    fnl = []
    temp4 = 2
    for i in range(len(cor)):
        for j in range(len(cor[i])):
            if temp4 == 1:
                temp3.append(cor[i][j])
            elif temp4 == 2:
                fnl.append(cor[i][j])
                temp2.append(temp3)
                temp3 = []       
    file2 = open("sup.txt",'w')
    file2.write(str(cor))
    for i in range(len(cor)):
        for j in range(len(cor[i])):
            if cor[i][j] != ".":
                file2.write("\n")
                file2.write(str(cor[i][j]))
    file2 = open("sup.py",'w')
    for i in range(len(fnl)):
        if fnl[i] != ".":
            file2.write(fnl[i])
            file2.write("\n")
        if fnl[i] == ".":
            file2.write("\nreturn result\n\n")
    file2.close()
    fnl2 = []
    with open('sup.py', 'r') as file3:
        for line in file3:
            fnl2.append(line)
    
    for i in range(len(fnl2)):
        e = fnl2[i].split()
        if len(e) !=0:
            if e[0] != "def":
                fnl2[i] = "\t"+fnl2[i]
    file3.close()
    file.write("\n")
    file.write("\n")
    file.write("\n")
    file2 = open("sup.py",'w')
    for i in range(len(fnl2)):
        if fnl2[i] != ".":
            file.write(fnl2[i])
    file2.close()
    file.close()
    file = open(nombre[1]+".py",'a')
    file.write("\n")
    file.write("print(main())")
    file.close()
    os.remove("sup.txt")
    os.remove("sup.py")