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

import unittest

from game import *
from aiplayer import *


class TestAiPlayer(unittest.TestCase):
    def test_self_play(self):
        for n in range(0, 100):
            g = Game(Player.NAUGHT if n & 1 else Player.CROSS)
            b = g.board
            ai = AiPlayer(True)

            while True:
                outcome = b.outcome()
                if outcome[0] != Outcome.NONE:
                    break
                move = ai.find_best_move(g)
                b[move] = g.current_player
                g.toggle_player()

            self.assertEqual((Outcome.TIE, Player.NONE), outcome)
