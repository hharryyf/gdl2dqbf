init(control(x)).
init(t(0)).
role(x).
role(o).
input(P, l) :- role(P).
input(P, r) :- role(P).
input(P, noop) :- role(P).
base(t(0)).
base(t(1)).
base(t(2)).
base(t(3)).
base(control(x)).
base(control(o)).

legal(P, l) :- true(control(P)).
legal(P, r) :- true(control(P)).
legal(x, noop) :- true(control(o)).
legal(o, noop) :- true(control(x)).

succ(0,1).
succ(1,2).
succ(2,3).

next(t(Y)) :- true(t(X)), does(P, l), role(P), not terminal, succ(X, Y).

next(t(Y)) :- true(t(X)), does(P, r), role(P), not terminal, succ(X, Y).

next(t(0)) :- true(t(X)), does(P, r), role(P), not terminal.


next(control(o)) :- true(control(x)), not terminal.
next(control(x)) :- true(control(o)), not terminal.

terminal :- true(t(3)).

goal(x,100) :- true(t(3)), not true(t(2)), not true(t(1)), not true(t(0)).


goal(x,100) :- true(t(3)), true(t(2)), not true(t(1)), not true(t(0)).

