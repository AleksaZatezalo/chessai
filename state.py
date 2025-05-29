#!/usr/bin/env python3
"""
Author: Aleksa Zatezalo
Date: May 2025
Description: Represents a chess board's state.
"""

import chess
import numpy as np

class State():
    def __init__(self, board=None):
        if board is None:
            self.board = chess.Board()
        else:
            self.board = board

    def serialize(self):
        state = np.zeros((8, 8, 5))
        state[:, :, 4] = (self.board.turn*1.0)
        print(state)
        #257 bits according to readme
        pp = self.board.shredder_fen()
        return pp

    def edges(self):
        return list(self.board.legal_moves)

    def value(self):
        # TODO: add neural net here
        return 1
    
if __name__ == "__main__":
    s = State()
    print(s.edges())