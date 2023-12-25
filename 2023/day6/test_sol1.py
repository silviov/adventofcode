#!/usr/bin/python3
import sol1
import unittest


class TestSol1(unittest.TestCase):

    DATA = [
        'Time:      7  15   30', 
        'Distance:  9  40  200', 
        ]

    def testData(self):
        self.assertEqual(288, sol1.process_data(self.DATA))
        

if __name__ == '__main__':
    unittest.main()
