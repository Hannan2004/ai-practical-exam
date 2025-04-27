% State is represented as state(Jug4, Jug3)

% Goal: exactly 2 liters in the 4-liter jug
goal(state(2, _)).

% Moves:
move(state(_, Jug3), state(4, Jug3), 'Fill 4-liter jug').
move(state(Jug4, _), state(Jug4, 3), 'Fill 3-liter jug').

move(state(Jug4, Jug3), state(0, Jug3), 'Empty 4-liter jug').
move(state(Jug4, Jug3), state(Jug4, 0), 'Empty 3-liter jug').

move(state(Jug4, Jug3), state(NewJug4, NewJug3), 'Pour 4-liter into 3-liter') :-
    Total is Jug4 + Jug3,
    (Total =< 3 -> NewJug4 = 0, NewJug3 = Total
    ; NewJug4 is Total - 3, NewJug3 = 3).

move(state(Jug4, Jug3), state(NewJug4, NewJug3), 'Pour 3-liter into 4-liter') :-
    Total is Jug4 + Jug3,
    (Total =<= 4 -> NewJug4 = Total, NewJug3 = 0
    ; NewJug4 = 4, NewJug3 is Total - 4).

% Solving
solve(State, _, []) :- goal(State).
solve(State, Visited, [Action|Actions]) :-
    move(State, NextState, Action),
    \+ member(NextState, Visited),  % avoid visiting already visited states
    solve(NextState, [NextState|Visited], Actions).

% Entry point
water_jug(Steps) :-
    solve(state(0,0), [state(0,0)], Steps).
