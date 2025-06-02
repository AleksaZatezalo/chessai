# Zero Knowledge Chess Engine

Zero Knowledge Chess Engine trained on pgn games. Coded alongside a George Hotz Twitch Stream linked below:

* (Chess Engine Part 1)[https://www.youtube.com/watch?v=RFaFmkCEGEs&t=3649s]
* (Chess Engine Part 2)[https://www.youtube.com/watch?v=aXxoYVKXebI]
* (Chess Engine Part 3)[https://www.youtube.com/watch?v=ZulvfKPSfKg]

The neural net uses deep learning to learn to play chess.

## Notes (To Be Deleted)
* Establish the search tree
* Use a neural net to prune the search tree

Definition: Value network
V - f(board)

What is V?
V = -1 black wins board state
V = 0 draw state
V = 1 white wins board state

Should we fix the value of the inital board state?

Simpler:
All positions where white wins = 1
All positions where draw = 0
All positions where black wins = -1 

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

8x8x5 + 4 = 260 bits