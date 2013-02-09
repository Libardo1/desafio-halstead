$ python3 halstead.py tokens.txt fuente.txt<br/>
n1 = 6 {'then', '<=', 'else', 'print', 'input', 'if'}<br/>
N1 = 7 ['input', 'print', 'print', 'if', 'else', 'then', '<=']<br/>
n2 = 5 {'a1', '"ganaste"', '100', '"perdiste"', "'ingrese un valor:'"}<br/>
N2 = 6 ["'ingrese un valor:'", 'a1', 'a1', '100', '"ganaste"', '"perdiste"']<br/>
<br/>
N = 13.000000<br/>
n = 11.000000<br/>
V = 44.972611<br/>
D = 3.600000<br/>
L = 0.277778<br/>
E = 161.901400<br/>
T = 8.994522<br/>
<br/><br/><br/>
****
$ python3 halstead.py tokens.txt halstead.py<br/>
n1 = 11 {'=', 'for', 'and', '/', 'if', '+', '*', 'not', 'import', 'in', '%'}
N1 = 40 ['if', 'for', 'for', 'in', 'in', 'in', 'import', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '=', '/', '/', '/', '/', '*', '*', '*', '+', '+', 'and', 'not', 'not', '%', '%']
n2 = 39 {'math', 'len', 'n1data', 'read', 't', 'r', 'n', 'i', 'log', 'open', 'is', 'V', 'T', 'N', 'L', 'n2', 'n1', 'escape', 'E', 'D', 'set', 're', '\'".*"|\\\'.*\\\'|\\\\b\\\\w+\\\\b\', open(sys.argv[2], \'r\'', '2', '1', 'sum', 'print', 'N1', 'sys', '"(?:(?<=[ \\t\\n\\r\\v])|(?<=\\A))%s(?=[\\(\\[\\{ \\t\\n\\r\\v]|\\Z)"', '18', 'n2data', 'split', "'r').read()) for t in open(sys.argv[1], 'r'", 'argv', 'findall', "'' and i not in open(sys.argv[1], 'r'", 'N2', '"n1 = %d %s\\nN1 = %d %s\\nn2 = %d %s\\nN2 = %d %s\\n\\nN = %f\\nn = %f\\nV = %f\\nD = %f\\nL = %f\\nE = %f\\nT = %f"'}
N2 = 90 ['sys', 're', 'math', 'n1data', 'sum', 're', 'findall', 'r', '"(?:(?<=[ \\t\\n\\r\\v])|(?<=\\A))%s(?=[\\(\\[\\{ \\t\\n\\r\\v]|\\Z)"', 're', 'escape', 't', 'open', 'sys', 'argv', '2', "'r').read()) for t in open(sys.argv[1], 'r'", 'read', 'split', 'n1', 'N1', 'len', 'set', 'n1data', 'len', 'n1data', 'n2data', 'i', 'i', 're', 'findall', '\'".*"|\\\'.*\\\'|\\\\b\\\\w+\\\\b\', open(sys.argv[2], \'r\'', 'read', 'i', 'is', "'' and i not in open(sys.argv[1], 'r'", 'read', 'split', 'n2', 'N2', 'len', 'set', 'n2data', 'len', 'n2data', 'N', 'n', 'N1', 'N2', 'n1', 'n2', 'V', 'D', 'N', 'math', 'log', 'n', '2', 'n1', '2', 'N2', 'n2', 'L', 'E', '1', 'D', 'V', 'D', 'T', 'E', '18', 'print', '"n1 = %d %s\\nN1 = %d %s\\nn2 = %d %s\\nN2 = %d %s\\n\\nN = %f\\nn = %f\\nV = %f\\nD = %f\\nL = %f\\nE = %f\\nT = %f"', 'n1', 'set', 'n1data', 'N1', 'n1data', 'n2', 'set', 'n2data', 'N2', 'n2data', 'N', 'n', 'V', 'D', 'L', 'E', 'T']

N = 130.000000
n = 50.000000
V = 733.701305
D = 12.692308
L = 0.078788
E = 9312.362713
T = 517.353484
