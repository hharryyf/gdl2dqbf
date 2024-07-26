_forall(t1(T), 1) :- tdom(T).
_forall(s1(F), 1) :- base(F).
_forall(moveL1(M), 1) :- ldom(M).
_forall(moveL2(M), 3) :- ldom(M).
_exists(neqa, 4).
_forall(t2(T), 5) :- tdom(T).
_exists(succtime, 6).
_exists(nsame(T), 6) :- tdom(T).
_exists(nopp(T), 6) :- tdom(T).
_exists(neqt, 6).
_forall(s2(F), 7) :- base(F).
_exists(neqs, 8).
_exists(neqsx, 8).
_depend(true2(F), t2(T)) :- base(F), tdom(T).
_depend(true2(F), s2(F)) :- base(F), base(F).
_depend(true2(F), moveL2(M)) :- base(F), ldom(M).
