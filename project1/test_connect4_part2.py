import os
from importlib.machinery import SourceFileLoader
import unittest

def _load_connect4_from(path, module_name):
    if not os.path.exists(path):
        return None
    loader = SourceFileLoader(module_name, path)
    mod = loader.load_module()
    return getattr(mod, 'Connect4', None)

Connect4 = None

for cand, name in (
    ('/mnt/data/main_modified.py', 'connect4_mod'),
    ('/mnt/data/main (1).py', 'connect4_main1'),
    ('/mnt/data/main.py', 'connect4_main')
):
    Connect4 = _load_connect4_from(cand, name)
    if Connect4:
        IMPORT_SOURCE = cand
        break
else:
    raise RuntimeError("Could not import Connect4 from known sources.")

class TestCheckWin(unittest.TestCase):
    def setUp(self):
        self.game = Connect4()
        for r in range(self.game.ROWS):
            for c in range(self.game.COLS):
                self.game.board[r][c] = ' '

    def test_horizontal_win(self):
        r = self.game.ROWS - 1
        for c in range(4):
            self.game.board[r][c] = 'X'
        self.assertTrue(self.game.check_win('X'))

    def test_vertical_win(self):
        col = 2
        for r in range(self.game.ROWS - 1, self.game.ROWS - 5, -1):
            self.game.board[r][col] = 'O'
        self.assertTrue(self.game.check_win('O'))

    def test_diagonal_down_right_win(self):
        for r,c in [(2,0),(3,1),(4,2),(5,3)]:
            self.game.board[r][c] = 'X'
        self.assertTrue(self.game.check_win('X'))

    def test_diagonal_up_right_win(self):
        for r,c in [(5,0),(4,1),(3,2),(2,3)]:
            self.game.board[r][c] = 'O'
        self.assertTrue(self.game.check_win('O'))

    def test_no_win(self):
        self.game.board[5][0] = 'X'
        self.game.board[5][1] = 'O'
        self.game.board[5][2] = 'X'
        self.game.board[4][0] = 'O'
        self.game.board[4][1] = 'X'
        self.game.board[3][0] = 'O'
        self.assertFalse(self.game.check_win('X'))
        self.assertFalse(self.game.check_win('O'))

class TestDropChip(unittest.TestCase):
    def setUp(self):
        self.game = Connect4()
        for r in range(self.game.ROWS):
            for c in range(self.game.COLS):
                self.game.board[r][c] = ' '

    def test_successful_drop(self):
        self.game.current_player = 'X'
        self.assertTrue(self.game.drop_chip(1))
        self.assertEqual(self.game.board[self.game.ROWS-1][0], 'X')

    def test_full_column(self):
        self.game.current_player = 'O'
        col = 3
        for _ in range(self.game.ROWS):
            self.assertTrue(self.game.drop_chip(col))
        self.assertFalse(self.game.drop_chip(col))

    def test_invalid_column(self):
        self.game.current_player = 'X'
        self.assertFalse(self.game.drop_chip(0))
        self.assertFalse(self.game.drop_chip(-1))
        self.assertFalse(self.game.drop_chip(self.game.COLS + 1))

    def test_full_board_behavior(self):
        sym = ['X','O']
        si = 0
        for r in range(self.game.ROWS):
            for c in range(1, self.game.COLS + 1):
                self.game.current_player = sym[si]
                si = 1 - si
                self.assertTrue(self.game.drop_chip(c))
        if hasattr(self.game, 'is_full'):
            self.assertTrue(self.game.is_full())
        for c in range(1, self.game.COLS + 1):
            self.game.current_player = 'X'
            self.assertFalse(self.game.drop_chip(c))

if __name__ == "__main__":
    unittest.main(verbosity=2)

