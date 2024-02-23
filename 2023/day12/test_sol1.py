#!/usr/bin/python3
import sol1
import unittest


class TestSol1(unittest.TestCase):

    def testLine(self):
        self.assertEqual(1, sol1.process_line(list('???.###'), [1, 1, 3]))

    def testLine2(self):
        self.assertEqual(10, sol1.process_line(list('?###????????'), [3, 2, 1]))

    def testExample(self):
        DATA= [
            '???.### 1,1,3',
            '.??..??...?##. 1,1,3',
            '?#?#?#?#?#?#?#? 1,3,1,6',
            '????.#...#... 4,1,1',
            '????.######..#####. 1,6,5',
            '?###???????? 3,2,1',
        ]
        self.assertEqual(21, sol1.process_data(DATA, 1))
        self.assertEqual(525152, sol1.process_data(DATA, 5))


if __name__ == '__main__':
    unittest.main()
