from clyngor import ASP, solve

def asp_encoding(inputfile, T, player, opponent, outfile):
    f = open(outfile, 'w')
    # log-encoding
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
                        print(f'moveL2({opponent},{k+1}' + '), ' + f'legal({opponent}, {moveL[j]}), not terminal.', file=f)
                    else:
                        print(f'moveL2({opponent},{k+1}' + '), ' + f'legal({opponent}, {moveL[j]}), not terminal.', file=f)
                else:
                    print(f'moveL2({opponent},{k+1}' + '), ', end='', file=f)
        j += 1
    
    print(file=f)

    print(f'tdom(0..{T-1}).', file=f)
    print('{t1(I)} :- tdom(I).', file=f)
    print('{t2(I)} :- tdom(I).', file=f)
    print('{s1(F)} :- base(F).', file=f)
    print('{s2(F)} :- base(F).', file=f)
    print('{true(F)} :- base(F).', file=f)
    print('{true2(F)} :- base(F).', file=f)
    print('{moveL1(F)} :- ldom(M).', file=f)
    print('{moveL2(F)} :- ldom(M).', file=f)

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
    print('1 {does(R, M) : input(R, M)} 1 :- not terminal.', file=f)
    print(':- not legal(R, M), does(R, M).', file=f)
    print(':- succ, not neqsx, not next(F), true2(F), base(F).', file=f)
    print(':- succ, not neqsx, next(F), not true2(F), base(F).', file=f)
    print('neqsx :- base(F), true(F), not s2(F).', file=f)
    print('neqsx :- base(F), not true(F), s2(F).', file=f)
    
    print('leq(I, I) :- tdom(I). leq(I, I + 1) :- tdom(I + 1), tdom(I).', file=f)
    print('leq(I, K) :- leq(I, J), leq(J, K).', file=f)
    print('nsame(I) :- not t1(I), t2(I), tdom(I).', file=f)
    print('nsame(I) :- t1(I), not t2(I), tdom(I).', file=f)
    print('nsame(J) :- nsame(I), leq(I, J).', file=f)
    print('nopp(I) :- not t1(I), tdom(I).', file=f)
    print('nopp(I) :- t2(I), tdom(I).', file=f)
    print('nopp(J) :- nopp(I), leq(J, I).', file=f)
    print('succ :- nsame(I), not nsame(I-1), nopp(I), not nopp(I+1), t2(I), not t1(I), tdom(I).', file=f)


    f.close()

asp_encoding('SinglePlayer/Translations/tic-tac-toe.asp', 1, 'xplayer', 'oplayer', 'out.txt')
