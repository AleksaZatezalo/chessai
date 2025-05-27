#!/usr/bin/env python3
"""
Author: Aleksa Zatezalo
Date: May 2025
Description: Represents a chess board's state.
"""

import chess

class State():
    def __init__(self):
        self.board = chess.Board()

    def edges(self):
        return list(self.board.legal_moves)

    def value(self):
        return 1
    
if __name__ == "__main__":
    s = State()
    print(s.edges())