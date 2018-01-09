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

from board import *


class TestBoard(unittest.TestCase):
    def test_available_empty(self):
        b = Board()

        self.assertEqual(b.available_cells(), [0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_available_n(self):
        b = Board()
        a = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        for i in range(0, 9):
            b[i] = Player.NAUGHT
            del a[0]
            self.assertEqual(a, b.available_cells())

    def test_is_full(self):
        b = Board()
        for i in range(0, 9):
            b[i] = Player.CROSS
        self.assertTrue(b.is_full())

    def test_no_outcome(self):
        b = Board()
        for i in range(0, 9):
            self.assertEqual((Outcome.NONE, Player.NONE), b.outcome())
            if i & 2:
                b[i] = Player.NAUGHT
            else:
                b[i] = Player.CROSS

    def test_tie(self):
        b = Board()
        for i in range(0, 9):
            if i & 2:
                b[i] = Player.NAUGHT
            else:
                b[i] = Player.CROSS
        self.assertEqual((Outcome.TIE, Player.NONE), b.outcome())

    def test_simple_win_012(self):
        b = Board()
        b[0] = Player.NAUGHT
        b[1] = Player.NAUGHT
        b[2] = Player.NAUGHT
        self.assertEqual((Outcome.WIN_012, Player.NAUGHT), b.outcome())

    def test_simple_win_345(self):
        b = Board()
        b[3] = Player.NAUGHT
        b[4] = Player.NAUGHT
        b[5] = Player.NAUGHT
        self.assertEqual((Outcome.WIN_345, Player.NAUGHT), b.outcome())

    def test_simple_win_678(self):
        b = Board()
        b[6] = Player.NAUGHT
        b[7] = Player.NAUGHT
        b[8] = Player.NAUGHT
        self.assertEqual((Outcome.WIN_678, Player.NAUGHT), b.outcome())

    def test_simple_win_036(self):
        b = Board()
        b[0] = Player.NAUGHT
        b[3] = Player.NAUGHT
        b[6] = Player.NAUGHT
        self.assertEqual((Outcome.WIN_036, Player.NAUGHT), b.outcome())

    def test_simple_win_147(self):
        b = Board()
        b[1] = Player.NAUGHT
        b[4] = Player.NAUGHT
        b[7] = Player.NAUGHT
        self.assertEqual((Outcome.WIN_147, Player.NAUGHT), b.outcome())

    def test_simple_win_258(self):
        b = Board()
        b[2] = Player.NAUGHT
        b[5] = Player.NAUGHT
        b[8] = Player.NAUGHT
        self.assertEqual((Outcome.WIN_258, Player.NAUGHT), b.outcome())

    def test_simple_win_048(self):
        b = Board()
        b[0] = Player.NAUGHT
        b[4] = Player.NAUGHT
        b[8] = Player.NAUGHT
        self.assertEqual((Outcome.WIN_048, Player.NAUGHT), b.outcome())

    def test_simple_win_246(self):
        b = Board()
        b[2] = Player.NAUGHT
        b[4] = Player.NAUGHT
        b[6] = Player.NAUGHT
        self.assertEqual((Outcome.WIN_246, Player.NAUGHT), b.outcome())


if __name__ == '__main__':
    unittest.main()
