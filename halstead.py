import sys, re, math


def getRegexpMatch(regexp, string):
    data = re.findall(regexp, string)
    string = re.sub(regexp, ' ', string)
    return data, string

tokens, fuente = open(
    sys.argv[1], 'r').read().split(), open(sys.argv[2], "r").read()
tokens.sort(key=lambda s: 1 / len(s))


strings, fuente = getRegexpMatch(
    r"\'([^\"\'\\]*(?:\\.[^\"\'\\]*)*)\'|\"([^\"\'\\]*(?:\\.[^\"\'\\]*)*)\"", fuente)

special = [re.escape(t) for t in ". , ; : ? ! [ ] ( ) { }".split(' ')]
fuente = re.sub('|'.join(special), " ", fuente)

n2data = []
for i in re.findall('\\w+', fuente):
    if i not in tokens:
        data, fuente = getRegexpMatch(r'(?:\b)%s(?:\b)' % re.escape(i), fuente)
        n2data = n2data + data

n2data = n2data + strings

n1data = []
for i in tokens:
    data, fuente = getRegexpMatch(re.escape(i), fuente)
    n1data = n1data + data

n1, N1, n2, N2 = len(set(n1data)), len(n1data), len(set(n2data)), len(n2data)

N, n = N1 + N2, n1 + n2
V, D = N * math.log(n, 2), (n1 / 2) * (N2 / n2)
L, E = 1 / D, V * D
T = E / 18

print("n1 = %d => %s\nN1 = %d => %s\nn2 = %d => %s\nN2 = %d => %s\n\nN = %d\nn = %d\nV = %f\nD = %f\nL = %f\nE = %f\nT = %f"
      % (n1, set(n1data), N1, n1data, n2, set(n2data), N2, n2data, N, n, V, D, L, E, T))
