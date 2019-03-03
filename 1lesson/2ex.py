import math
A = float(input("A="))
B = float(input("B="))
C = float(input("C="))

def nahodX(A,B,C):
	if A != 0:
		D=B**2 - 4*A*C
		if D>0:
			X1=(-B+math.sqrt(D))/(2*A)
			X2=(-B-math.sqrt(D))/(2*A)
			print("%.2f, %.2f"%(X1,X2))
		elif D==0 :
			X1=-B/(2*A)
			print("%.2f"%(X1))
		else :
			print ("Корней нет")
	elif (B==0 and A==0):
		print("Корней нет")
	else:
		X1=-C/B
		print("%.2f"%(X1))

nahodX(A,B,C)
