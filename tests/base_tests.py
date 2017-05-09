import unittest
import sys
import os
sys.path.append(os.path.join(os.getcwd(), "tic_tac_toe"))
import base


class TestUM(unittest.TestCase):

    def setUp(self):
        self.baseobj = base.Base()
        self.baseobj.matrix = [None] * 9

    def test_find_block(self):
        self.assertEqual(self.baseobj.findblock(10, 10), 0)

    def test_checkXwin(self):
        self.baseobj.matrix = ['X', 'O', 'X', 'X', 'X', 'O', 'X', 'O', 'O']
        self.assertEqual(self.baseobj.check('X')[1], True)

    def test_checkForDraw(self):
        self.baseobj.matrix = ['X', 'O', 'O', 'O', 'O', 'X', 'X', 'X', 'O']
        self.assertEqual(self.baseobj.checkForDraw(), True)

if __name__ == '__main__':
    unittest.main()
