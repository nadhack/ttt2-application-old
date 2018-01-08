# MIT License
#
# Copyright (c) 2018 Matthew T. Bucknall
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import math
import random

from board import *
from game import *


# TODO: This doesn't work!!!
class AiPlayer:
    def __init__(self, depth = 10):
        self._maxDepth = depth - 1

    @staticmethod
    def _alphabeta(board, alpha, beta, player, depth):
        if depth == 0 or board.isFull():
            return 0

        outcome = board.outcome()
        if outcome[0] == Outcome.TIE:
            return 0
        if outcome[0] != Outcome.NONE:
            return -depth * outcome[1].value * player

        bestScore = -math.inf

        for move in board.availableCells():
            board[move] = Player(player)
            score = -AiPlayer._alphabeta(board, -beta, -alpha, -player, depth - 1)
            board[move] = Player.NONE
            if score > bestScore:
                bestScore = score
            if score > alpha:
                alpha = score
            if alpha >= beta:
                break

        return bestScore


    def findBestMove(self, game):
        board = game.board
        player = game.currentPlayer.value
        bestMove = -1
        bestScore = -math.inf
        print("Player", player)
        for move in board.availableCells():
            board[move] = Player(player)
            score = AiPlayer._alphabeta(board, -math.inf, math.inf, player, self._maxDepth)
            board[move] = Player.NONE
            if score > bestScore:
                bestScore = score
                bestMove = move

        return bestMove
