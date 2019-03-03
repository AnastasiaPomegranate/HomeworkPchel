A = int(input("A="))
B = int(input("B="))

def Evklid (A,B):
	while A != 0 and B != 0:
		if A>B:
			A=A%B
		else:
			B=B%A
	return A+B
print ("NOD=",Evklid(A,B))
