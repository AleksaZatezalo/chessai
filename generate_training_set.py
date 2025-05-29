#!/usr/bin/env python3

import os 
import chess.pgn
from state import State
import numpy as np

gn = 0
for fn in os.listdir("data"):
        pgn = open(os.path.join("data", fn))
        while 1:
                try:
                        game = chess.pgn.read_game(pgn)
                except Exception:
                        break
                print(f"parsing game %d" % gn)
                gn += 1
                result = game.headers['Result']
                board = game.board()
                value = {'1/2-1/2':0, '0-1':-1, '1-0':1}[game.headers['Result']]
                for i, move in enumerate(game.mainline_moves()):
                        board.push(move)
                        ser =  State(board).serialize()[:, :, 0]

                        #TODO: extract the board
                       # print(value, ser)
        break