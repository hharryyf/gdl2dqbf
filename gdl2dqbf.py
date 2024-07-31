from clyngor import ASP, solve
from dqasp2dqbf import dqasp2dqbf
import os
import sys
import queue

def asp_encoding(inputfile, T, player, opponent, outfile):
    f = open(outfile, 'w')
    ################ log-encoding #################
    answer = solve(inputfile, inline='#show input/2.')
    moveL = set()
    for ans in answer:
        for c in ans:
            if c[1][0] == opponent:
                moveL.add(c[1][1])
    moveL = list(moveL)
    moveL.sort()
    tol, lenl = 0, len(moveL)
    while (1 << tol) < lenl:
        tol += 1

    print(f'ldom(1..{tol}).', file=f)
    print('% log-encoding', file=f)

    j = 0
    for i in range(0, 1 << tol):
        if j < len(moveL):
            print(f'does({opponent}, {moveL[j]}) :- ', end='', file=f)
            for k in range(0, tol):
                if ((i >> k) & 1) == 0:
                    print('not ', end='', file=f)
                if k == tol - 1:
                    if i == 0:
                        print(f'moveL2({k+1}' + '), ' + f'legal({opponent}, {moveL[j]}), not terminal.', file=f)
                    else:
                        print(f'moveL2({k+1}' + '), ' + f'legal({opponent}, {moveL[j]}), not terminal.', file=f)
                else:
                    print(f'moveL2({k+1}' + '), ', end='', file=f)
        j += 1
    
    print(file=f)
    ####################################################
    print(f'tdom(0..{T-1}).', file=f)
    print('{t1(I)} :- tdom(I).', file=f)
    print('{t2(I)} :- tdom(I).', file=f)
    print('{s1(F)} :- base(F).', file=f)
    print('{s2(F)} :- base(F).', file=f)
    print('{true(F)} :- base(F).', file=f)
    print('{true2(F)} :- base(F).', file=f)
    print('{moveL1(M)} :- ldom(M).', file=f)
    print('{moveL2(M)} :- ldom(M).', file=f)

    print(':- ', end='', file=f)
    for i in range(0, T):
        print(f'not t1({i}), ', end='', file=f)
    print('base(F), not true(F), init(F).', file=f)

    print(':- ', end='', file=f)
    for i in range(0, T):
        print(f'not t1({i}), ', end='', file=f)
    print('base(F), true(F), not init(F).', file=f)

    print(':- ', end='', file=f)
    for i in range(0, T):
        print(f't1({i}), ', end='', file=f)
    print('not terminal.', file=f)

    print(':- ', end='', file=f)
    for i in range(0, T):
        print(f't1({i}), ', end='', file=f)
    print(f'not goal({player}, 100).', file=f)

    print('neqt :- t1(T), not t2(T), tdom(T).', file=f)
    print('neqt :- not t1(T), t2(T), tdom(T).', file=f)
    print('neqs :- s1(F), not s2(F), base(F).', file=f)
    print('neqs :- not s1(F), s2(F), base(F).', file=f)
    print('neqa :- moveL1(M), not moveL2(M), ldom(M).', file=f)
    print('neqa :- not moveL1(M), moveL2(M), ldom(M).', file=f)
    print(':- not neqt, not neqs, not neqa, base(F), true(F), not true2(F).', file=f)
    print(':- not neqt, not neqs, not neqa, base(F), not true(F), true2(F).', file=f)
    print('1 {does(R, M) : input(R, M)} 1 :- not terminal, role(R).', file=f)
    print(':- not legal(R, M), does(R, M).', file=f)
    print(':- succtime, not neqsx, not next(F), true2(F), base(F).', file=f)
    print(':- succtime, not neqsx, next(F), not true2(F), base(F).', file=f)
    print('neqsx :- base(F), true(F), not s2(F).', file=f)
    print('neqsx :- base(F), not true(F), s2(F).', file=f)
    print('next(F) :- terminal, base(F), true(F).', file=f)
    
    print('leq(I, I) :- tdom(I). leq(I, I + 1) :- tdom(I + 1), tdom(I).', file=f)
    print('leq(I, K) :- leq(I, J), leq(J, K).', file=f)
    print('nsame(I) :- not t1(I), t2(I), tdom(I).', file=f)
    print('nsame(I) :- t1(I), not t2(I), tdom(I).', file=f)
    print('nsame(J) :- nsame(I), leq(I, J).', file=f)
    print('nopp(I) :- not t1(I), tdom(I).', file=f)
    print('nopp(I) :- t2(I), tdom(I).', file=f)
    print('nopp(J) :- nopp(I), leq(J, I).', file=f)
    print('succtime :- nsame(I), not nsame(I-1), nopp(I), not nopp(I+1), t2(I), not t1(I), tdom(I).', file=f)

    f.close()

