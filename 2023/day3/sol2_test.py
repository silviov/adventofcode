#!/usr/bin/python3
import sol2
import unittest

DATA = [
'467..114..',
'...*......',
'..35..633.',
'......#...',
'617*......',
'.....+.58.',
'..592.....',
'......755.',
'...$.*....',
'.664.598..',
]


class TestMap(unittest.TestCase):


    def testResult(self):
        m = sol2.Map()
        m.read_data(DATA)
        self.assertEqual(467835, m.result())
    

if __name__ == '__main__':
    unittest.main()
