ldom(1..3).
% log-encoding
does(oplayer, drop(1)) :- not moveL2(1), not moveL2(2), not moveL2(3), legal(oplayer, drop(1)), not terminal.
does(oplayer, drop(2)) :- moveL2(1), not moveL2(2), not moveL2(3), legal(oplayer, drop(2)), not terminal.
does(oplayer, drop(3)) :- not moveL2(1), moveL2(2), not moveL2(3), legal(oplayer, drop(3)), not terminal.
does(oplayer, drop(4)) :- moveL2(1), moveL2(2), not moveL2(3), legal(oplayer, drop(4)), not terminal.
does(oplayer, noop) :- not moveL2(1), not moveL2(2), moveL2(3), legal(oplayer, noop), not terminal.

tdom(0..3).
{t1(I)} :- tdom(I).
{t2(I)} :- tdom(I).
{s1(F)} :- base(F).
{s2(F)} :- base(F).
{true(F)} :- base(F).
{true2(F)} :- base(F).
{moveL1(M)} :- ldom(M).
{moveL2(M)} :- ldom(M).
:- not t1(0), not t1(1), not t1(2), not t1(3), base(F), not true(F), init(F).
:- not t1(0), not t1(1), not t1(2), not t1(3), base(F), true(F), not init(F).
:- t1(0), t1(1), t1(2), t1(3), not terminal.
:- t1(0), t1(1), t1(2), t1(3), not goal(xplayer, 100).
neqt :- t1(T), not t2(T), tdom(T).
neqt :- not t1(T), t2(T), tdom(T).
neqs :- s1(F), not s2(F), base(F).
neqs :- not s1(F), s2(F), base(F).
neqa :- moveL1(M), not moveL2(M), ldom(M).
neqa :- not moveL1(M), moveL2(M), ldom(M).
:- not neqt, not neqs, not neqa, base(F), true(F), not true2(F).
:- not neqt, not neqs, not neqa, base(F), not true(F), true2(F).
1 {does(R, M) : input(R, M)} 1 :- not terminal, role(R).
:- not legal(R, M), does(R, M).
:- succtime, not neqsx, not next(F), true2(F), base(F).
:- succtime, not neqsx, next(F), not true2(F), base(F).
neqsx :- base(F), true(F), not s2(F).
neqsx :- base(F), not true(F), s2(F).
next(F) :- terminal, base(F), true(F).
leq(I, I) :- tdom(I). leq(I, I + 1) :- tdom(I + 1), tdom(I).
leq(I, K) :- leq(I, J), leq(J, K).
nsame(I) :- not t1(I), t2(I), tdom(I).
nsame(I) :- t1(I), not t2(I), tdom(I).
nsame(J) :- nsame(I), leq(I, J).
nopp(I) :- not t1(I), tdom(I).
nopp(I) :- t2(I), tdom(I).
nopp(J) :- nopp(I), leq(J, I).
succtime :- nsame(I), not nsame(I-1), nopp(I), not nopp(I+1), t2(I), not t1(I), tdom(I).
