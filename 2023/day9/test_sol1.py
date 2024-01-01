#!/usr/bin/python3
import sol1
import unittest


class TestSol1(unittest.TestCase):

    def testData(self):
        DATA= [
            '0 3 6 9 12 15',
            '1 3 6 10 15 21',
            '10 13 16 21 30 45',
        ]
        self.assertEqual(114, sol1.process_data(DATA))


if __name__ == '__main__':
    unittest.main()
