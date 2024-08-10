import sys

f = open(sys.argv[1], 'r')
i = 0
numvar = 0
numclause = 0

univ = set()
exist = set()
cnt = 0

for linep in f:
    line = linep.split()
    if i == 0:
        if line[0].strip() != 'p' or line[1].strip() != 'cnf':
            print(f'Invalid first line {linep}')
            exit(1)
        numvar = int(line[2])
        numclause = int(line[3])
    else:
        if line[0] == 'a':
            for j in range(1, len(line)):
                if j == len(line) - 1 and line[j].strip() != '0':
                    print(f'Invalid quantifier prefix {linep}')
                    exit(1)
                if j < len(line) - 1 and (int(line[j]) > numvar or int(line[j]) <= 0):
                    print(f'Invalid quantifier prefix {linep}, variables not in range [1, {numvar}]')
                    exit(1)
                if j < len(line) - 1:
                    if int(line[j]) in univ:
                        print(f'Invalid quantifier prefix {linep}, {line[j]} was quantified twice')
                        exit(1)
                    if int(line[j]) in exist:
                        print(f'Invalid quantifier prefix {linep}, {line[j]} was quantified both existentially and universally')
                        exit(1)
                    univ.add(int(line[j]))
        elif line[0] == 'd':
            for j in range(1, len(line)):
                if j == len(line) - 1 and line[j].strip() != '0':
                    print(f'Invalid quantifier prefix {linep}')
                    exit(1)
                if j < len(line) - 1 and (int(line[j]) > numvar or int(line[j]) <= 0):
                    print(f'Invalid quantifier prefix {linep}, variables not in range [1, {numvar}]')
                    exit(1)
                if j < len(line) - 1:
                    if j == 1 and int(line[j]) in univ:
                        print(f'Invalid quantifier prefix {linep}, {line[j]} was quantified both existentially and universally')
                        exit(1)
                    if j > 1 and int(line[j]) not in univ:
                        print(f'Invalid quantifier prefix {linep}, partial dependency can only depend on universal variables, but {line[j]} is existential')
                        exit(1)
                    if j == 1:
                        exist.add(int(line[1]))
        elif line[0] == 'e':
            for j in range(1, len(line)):
                if j == len(line) - 1 and line[j].strip() != '0':
                    print(f'Invalid quantifier prefix {linep}')
                    exit(1)
                if j < len(line) - 1 and (int(line[j]) > numvar or int(line[j]) <= 0):
                    print(f'Invalid quantifier prefix {linep}, variables not in range [1, {numvar}]')
                    exit(1)
                if j < len(line) - 1:
                    if int(line[j]) in exist:
                        print(f'Invalid quantifier prefix {linep}, {line[j]} was quantified twice')
                        exit(1)
                    if int(line[j]) in univ:
                        print(f'Invalid quantifier prefix {linep}, {line[j]} was quantified both existentially and universally')
                        exit(1)
                    exist.add(int(line[j]))
        else:
            cnt += 1
            for j in range(1, len(line)):
                if j == len(line) - 1 and line[j].strip() != '0':
                    print(f'Invalid clause {linep}')
                    exit(1)
                if j < len(line) - 1 and (abs(int(line[j])) > numvar or abs(int(line[j])) == 0):
                    print(f'Invalid clause {linep}, variables not in range [1, {numvar}]')
                    exit(1)
    i += 1
if cnt != numclause:
    print(f'Invalid number of clauses should be {numclause}, actual {cnt}')
    exit(1)                

f.close()