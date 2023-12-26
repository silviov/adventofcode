#!/usr/bin/python3
import sol1
import unittest


class TestSol1(unittest.TestCase):

    DATA1= [
        'RL',
        '',
        'AAA = (BBB, CCC)',
        'BBB = (DDD, EEE)',
        'CCC = (ZZZ, GGG)',
        'DDD = (DDD, DDD)',
        'EEE = (EEE, EEE)',
        'GGG = (GGG, GGG)',
        'ZZZ = (ZZZ, ZZZ)',
    ]

    DATA2 = [
        'LLR',
        '',
        'AAA = (BBB, BBB)',
        'BBB = (AAA, ZZZ)',
        'ZZZ = (ZZZ, ZZZ)',
    ]

    def testData1(self):
        self.assertEqual(2, sol1.process_data(self.DATA1))

    def testData2(self):
        self.assertEqual(6, sol1.process_data(self.DATA2))
        

if __name__ == '__main__':
    unittest.main()
