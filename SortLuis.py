from AFD import * 
from Evaluator import *
keywords =['while', 'do', 'if', 'switch']
letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" 
letter = character(letter)
digit = "0123456789" 
digit = character(digit)
tab = chr(9)
tab = character(tab)
eol = chr(10)
eol = character(eol)
ident=letter+" (("+letter+"|"+digit+")*)"
number=digit+" (("+digit+")*)"
autk=[ident]
aut =[number]
charss =[ chr(9), chr(10)]
scanner(keywords, aut , autk, charss)


def operations(val):
    
	lst=[]
    
	for i in range(val):
    
	      lst.append(input("Enter te word to sort: "))
    
	lst.sort()
    
	result=lst

	return result

def main():   
    
	val=input("Enter the number of words to sort: ")
    
	result=operations(int(val))

	return result


print(main())