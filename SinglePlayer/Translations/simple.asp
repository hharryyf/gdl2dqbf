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
% base(s4).
% base(s5).
% base(s6).
% base(s7).
% base(s8).
% base(s9).
% base(s10).
% base(s11).
% base(s12).
% base(s13).
% base(s14).
% base(s15).
base(control(x)).
base(control(o)).

legal(P, l) :- true(control(P)).
legal(P, r) :- true(control(P)).
legal(x, noop) :- true(control(o)).
legal(o, noop) :- true(control(x)).

next(s2) :- true(s1), does(x, l), not terminal.
next(s3) :- true(s1), does(x, r), not terminal.
%next(s4) :- true(s2), does(o, l), not terminal.
%next(s5) :- true(s2), does(o, r), not terminal.
%next(s6) :- true(s3), does(o, l), not terminal.
%next(s7) :- true(s3), does(o, r), not terminal.
%next(s8) :- true(s4), does(x, l), not terminal.
%next(s9) :- true(s4), does(x, r), not terminal.
%next(s10) :- true(s5), does(x, l), not terminal.
%next(s11) :- true(s5), does(x, r), not terminal.
%next(s12) :- true(s6), does(x, l), not terminal.
%next(s13) :- true(s6), does(x, r), not terminal.
%next(s14) :- true(s7), does(x, l), not terminal.
%next(s15) :- true(s7), does(x, r), not terminal.
%next(control(o)) :- true(control(x)), not terminal.
%next(control(x)) :- true(control(o)), not terminal.

terminal :- true(s2).
terminal :- true(s3).
goal(x,100) :- true(s2).

%terminal :- true(s8).
%terminal :- true(s9).
%terminal :- true(s10).
%terminal :- true(s11).
%terminal :- true(s12).
%terminal :- true(s13).
%terminal :- true(s14).
%terminal :- true(s15).

%goal(x,100) :- true(s8).
%goal(x,0) :- true(s9).
%goal(x,100) :- true(s10).
%goal(x,0) :- true(s11).
%goal(x,0) :- true(s12).
%goal(x,0) :- true(s13).
%goal(x,0) :- true(s14).
%goal(x,0) :- true(s15).


%goal(o,0) :- true(s8).
%goal(o,100) :- true(s9).
%goal(o,0) :- true(s10).
%goal(o,100) :- true(s11).
%goal(o,100) :- true(s12).
%goal(o,100) :- true(s13).
%goal(o,100) :- true(s14).
%goal(o,100) :- true(s15).

