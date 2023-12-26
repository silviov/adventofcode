#!/usr/bin/python3
import sol2
import unittest


class TestSol1(unittest.TestCase):

    DATA1= [
        'LR',
        '',
        '11A = (11B, XXX)',
        '11B = (XXX, 11Z)',
        '11Z = (11B, XXX)',
        '22A = (22B, XXX)',
        '22B = (22C, 22C)',
        '22C = (22Z, 22Z)',
        '22Z = (22B, 22B)',
        'XXX = (XXX, XXX)',
    ]

    def testData1(self):
        self.assertEqual(6, sol2.process_data(self.DATA1))


if __name__ == '__main__':
    unittest.main()
