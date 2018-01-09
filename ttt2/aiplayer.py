# Copyright (c) 2018 Matthew T. Bucknall. All rights reserved.
#
# This work is licensed under the terms of the MIT license.
# See LICENSE file

import math
import random

from game import *


class AiPlayer:
    def __init__(self, randomized = False, depth = 10):
        self.randomized = randomized
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
        available = board.availableCells()

        if self.randomized:
            random.shuffle(available)

        for move in available:
            board[move] = Player(player)
            score = -AiPlayer._alphabeta(board, -math.inf, math.inf, -player, self._maxDepth)
            board[move] = Player.NONE
            if score > bestScore:
                bestScore = score
                bestMove = move

        return bestMove
