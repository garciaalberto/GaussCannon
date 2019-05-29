import pprint
import scipy
import scipy.linalg as slinlang 

alpha = 125
x = 1
y = 2
diagonal = x+y*alpha
minor_diagonal = -alpha

dimension = 25

bidimensional_array = [[0 for i in range(dimension)] for j in range(dimension)]

for i in range(dimension):
	for j in range(dimension):
		if i == j:
			bidimensional_array[i][j] = diagonal
		if i-1 == j:
			bidimensional_array[i][j] = minor_diagonal
		if i+1 == j:
			bidimensional_array[i][j] = minor_diagonal

A = scipy.array(bidimensional_array)

P, L, U = slinlang.lu(A)
Q, R = slinlang.qr(A)

print("A:")
pprint.pprint(A)

print("P:")
pprint.pprint(P)

print("L:")
pprint.pprint(L)

print("U:")
pprint.pprint(U)

print("Q:")
pprint.pprint(Q)

print("R:")
pprint.pprint(R)

i=input()