import sys, re
from math import log


with open(sys.argv[1], 'r') as f:
    tokens = f.read().split()

with open(sys.argv[2], 'r') as f:
    fuente = f.read()

ops = [len(re.findall("%s " % t, fuente)) for t in tokens]
n1, N1 = sum([n > 0 for n in ops]), sum(ops)

ops = [i for i in
       re.findall(
       '".*"|\'.*\'|[a-zA-Z0-9]*', fuente)
       if i != '' and i not in tokens]
n2, N2 = len(set(ops)), len(ops)

N, n = N1 + N2 , n1 + n2
V, D  = N * log(n, 2), (n1 / 2) * (N2 / n2)
L, E = 1 / D, V * D
T = E / 18

print("n1 = %f\nn2 = %f\nN1 = %f\nN2 = %f\nN = %f\nn = %f\nV = %f\nD = %f\nL = %f\nE = %f\nT = %f"
    % (n1, n2, N1, N2, N, n, V, D, L, E, T))