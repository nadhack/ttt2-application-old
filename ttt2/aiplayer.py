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

from game import *


class AiPlayer:
    def __init__(self, randomized = False, depth = 10):
        self._randomized = randomized
        self._max_depth = depth - 1

    @staticmethod
    def _alphabeta(board, alpha, beta, player, depth):
        if depth == 0 or board.is_full():
            return 0

        outcome = board.outcome()
        if outcome[0] == Outcome.TIE:
            return 0
        if outcome[0] != Outcome.NONE:
            return -depth * outcome[1].value * player

        best_score = -math.inf

        for move in board.available_cells():
            board[move] = Player(player)
            score = -AiPlayer._alphabeta(board, -beta, -alpha, -player, depth - 1)
            board[move] = Player.NONE
            if score > best_score:
                best_score = score
            if score > alpha:
                alpha = score
            if alpha >= beta:
                break

        return best_score

    def find_best_move(self, game):
        board = game.board
        player = game.currentPlayer.value
        best_move = -1
        best_score = -math.inf
        available = board.available_cells()

        if self._randomized:
            random.shuffle(available)

        for move in available:
            board[move] = Player(player)
            score = -AiPlayer._alphabeta(board, -math.inf, math.inf, -player, self._max_depth)
            board[move] = Player.NONE
            if score > best_score:
                best_score = score
                best_move = move

        return best_move
