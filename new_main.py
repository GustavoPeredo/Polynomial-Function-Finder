from sympy import *
from sympy.parsing.sympy_parser import parse_expr
from sympy.combinatorics import Permutation 
from itertools import permutations 

x,y,i = symbols("x,y,i")

print("""
  _____      _                             _           _       _   ______                _   _               ______ _           _           
 |  __ \    | |                           (_)         (_)     | | |  ____|              | | (_)             |  ____(_)         | |          
 | |__) |__ | |_   _ _ __   ___  _ __ ___  _ _ __ ___  _  __ _| | | |__ _   _ _ __   ___| |_ _  ___  _ __   | |__   _ _ __   __| | ___ _ __ 
 |  ___/ _ \| | | | | '_ \ / _ \| '_ ` _ \| | '_ ` _ \| |/ _` | | |  __| | | | '_ \ / __| __| |/ _ \| '_ \  |  __| | | '_ \ / _` |/ _ \ '__|
 | |  | (_) | | |_| | | | | (_) | | | | | | | | | | | | | (_| | | | |  | |_| | | | | (__| |_| | (_) | | | | | |    | | | | | (_| |  __/ |   
 |_|   \___/|_|\__, |_| |_|\___/|_| |_| |_|_|_| |_| |_|_|\__,_|_| |_|   \__,_|_| |_|\___|\__|_|\___/|_| |_| |_|    |_|_| |_|\__,_|\___|_|   
                __/ |                                                                                                                       
               |___/  
               """)

print("Hello! Welcome to Polynomial Function Finder, a software used to find a function \n of smallest degree from points you have. Type the x coordinates of your points, separated by semi collomn ';': ")

xvalues = input().split(";")

xvalues = [float(z) for z in xvalues]

print("Now the respective y coordinates of your pounts: ")

yvalues = input().split(";")

yvalues = [float(z) for z in yvalues]

print("Now let the computer do it's magic.")

def Multiply(xvalues3, tau, maximum):
	result = 1
	for i in range(maximum):
		if type(xvalues3[i]) is str:
			result = result * float(xvalues3[i])
		else:
			result = result * xvalues3[i]**(maximum - tau[i] - 1)
	return result

def testFunction(function, xvalues, yvalues):
	xs = 0
	results = []
	sympy_exp = parse_expr(str(function))
	for xvalue in xvalues:
		results.append(float(sympy_exp.evalf(subs={x:xvalue})))
	if results == yvalues:
		return True
	else:
		return False


if all(i is yvalues for i in yvalues):
	result = yvalues[0]
	
else:
	fuctionWasFound = False
	for z in range(len(yvalues) + 1):
		if not fuctionWasFound:
			result = 0
			if z == 2:
				result = ((yvalues[0] - yvalues[1])/(xvalues[0] - xvalues[1]))*x + ((xvalues[0]*yvalues[1]) - (xvalues[1]*yvalues[0]))/(xvalues[0] - xvalues[1])
			elif z > 2:
						constants = []
						perm = [list(x) for x in permutations(range(z))]
						for p in range(z):
								summationDom = 0
								summationNom = 0
								for tau in perm:

									"""if xvalues[tau.index(p)] != 0:
										summationNom = summationNom + ((-1)**(len(Permutation(tau).transpositions()))*((Multiply(xvalues,tau,z))/(xvalues[tau.index(p)]**(z-p-1)))*yvalues[tau.index(p)])
									elif xvalues[tau.index(p)] == 0:"""
									
									xvalues2 = xvalues.copy()
									xvalues2[tau.index(p)] = str(yvalues[tau.index(p)])
									summationNom = summationNom + ((-1)**(len(Permutation(tau).transpositions()))*((Multiply(xvalues2,tau,z))))
									
									summationDom = summationDom + (((-1)**(len(Permutation(tau).transpositions())))*(Multiply(xvalues,tau,z)))
								constants.append(summationNom/summationDom)
						for values in range(len(constants)):
							result = result + constants[values]*x**(len(constants)-values-1)
			fuctionWasFound = testFunction(result, xvalues, yvalues)
pprint(result)