# helper function, return all atoms that depend on predicate_list (given as a prefix), 
# and not in blacklist, given the list of the smodels file
def get_dependency(predicate_list, blacklist, smodelfile):
    # code for building the dependency
    f = open(smodelfile, 'r')
    status = 0
    edge = set()
    graph = {}
    var2id = {}
    id2var = {}
    result = []
    for line in f:
        line = line.strip()
        if line == '0':
            status += 1
            continue
        if status == 0:
            line = list(map(int, line.split()))
            if line[0] == 1:
                    head = line[1]
                    for i in range(4, len(line)):
                        if line[i] == 1:
                            print('Unexpected Error')
                            exit(1)
                        edge.add((line[i], head))
            # head number_of_lit number_of_neg_lit bound [negative lit] [positive lit]
            elif line[0] == 2:
                head = line[1]
                for i in range(5, len(line)):
                    edge.add((line[i], head))
            # number_of_head [head] number_of_lit number_of_neg_lit [negative lit] [positive lit]
            elif line[0] == 3:
                head_num = line[1]
                head = []
                for i in range(2, head_num + 2):
                    head.append(line[i])
                # this part can be optimized
                for i in range(head_num + 4, len(line)):
                    for h in head:
                        edge.add((line[i], h))
            else:
                print('ERROR! Cannot handle rules of type >= 4', file=sys.stderr)
                exit(1)
        elif status == 1:
            line = line.split()
            vid, atom = int(line[0]), line[1]
            var2id[atom] = vid 
            id2var[vid] = atom
    
    if len(predicate_list) == 0:
        for e in var2id.keys():
            ok = True
            for bad in blacklist:
                if e[:len(bad)] == bad:
                    ok = False
                    break
            if ok == True:
                result.append(e)
    else:
        for e in edge:
            if e[0] not in graph:
                graph[e[0]] = []
            graph[e[0]].append(e[1])
        
        # use BFS to get the dependencies
        q = queue.Queue()
        visited = set()
        for v, name in id2var.items():
            for s in predicate_list:
                if name[:len(s)] == s:
                    q.put(v)
        

        while q.empty() == False:
            curr = q.get()
            if curr in visited:
                continue 
            visited.add(curr)
            if curr in id2var:
                ok = True
                name = id2var[curr]
                for bad in blacklist:
                    if name[:len(bad)] == bad:
                        ok = False
                        break
                if ok == True:
                    result.append(name)

            if curr in graph:
                for v in graph[curr]:
                    if v not in visited:
                        q.put(v)

    f.close()

    return result

def quantification(aspfilelist, player, opponent, outfile):
    aspfilelist = ' '.join(aspfilelist)
    cmd = f'clingo --output=smodels {aspfilelist}  > encoding.smodels'
    os.system(f"bash -c '{cmd}'")    
    
    
    
    special = ['nopp', 'nsame', 'succtime', 'neqt', 'neqa', 'neqsx', 'neqs', 'true2', 't1', 't2', 's1', 'moveL1', 'moveL2', 's2']
    all_atom = set(get_dependency([], special, 'encoding.smodels'))
    does_x = set(get_dependency(['does(','true('], special, 'encoding.smodels'))
    does_o = set(get_dependency([f'does({opponent},'], special, 'encoding.smodels'))
    #print(all_atom)
    #print(does_x)
    #print(does_o)
    outfile = open(outfile, 'w')
    
    # all static atoms that are not special/univ are quantified existentially at level 0
    for e in all_atom:
        if e not in does_x:
            print(f'_exists({e}, 0).', file=outfile)
    print('_forall(t1(T), 1) :- tdom(T).', file=outfile)
    print('_forall(s1(F), 1) :- base(F).', file=outfile)
    print('_forall(moveL1(M), 1) :- ldom(M).', file=outfile)
    # all atoms that depend on true and does_x but not moveL2, existentially at level 2
    for e in does_x:
        if e not in does_o:
            print(f'_exists({e}, 2).', file=outfile)
    print('_forall(moveL2(M), 3) :- ldom(M).', file=outfile)
    # all atoms that depend on does_o, existentially at level 4
    for e in does_o:
        print(f'_exists({e}, 4).', file=outfile)
    print('_exists(neqa, 4).', file=outfile)
    print('_forall(t2(T), 5) :- tdom(T).', file=outfile)
    print('_exists(succtime, 6).', file=outfile)
    print('_exists(nsame(T), 6) :- tdom(T).', file=outfile)
    print('_exists(nopp(T), 6) :- tdom(T).', file=outfile)
    print('_exists(neqt, 6).', file=outfile)
    print('_forall(s2(F), 7) :- base(F).', file=outfile)
    print('_exists(neqs, 8).', file=outfile)
    print('_exists(neqsx, 8).', file=outfile)
    # specify partial dependencies
    print('_depend(true2(F), t2(T)) :- base(F), tdom(T).', file=outfile)
    print('_depend(true2(F), s2(F)) :- base(F).', file=outfile)
    print('_depend(true2(F), moveL2(M)) :- base(F), ldom(M).', file=outfile)
    outfile.close()

def gdl2dqasp(inputfile, T, player, opponent, outfile):
    asp_encoding(inputfile, T, player, opponent, 'encoding.asp')
    quantification([inputfile, 'encoding.asp'], player, opponent, 'quantification.asp')
    dqasp2dqbf([inputfile, 'encoding.asp', 'quantification.asp'], outfile)


if __name__ == "__main__":
    if len(sys.argv) != 6:
        print('Usage: python [path to the game.asp] [log(depth) of the game] [first player] [second player] [output file]')
        exit(1)
    gdl2dqasp(sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4], sys.argv[5])
#gdl2dqasp('SinglePlayer/Translations/tic-tac-toe.asp', 1, 'xplayer', 'oplayer', 'out.txt')
