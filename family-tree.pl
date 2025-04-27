% --- Facts ---

parent(pam, bob).
parent(tom, bob).
parent(tom, liz).
parent(bob, ann).
parent(bob, pat).
parent(pat, jim).

female(pam).
female(liz).
female(ann).
female(pat).

male(tom).
male(bob).
male(jim).

% --- Rules ---

% offspring(Y, X) means Y is a offspring of X
offspring(Y, X) :- parent(X, Y).

% mother(X, Y) means X is a mother of Y
mother(X, Y) :- parent(X, Y), female(X).

% grandparent(X, Z) means X is a parent of Z
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).

% sister(X, Y) means X is the sister of Y.
sister(X, Y) :- parent(Z, X),parent(Z, Y),female(X), X \= Y.

% predecessor(X, Z) means X is a predecessor (ancestor) of Z

% Rule 1: direct parent
predecessor(X, Z) :- parent(X, Z).

% Rule 2: ancestor through intermediate nodes
predecessor(X, Z) :- parent(X, Y),parent(Y, Z).

 