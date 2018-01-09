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

import sys

from enum import Enum


_player_symbols = ['O', ' ', 'X']


class Player(Enum):
    NAUGHT = -1
    NONE = 0
    CROSS = 1

    def __str__(self):
        return _player_symbols[self.value + 1]

    def opponent(self):
        return Player(self.value * -1)


class Outcome(Enum):
    NONE = 0
    TIE = 1
    WIN_012 = 2
    WIN_345 = 3
    WIN_678 = 4
    WIN_036 = 5
    WIN_147 = 6
    WIN_258 = 7
    WIN_048 = 8
    WIN_246 = 9


class Board:
    def __init__(self):
        self._state = [Player.NONE] * 9

    def __setitem__(self, item, value):
        self._state[item] = value

    def __getitem__(self, item):
        return self._state[item]

    def available_cells(self):
       return [i for i, cell in enumerate(self._state) if cell == Player.NONE]

    def is_full(self):
        return self._state.count(Player.NONE) == 0

    def outcome(self):
        if self.is_full():
            return Outcome.TIE, Player.NONE
        s = self._state
        if s[0] != Player.NONE and s[0] == s[1] == s[2]:
            return Outcome.WIN_012, s[0]
        if s[3] != Player.NONE and s[3] == s[4] == s[5]:
            return Outcome.WIN_345, s[3]
        if s[6] != Player.NONE and s[6] == s[7] == s[8]:
            return Outcome.WIN_678, s[6]
        if s[0] != Player.NONE and s[0] == s[3] == s[6]:
            return Outcome.WIN_036, s[0]
        if s[1] != Player.NONE and s[1] == s[4] == s[7]:
            return Outcome.WIN_147, s[1]
        if s[2] != Player.NONE and s[2] == s[5] == s[8]:
            return Outcome.WIN_258, s[2]
        if s[0] != Player.NONE and s[0] == s[4] == s[8]:
            return Outcome.WIN_048, s[0]
        if s[2] != Player.NONE and s[2] == s[4] == s[6]:
            return Outcome.WIN_246, s[2]
        return Outcome.NONE, Player.NONE

    def dump(self, f = sys.stdout):
        s = self
        f.write(" {0} | {1} | {2}\n".format(s[0], s[1], s[2]))
        f.write("---+---+---\n")
        f.write(" {0} | {1} | {2}\n".format(s[3], s[4], s[5]))
        f.write("---+---+---\n")
        f.write(" {0} | {1} | {2}\n\n".format(s[6], s[7], s[8]))
