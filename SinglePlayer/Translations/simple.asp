init(control(x)).
init(s1).
role(x).
role(o).

input(P, l) :- role(P).
input(P, r) :- role(P).
input(P, noop) :- role(P).
base(s1).
base(s2).
base(s3).
base(control(x)).
base(control(o)).

legal(P, l) :- true(control(P)).
legal(P, r) :- true(control(P)).
legal(x, noop) :- true(control(o)).
legal(o, noop) :- true(control(x)).

next(s2) :- true(s1), does(x, l), not terminal.
next(s3) :- true(s1), does(x, r), not terminal.
next(control(o)) :- true(control(x)), not terminal.
next(control(x)) :- true(control(o)), not terminal.

terminal :- true(s2).
terminal :- true(s3).
goal(x,100) :- true(s2).

