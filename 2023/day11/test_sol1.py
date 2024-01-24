#!/usr/bin/python3
import sol1
import unittest


class TestSol1(unittest.TestCase):

    def testExample(self):
        DATA= [
            '...#......',
            '.......#..',
            '#.........',
            '..........',
            '......#...',
            '.#........',
            '.........#',
            '..........',
            '.......#..',
            '#...#.....',
        ]
        for c, l in enumerate(DATA):
            DATA[c] = list(l)
        self.assertEqual(374, sol1.process_data(DATA, 2))
        self.assertEqual(1030, sol1.process_data(DATA, 10))
        self.assertEqual(8410, sol1.process_data(DATA, 100))


if __name__ == '__main__':
    unittest.main()
