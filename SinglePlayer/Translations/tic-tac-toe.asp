timedomain(1..1).
role(xplayer).
role(oplayer).
index(1).
index(2).
index(3).
base(cell(X35226, X35227, b)) :- index(X35226), index(X35227), domdomain(2, X35226), domdomain(2, X35227).
base(cell(X35226, X35227, x)) :- index(X35226), index(X35227), domdomain(2, X35226), domdomain(2, X35227).
base(cell(X35226, X35227, o)) :- index(X35226), index(X35227), domdomain(2, X35226), domdomain(2, X35227).
base(control(X35226)) :- role(X35226), domdomain(4, X35226).
input(X35224, mark(X35227, X35228)) :- index(X35227), index(X35228), role(X35224), domdomain(4, X35224), domdomain(2, X35227), domdomain(2, X35228).
input(X35224, noop) :- role(X35224), domdomain(4, X35224).
init(cell(1, 1, b)).
init(cell(1, 2, b)).
init(cell(1, 3, b)).
init(cell(2, 1, b)).
init(cell(2, 2, b)).
init(cell(2, 3, b)).
init(cell(3, 1, b)).
init(cell(3, 2, b)).
init(cell(3, 3, b)).
init(control(xplayer)).
next(cell(X35226, X35227, x)) :- does(xplayer, mark(X35226, X35227)), true(cell(X35226, X35227, b)), not terminal, domdomain(2, X35226), domdomain(2, X35227).
next(cell(X35226, X35227, o)) :- does(oplayer, mark(X35226, X35227)), true(cell(X35226, X35227, b)), not terminal, domdomain(2, X35226), domdomain(2, X35227).
next(cell(X35226, X35227, X35228)) :- true(cell(X35226, X35227, X35228)), X35228 != b, not terminal, domdomain(2, X35226), domdomain(2, X35227), domdomain(3, X35228).
next(cell(X35226, X35227, b)) :- does(X35232, mark(X35235, X35236)), true(cell(X35226, X35227, b)), 1 { X35226 != X35235 ; X35227 != X35236 }, domdomain(4, X35232), domdomain(2, X35235), domdomain(2, X35236), not terminal, domdomain(2, X35226), domdomain(2, X35227).
next(control(xplayer)) :- true(control(oplayer)), not terminal.
next(control(oplayer)) :- true(control(xplayer)), not terminal.
row(X35224, X35225) :- true(cell(X35224, 1, X35225)), true(cell(X35224, 2, X35225)), true(cell(X35224, 3, X35225)), timedomain(1), domdomain(2, X35224), domdomain(3, X35225).
column(X35224, X35225) :- true(cell(1, X35224, X35225)), true(cell(2, X35224, X35225)), true(cell(3, X35224, X35225)), timedomain(1), domdomain(2, X35224), domdomain(3, X35225).
diagonal(X35224) :- true(cell(1, 1, X35224)), true(cell(2, 2, X35224)), true(cell(3, 3, X35224)), timedomain(1), domdomain(3, X35224).
diagonal(X35224) :- true(cell(1, 3, X35224)), true(cell(2, 2, X35224)), true(cell(3, 1, X35224)), timedomain(1), domdomain(3, X35224).
line(X35224) :- row(X35228, X35224), domdomain(2, X35228), timedomain(1), domdomain(3, X35224).
line(X35224) :- column(X35228, X35224), domdomain(2, X35228), timedomain(1), domdomain(3, X35224).
line(X35224) :- diagonal(X35224), timedomain(1), domdomain(3, X35224).
open :- true(cell(X35228, X35229, b)), domdomain(2, X35228), domdomain(2, X35229), timedomain(1).
legal(X35224, mark(X35227, X35228)) :- true(cell(X35227, X35228, b)), true(control(X35224)), timedomain(1), domdomain(4, X35224), domdomain(2, X35227), domdomain(2, X35228).
legal(xplayer, noop) :- true(control(oplayer)), timedomain(1).
legal(oplayer, noop) :- true(control(xplayer)), timedomain(1).
goal(xplayer, 100) :- line(x), timedomain(1).
goal(xplayer, 50) :- not line(x), not line(o), not open, timedomain(1).
goal(xplayer, 0) :- line(o), timedomain(1).
goal(oplayer, 100) :- line(o), timedomain(1).
goal(oplayer, 50) :- not line(x), not line(o), not open, timedomain(1).
goal(oplayer, 0) :- line(x), timedomain(1).
terminal :- line(x), timedomain(1).
terminal :- line(o), timedomain(1).
terminal :- not open, timedomain(1).
domdomain(1, cell).
domdomain(1, control).
domdomain(2, 1).
domdomain(2, 2).
domdomain(2, 3).
domdomain(3, b).
domdomain(3, o).
domdomain(3, x).
domdomain(4, oplayer).
domdomain(4, xplayer).
domdomain(5, 0).
domdomain(5, 50).
domdomain(5, 100).
domdomain(6, mark).
domdomain(6, noop).
