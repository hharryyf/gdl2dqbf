'''
    3 quantifiers 
    _exists(F, int)
    _forall(F, int)
    _depend(E, U)

    all unquantified variables are quantified existentially in the inner most block 


    input format: a SAT formula in DIMACS format
    output: a DQBF formula in DQDIMACS format    
'''

import sys
import os

def parse_tuple(content):
    cnt = 0
    curr = ''
    elim = []
    for ch in content:
        if ch == ',' and cnt == 0:
            elim.append(curr)
            curr = ''
        else:
            curr += ch
        
        if ch == '(':
            cnt += 1
        elif ch == ')':
            cnt -= 1
    if curr != '':
        elim.append(curr)
    
    return elim

def dqasp2dqbf(aspfilelist, outfile):
    aspfilelist = ' '.join(aspfilelist)
    cmd = f'clingo --output=smodels {aspfilelist} | lp2normal2 | lp2lp2 | lp2acyc| lp2sat > game.dimacs'
    os.system(f"bash -c '{cmd}'")
    f = open('game.dimacs', 'r')
    ot = open(outfile, 'w')
    normalexists = {}
    normaluniv = {}
    exists = set()  # existential variables
    univ = set()    # universal variables
    depend = []
    var2id = {}     # variable name to id
    id2var = {}     # id to variable name
    quant = []      # list of tuples (level, type, variable)
    i = 0
    status = 0
    numvar = 0
    for line in f:
        if i == 0:
            s = line.split()
            numvar = int(s[2])
            print(line, end='', file=ot)
        else:
            s = line.split()
            if s[0] == 'c':
                if s[2][0] == '_':
                    quantifier = parse_tuple(s[2][8:-1])
                    if len(quantifier) == 2:
                        if s[2][:7] == '_exists':
                            quant.append((int(quantifier[1]), 'e', quantifier[0]))
                            exists.add(quantifier[0])
                            if quantifier[0] in normalexists.keys():
                                print(f'ERROR! Cannot quantify {quantifier[0]} in different level!', file=sys.stderr)
                                exit(1)
                            normalexists[quantifier[0]] = int(quantifier[1])
                        elif s[2][:7] == '_forall':
                            quant.append((int(quantifier[1]), 'a', quantifier[0]))
                            univ.add(quantifier[0])
                            if quantifier[0] in normaluniv.keys():
                                print(f'ERROR! Cannot quantify {quantifier[0]} in different level!', file=sys.stderr)
                                exit(1)
                            normaluniv[quantifier[0]] = int(quantifier[1])
                        else:
                            depend.append((quantifier[0], quantifier[1]))
                        quant.append((-1, 'e', s[2].strip()))
                        exists.add(s[2].strip())
                    var2id[s[2].strip()] = int(s[1])
                    id2var[int(s[1])] = s[2].strip()    
                else:
                    var2id[s[2].strip()] = int(s[1])
                    id2var[int(s[1])] = s[2].strip()
            else:
                if status == 0:                
                    # error check
                    # a variable cannot be quantified both existentially and univerally
                    for e in exists:
                        if e in univ:
                            print(f'ERROR! {e} is quantified both existentially and universally!', file=sys.stderr)
                            exit(1)

                    for e in depend:
                        if e[0] in univ:
                            print(f'ERROR! Cannot quantify {e[0]} both existentially and universally!', file=sys.stderr)
                        if e[1] not in univ:
                            print(f'ERROR! Must quantify {e[1]} universally!', file=sys.stderr)
                            exit(1)
                        if e[0] in exists:
                            print(f'ERROR! Cannot quantify {e[0]} existentially with both d and e!', file=sys.stderr)
                            exit(1)

                    for e in depend:
                        exists.add(e[0])

                    quant.sort()
                    depend.sort()
                    mx = 0
                    if len(quant) != 0:
                        mx = quant[-1][0]

                    for i in range(1, numvar + 1):
                        if i not in id2var.keys():
                            quant.append((mx + 1, 'e', i))
                        else:
                            if (id2var[i] not in exists) and (id2var[i] not in univ):
                                quant.append((mx + 1, 'e', i))      

                        
                    for i in range(0, len(quant)):
                        if i == 0:
                            print(quant[i][1], end='', file=ot)
                        elif quant[i][1] != quant[i-1][1]:
                            print(' 0', file=ot)
                            print(quant[i][1], end='', file=ot)

                        if quant[i][0] < mx + 1:
                            print(f' {var2id[quant[i][2]]}', end='', file=ot)
                        else:
                            print(f' {quant[i][2]}', end='', file=ot)     

                        if (i == len(quant) - 1):
                            print(' 0', file=ot)
                        
                    # deal with dependencies
                    for i in range(0, len(depend)):
                        if i == 0:
                            print(f'd {var2id[depend[i][0]]} {var2id[depend[i][1]]}', end='', file=ot) 
                        elif depend[i][0] != depend[i-1][0]:
                            print(' 0', file=ot)
                            print(f'd {var2id[depend[i][0]]} {var2id[depend[i][1]]}', end='', file=ot) 
                        else:
                            print(f' {var2id[depend[i][1]]}', file=ot)
                        if i == len(depend) - 1:
                            print(' 0', file=ot)

                print(line, end='', file=ot)
                status = 1
        i += 1
    
    for e in var2id:
        if e not in exists and e not in univ:
            print(f'WARNING! {e} not quantified!', file=sys.stderr)


    f.close()
    ot.close()
    


dqasp2dqbf(['try.lp', 'try.lp'], 'game.dqdimacs')
