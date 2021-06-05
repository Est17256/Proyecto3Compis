import os
from Creator import *
textoA="DoubleLuis.atg"
texto = open(textoA, "r")
temp, chrs, keys, toks, prd= load(textoA)
npgm(temp, chrs, keys, toks, prd)
nombre = temp[0].split(" ")
print(nombre)
os.system('python '+nombre[1]+'.py')
