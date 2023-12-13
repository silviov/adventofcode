#!/usr/bin/python3
import sol1
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

class TestLine(unittest.TestCase):

    def testParseLine(self):
        l = sol1.Line(DATA[0])
        self.assertEqual(2, len(l.numbers))

        self.assertEqual(467, l.numbers[0].value)
        self.assertEqual(0, l.numbers[0].start)
        self.assertEqual(3, l.numbers[0].end)

        self.assertEqual(114, l.numbers[1].value)
        self.assertEqual(5, l.numbers[1].start)
        self.assertEqual(8, l.numbers[1].end)

    def testHasSymbol(self):
        l = sol1.Line(DATA[0])
        self.assertFalse(l.has_symbol(0, 9))

        l = sol1.Line(DATA[1])
        self.assertEqual(l.symbols, {3})
        self.assertFalse(l.has_symbol(0, 2))
        self.assertTrue(l.has_symbol(4, 6))


class TestMap(unittest.TestCase):

    def TestResult2(self):
        m = sol1.Map()
        m.read_data([
            '..........',
            '......+5..',
            '.........1',
            ])
        self.assertEqual(5, m.results())

    def testResult(self):
        m = sol1.Map()
        m.read_data(DATA)
        self.assertEqual(4361, m.result())
    

if __name__ == '__main__':
    unittest.main()
