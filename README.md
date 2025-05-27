# Zero Knowledge Chess Engine

* Establish the search tree
* Use a neural net to prune the search tree

Definition: Value network
V - f(board)

State(Board):

Extra State:
* Castle available X2
* En passant

Pieces(1+6*2-13):
* Blank
* Pawn
* Bishop
* Knight
* Queen
* Rook

8x8x4 + 4 = 260 bits