#!/usr/bin/python3
import sol2
import unittest


class TestSol2(unittest.TestCase):

    DATA = [
        'seeds: 79 14 55 13',
        '',
        'seed-to-soil map:',
        '50 98 2',
        '52 50 48',
        '',
        'soil-to-fertilizer map:',
        '0 15 37',
        '37 52 2',
        '39 0 15',
        '',
        'fertilizer-to-water map:',
        '49 53 8',
        '0 11 42',
        '42 0 7',
        '57 7 4',
        '',
        'water-to-light map:',
        '88 18 7',
        '18 25 70',
        '',
        'light-to-temperature map:',
        '45 77 23',
        '81 45 19',
        '68 64 13',
        '',
        'temperature-to-humidity map:',
        '0 69 1',
        '1 0 69',
        '',
        'humidity-to-location map:',
        '60 56 37',
        '56 93 4',
        ]

    def testData(self):
        self.assertEqual(46, sol2.process_data(self.DATA))

    def testMapping(self):
        mapping = [
            sol2.Mapping("50 100 5"),
            sol2.Mapping("60 110 5"),
            sol2.Mapping("30 115 10"),
        ]
        i = sol2.Interval((90, 40))
        self.assertEqual([(30, 10), (50, 5), (60, 5), (90, 10), (105, 5), (125, 5)], i.map(mapping))


if __name__ == '__main__':
    unittest.main()
