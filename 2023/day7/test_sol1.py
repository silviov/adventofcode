#!/usr/bin/python3
import sol1
import unittest


class TestSol1(unittest.TestCase):

    DATA = [
        '32T3K 765',
        'T55J5 684',
        'KK677 28',
        'KTJJT 220',
        'QQQJA 483',
        ]

    def testData(self):
        self.assertEqual(6440, sol1.process_data(self.DATA))
        

if __name__ == '__main__':
    unittest.main()
