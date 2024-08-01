
tdom(0..0).

_exists(tdom(0), 0).
_forall(tdom(1), 1).
_depend(tdom(2), tdom(1)).


{t1(I)} :- tdom(I).
{t2(I)} :- tdom(I).
leq(I, I) :- tdom(I).
leq(I, I+1) :- tdom(I+1), tdom(I).
leq(I, K) :- leq(I, J), leq(J, K).

nsame(I) :- not t1(I), t2(I), tdom(I).
nsame(I) :- t1(I), not t2(I), tdom(I).
nopp(I) :- not t1(I), tdom(I).
nopp(I) :- t2(I), tdom(I).
nsame(J) :- nsame(I), leq(I, J).
nopp(J) :- nopp(I), leq(J, I).

succ :- nsame(I), not nsame(I-1), nopp(I), not nopp(I+1), t2(I), not t1(I), tdom(I).

:- not succ.
