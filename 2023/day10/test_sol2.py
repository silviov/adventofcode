#!/usr/bin/python3
import sol2
import unittest


class TestSol2(unittest.TestCase):

    def testSimple(self):
        DATA= [
            '...........',
            '.S-------7.',
            '.|F-----7|.',
            '.||.....||.',
            '.||.....||.',
            '.|L-7.F-J|.',
            '.|..|.|..|.',
            '.L--J.L--J.',
            '...........',
        ]
        for c, l in enumerate(DATA):
            DATA[c] = list(l)
        self.assertEqual(4, sol2.process_data(DATA))

    def testComplex(self):
        DATA= [
            '.F----7F7F7F7F-7....',
            '.|F--7||||||||FJ....',
            '.||.FJ||||||||L7....',
            'FJL7L7LJLJ||LJ.L-7..',
            'L--J.L7...LJS7F-7L7.',
            '....F-J..F7FJ|L7L7L7',
            '....L7.F7||L7|.L7L7|',
            '.....|FJLJ|FJ|F7|.LJ',
            '....FJL-7.||.||||...',
            '....L---J.LJ.LJLJ...',
        ]
        for c, l in enumerate(DATA):
            DATA[c] = list(l)
        self.assertEqual(8, sol2.process_data(DATA))

    def testVeryComplex(self):
        DATA= [
            'FF7FSF7F7F7F7F7F---7',
            'L|LJ||||||||||||F--J',
            'FL-7LJLJ||||||LJL-77',
            'F--JF--7||LJLJ7F7FJ-',
            'L---JF-JLJ.||-FJLJJ7',
            '|F|F-JF---7F7-L7L|7|',
            '|FFJF7L7F-JF7|JL---7',
            '7-L-JL7||F7|L7F-7F7|',
            'L.L7LFJ|||||FJL7||LJ',
            'L7JLJL-JLJLJL--JLJ.L',
        ]
        for c, l in enumerate(DATA):
            DATA[c] = list(l)
        self.assertEqual(10, sol2.process_data(DATA))


if __name__ == '__main__':
    unittest.main()
