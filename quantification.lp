_exists(role(x), 0).
_exists(input(x,noop), 0).
_exists(input(x,l), 0).
_exists(ldom(2), 0).
_exists(input(x,r), 0).
_exists(tdom(0), 0).
_exists(base(s3), 0).
_exists(base(control(x)), 0).
_exists(input(o,r), 0).
_exists(base(control(o)), 0).
_exists(init(control(x)), 0).
_exists(input(o,l), 0).
_exists(ldom(1), 0).
_exists(base(s2), 0).
_exists(base(s1), 0).
_exists(leq(0,0), 0).
_exists(init(s1), 0).
_exists(input(o,noop), 0).
_exists(role(o), 0).
_forall(t1(T), 1) :- tdom(T).
_forall(s1(F), 1) :- base(F).
_forall(moveL1(M), 1) :- ldom(M).
_exists(legal(o,r), 2).
_exists(goal(x,100), 2).
_exists(next(s1), 2).
_exists(true(control(x)), 2).
_exists(legal(o,noop), 2).
_exists(next(control(o)), 2).
_exists(does(x,noop), 2).
_exists(legal(x,noop), 2).
_exists(next(control(x)), 2).
_exists(does(x,r), 2).
_exists(true(s3), 2).
_exists(legal(x,r), 2).
_exists(next(s3), 2).
_exists(true(s2), 2).
_exists(legal(x,l), 2).
_exists(true(control(o)), 2).
_exists(does(x,l), 2).
_exists(terminal, 2).
_exists(next(s2), 2).
_exists(legal(o,l), 2).
_exists(true(s1), 2).
_forall(moveL2(M), 3) :- ldom(M).
_exists(does(o,noop), 4).
_exists(does(o,l), 4).
_exists(does(o,r), 4).
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
_depend(true2(F), s2(G)) :- base(F), base(G).
_depend(true2(F), moveL2(M)) :- base(F), ldom(M).
