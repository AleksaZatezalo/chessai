#!/usr/bin/env python3

import os 
import chess.pgn

for fn in os.listdir("data"):
        pgn = open(os.path.join("data", fn))
        while 1:
                try:
                        game = chess.pgn.read_game(pgn)
                except Exception:
                        break
                result = game.headers['Result']
                board = game.board()
                for move in game.mainline_moves():
                        board.push(move)
                        print(board)
                print(result)
        exit(0)
