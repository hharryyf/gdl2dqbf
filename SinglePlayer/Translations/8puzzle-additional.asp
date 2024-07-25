{y(1)}.
{y(2)}.
{y(3)}.
{y(4)}.
{y(5)}.

:- init(F), not true(F, i).
:- not init(F), true(F, i).

:- not goal(player, 100, g).
:- not terminal(g).

timedomain(0..5).
timedomain(g).
timedomain(i).
mdom(player, A) :- input(player, A).
mdom(player, dummy).

{true(F, T)} :- base(F), timedomain(T).
1 {does(player, A, T) : mdom(player, A)} 1 :- timedomain(T).

:- not legal(player, A, T), does(player, A, T), timedomain(T), mdom(player, A).

legal(player, dummy, T) :- timedomain(T), terminal(T).

next(F, T) :- true(F, T), terminal(T), timedomain(T).

:- base(F), next(F, i), not true(F, 0) , not y(1), not y(2), not y(3), not y(4), not y(5).
:- base(F), not next(F, i), true(F, 0) , not y(1), not y(2), not y(3), not y(4), not y(5).
:- base(F), next(F, 0), not true(F, g) , y(1), y(2), y(3), y(4), y(5).
:- base(F), not next(F, 0), true(F, g) , y(1), y(2), y(3), y(4), y(5).

:- not y(1), base(F), next(F, 0), not true(F, 1).
:- not y(1), base(F), not next(F, 0), true(F, 1).

:- y(1), base(F), next(F, 0), not true(F, 1).
:- y(1), base(F), not next(F, 0), true(F, 1).

:- not y(2), y(1), base(F), next(F, 0), not true(F, 2).
:- not y(2), y(1), base(F), not next(F, 0), true(F, 2).

:- y(2), not y(1), base(F), next(F, 0), not true(F, 2).
:- y(2), not y(1), base(F), not next(F, 0), true(F, 2).

:- not y(3), y(1), y(2), base(F), next(F, 0), not true(F, 3).
:- not y(3), y(1), y(2), base(F), not next(F, 0), true(F, 3).

:- y(3), not y(1), not y(2), base(F), next(F, 0), not true(F, 3).
:- y(3), not y(1), not y(2), base(F), not next(F, 0), true(F, 3).

:- not y(4), y(1), y(2), y(3), base(F), next(F, 0), not true(F, 4).
:- not y(4), y(1), y(2), y(3), base(F), not next(F, 0), true(F, 4).

:- y(4), not y(1), not y(2), not y(3), base(F), next(F, 0), not true(F, 4).
:- y(4), not y(1), not y(2), not y(3), base(F), not next(F, 0), true(F, 4).

:- not y(5), y(1), y(2), y(3), y(4), base(F), next(F, 0), not true(F, 5).
:- not y(5), y(1), y(2), y(3), y(4), base(F), not next(F, 0), true(F, 5).

:- y(5), not y(1), not y(2), not y(3), not y(4), base(F), next(F, 0), not true(F, 5).
:- y(5), not y(1), not y(2), not y(3), not y(4), base(F), not next(F, 0), true(F, 5).

