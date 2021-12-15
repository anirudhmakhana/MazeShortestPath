move_pos(PrevX,PrevY,PrevX,Y) :- Y is PrevY-1. % move one position Up
move_pos(PrevX,PrevY,X,PrevY) :- X is PrevX+1. % move one position right
move_pos(PrevX,PrevY,PrevX,Y) :- Y is PrevY+1. % move one position down
move_pos(PrevX,PrevY,X,PrevY) :- X is PrevX-1. % move one position left

notvisited(_, []) :- !.

notvisited(X, [H|T]) :-
     X \= H,
    notvisited(X, T).

findGoalPath(X,Y,X,Y,GoalPath,GoalPath).

findGoalPath(PrevX,PrevY,X,Y,AlreadyVisitedPath,GoalPath) :- barrier(NextX,NextY), move_pos(PrevX,PrevY,NextX,NextY),

notvisited(barrier(NextX,NextY),AlreadyVisitedPath),

findGoalPath(NextX,NextY,X,Y,[barrier(NextX,NextY)|AlreadyVisitedPath],GoalPath).