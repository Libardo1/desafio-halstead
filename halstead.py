import sys, re
from math import log


with open(sys.argv[1], 'r') as f:
    tokens = f.read().split()

with open(sys.argv[2], 'r') as f:
    fuente = f.read()

n1data = [re.findall(t, fuente) for t in tokens]
n1data = sum(n1data, [])
n1, N1 = len(set(n1data)), len(n1data)

# print (n1data)

n2data = [i for i in
       re.findall(
       '".*"|\'.*\'|[a-zA-Z0-9]*', fuente)
       if i != '' and i not in tokens]
n2, N2 = len(set(n2data)), len(n2data)

N, n = N1 + N2 , n1 + n2
V, D  = N * log(n, 2), (n1 / 2) * (N2 / n2)
L, E = 1 / D, V * D
T = E / 18

print("n1 = %d %s\nN1 = %d %s\nn2 = %d %s\nN2 = %d %s\n\nN = %f\nn = %f\nV = %f\nD = %f\nL = %f\nE = %f\nT = %f"
    % (n1, set(n1data), N1, n1data, n2, set(n2data), N2, n2data, N, n, V, D, L, E, T))