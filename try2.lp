
tdom(0..1).
{t1(I)} :- tdom(I).
{t2(I)} :- tdom(I).
neqt :- t1(T), not t2(T), tdom(T).
neqt :- not t1(T), t2(T), tdom(T).
