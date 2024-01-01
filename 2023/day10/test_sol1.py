#!/usr/bin/python3
import sol1
import unittest


class TestSol1(unittest.TestCase):

    def testCircle(self):
        DATA= [
            '.....',
            '.S-7.',
            '.|.|.',
            '.L-J.',
            '.....',
        ]
        for c, l in enumerate(DATA):
            DATA[c] = list(l)
        self.assertEqual(4, sol1.process_data(DATA))

    def testComplex(self):
        DATA= [
            '..F7.',
            '.FJ|.',
            'SJ.L7',
            '|F--J',
            'LJ...',
        ]
        for c, l in enumerate(DATA):
            DATA[c] = list(l)
        self.assertEqual(8, sol1.process_data(DATA))


if __name__ == '__main__':
    unittest.main()
