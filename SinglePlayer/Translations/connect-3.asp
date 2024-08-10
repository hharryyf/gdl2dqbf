
role(xplayer).
role(oplayer).

init(control(xplayer)).

base(control(xplayer)).
base(control(oplayer)).
base(cell(X,Y,P)) :- role(P), x(X), y(Y).
input(xplayer, noop).
input(oplayer, noop).
input(P, drop(X)) :- x(X), role(P).

legal(xplayer, noop) :- true(control(oplayer)).
legal(xplayer, drop(X)) :- true(control(xplayer)), columnopen(X).
legal(oplayer, noop) :- true(control(xplayer)).
legal(oplayer, drop(X)) :- true(control(oplayer)), columnopen(X).


next(cell(X, 1, P)) :- does(P, drop(X)), columnempty(X), not terminal.

next(cell(X, Y2, P)) :- does(P, drop(X)), cellopen(X, Y2), succ(Y1, Y2), not cellopen(X, Y1), not terminal.

next(cell(X, Y, P)) :- true(cell(X, Y, P)), not terminal.

next(control(xplayer)) :- true(control(oplayer)), not terminal.

next(control(oplayer)) :- true(control(xplayer)), not terminal.


terminal :- line(xplayer).

terminal :- line(oplayer).

terminal :- not boardopen.


goal(xplayer, 100) :- line(xplayer).

goal(xplayer, 50) :- not line(xplayer), not line(oplayer), not boardopen.

goal(xplayer, 0) :- line(oplayer).

goal(xplayer, 0) :- not line(xplayer), not line(oplayer), boardopen.

goal(oplayer, 100) :- line(oplayer).

goal(oplayer, 50) :- not line(xplayer), not line(oplayer), not boardopen.

goal(oplayer, 0) :- line(xplayer).

goal(oplayer, 0) :- not line(xplayer), not line(oplayer), boardopen.


cellopen(X, Y) :- x(X), y(Y), not true(cell(X, Y, xplayer)), not true(cell(X, Y, oplayer)).

columnopen(X) :- cellopen(X, 4).

columnempty(X) :- cellopen(X, 1).

boardopen :- x(X), columnopen(X).

line(P) :- true(cell(X1, Y, P)), succ(X1, X2), succ(X2, X3), true(cell(X2, Y, P)), true(cell(X3, Y, P)).

line(P) :- true(cell(X, Y1, P)), succ(Y1, Y2), succ(Y2, Y3), true(cell(X, Y2, P)), true(cell(X, Y3, P)).

line(P) :- true(cell(X1, Y1, P)), succ(X1, X2), succ(X2, X3), succ(Y1, Y2), succ(Y2, Y3), true(cell(X2, Y2, P)), true(cell(X3, Y3, P)).


line(P) :- true(cell(X1, Y3, P)), succ(X1, X2), succ(X2, X3), succ(Y1, Y2), succ(Y2, Y3), true(cell(X2, Y2, P)), true(cell(X3, Y1, P)).
    

succ(1, 2).
succ(2, 3).
succ(3, 4).

x(1..4).
y(1..4).