from AFD import * 
from Evaluator import *
keywords =['while', 'do']
upletter ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
upletter = character(upletter)
downletter ="abcdefghijklmnopqrstuvwxyz"
downletter = character(downletter)
letter = "abcdefghijklmnopqrstuvwxyz" + upletter + downletter 
letter = character(letter)
digit = "0123456789" 
digit = character(digit)
hexdigit = digit + "ABCDEF"
hexdigit = character(hexdigit)
hexterm = 'H'
hexterm = character(hexterm)
tab = chr(9)
tab = character(tab)
eol = chr(10)
eol = character(eol)
whitespace = chr(13)+eol+tab+chr(13)
whitespace = character(whitespace)
sign ='+'+'-'
sign = character(sign)
ident=letter+" (("+letter+"|"+digit+")*)"
hexnumber=hexdigit+" (("+hexdigit+")*) "+hexterm
number=digit+" (("+digit+")*)"
signnumber="(("+sign+")*) "+digit+" (("+digit+")*)"
whitetoken=whitespace+" (("+whitespace+")*)"
autk=[ident,hexnumber]
aut =[number,signnumber,whitetoken]
charss =[ chr(9), chr(10), chr(13)+eol+tab+chr(13)]
scanner(keywords, aut , autk, charss)


def converse(val):
    
	try:
    
	      result=int(val, 16)
    
	except ValueError:
    
	      print("Not HEX")
    
	      exit()

	return result

def operaciones(val1,val2,sig1):   
    
	if sig1=="*":
    
	    res= val1*val2
    
	if sig1=="/":
    
	    res= val1/val2
    
	if sig1=="+":
    
	    res= val1+val2
    
	if sig1=="-":
    
	    res= val1-val2
    
	result=res

	return result

def main():   
    
	temp=input("Enter val1: ")
    
	val1=converse(temp)
    
	sig1=input("Enter sign: ")
    
	temp=input("Enter val2: ")
    
	val2=converse(temp)
    
	result=operaciones(val1,val2,sig1)

	return result


print(main())