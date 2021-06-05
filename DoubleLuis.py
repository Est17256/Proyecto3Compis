from AFD import * 
from Evaluator import *
keywords =['while', 'do']
digit="0123456789"
digit= character(digit)
tab=chr(9)
tab= character(tab)
eol=chr(10)
eol= character(eol)
blanco=eol+chr(13)+tab
blanco= character(blanco)
number=digit+" (("+digit+")*)"
decnumber=digit+" (("+digit+")*) " +". "+digit+" (("+digit+")*)"
white=blanco+" (("+blanco+")*)"
autk=[]
aut =[number,decnumber,white]
charss =[chr(9),chr(10),eol+chr(13)+tab]
scanner(keywords, aut , autk, charss)


def security(val):
    
	try:
    
	      result = float(val)
    
	except ValueError:
    
	      print("Not int or double, exit")
    
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
    
	val1=security(temp)
    
	sig1=input("Enter sign: ")
    
	temp=input("Enter val2: ")
    
	val2=security(temp)
    
	result=operaciones(val1,val2,sig1)

	return result


print(main())