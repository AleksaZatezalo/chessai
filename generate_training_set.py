#!/usr/bin/env python3

import os 
import chess.pgn
from state import State
import numpy as np
import h5py

# pgn files in the data folder
def get_dataset(num_samples=None):
        X, Y = [], []
        gn = 0
        for fn in os.listdir("data"):
                pgn = open(os.path.join("data", fn))
                while 1:
                        try:
                                game = chess.pgn.read_game(pgn)
                        except Exception:
                                break
                        print(f"parsing game %d, got %d examples" % (gn, len(X)))
                        board = game.board()
                        value = {'1/2-1/2':0, '0-1':-1, '1-0':1}[game.headers['Result']]
                        for i, move in enumerate(game.mainline_moves()):
                                board.push(move)
                                ser =  State(board).serialize()[:, :, 0]
                                X.append(ser)
                                Y.append(value)
                        if num_samples is not None and len(X) > num_samples:
                                return X, Y
                        gn += 1
        X = np.array(X)
        Y = np.array(Y)
        return X, Y

if __name__ =="__main__":
       X, Y = get_dataset(1000)
       np.savez("processed/dataset.npz", X, Y)
#        h5 = h5py.File('processed/traingme.h5', 'w')
#        h5.create_dataset('X', X)
#        h5.create_dataset('X', Y)
#        h5.close()