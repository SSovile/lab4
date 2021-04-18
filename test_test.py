import os
import unittest

import pep8

import details
from details import DetailType
from details.doors import Doors
from details.manager import DetailsManager
from details.motors import Motors
from details.wheels import Wheels


class TestPep8(unittest.TestCase):

    def test_pep8(self):
        style = pep8.StyleGuide()
        style.options.max_line_length = 115
        filenames = []
        for root, _, files in os.walk('.'):
            python_files = [f for f in files if f.endswith(
                '.py') and "examples" not in root]
            for file in python_files:
                if len(root.split('samples')) != 2:
                    filename = '{0}/{1}'.format(root, file)
                    filenames.append(filename)
        check = style.check_files(filenames)
        print('PEP8 style errors: %d' % check.total_errors)


details = [
    Doors(10232, 'German', 'Metal'),
    Wheels(20456, 'England', 'Metal'),
    Motors(20866, 'German', 'Metal'),
    Doors(10646, 'Spain', 'Metal'),
    Wheels(30564, 'England', 'Metal'),
    Motors(17777, 'Spain', 'Metal'),
]


class ManagerTest(unittest.TestCase):
    def test_sort_by_number_of_players(self):
        fac = DetailsManager()
        fac.add_details(details)

        expect = Wheels(30564, 'England', 'Metal'), \
                 Motors(20866, 'German', 'Metal'), \
                 Wheels(20456, 'England', 'Metal'), \
                 Motors(17777, 'Spain', 'Metal'), \
                 Doors(10646, 'Spain', 'Metal'), \
                 Doors(10232, 'German', 'Metal')
        self.assertListEqual(fac.sort_by_ser_num(True),
                             sorted(details, key=lambda s: s.sser_num, reverse=True), expect)

    def test_add_details(self):
        details = [
            Doors(10232, 'German', 'Metal'),
            Wheels(20456, 'England', 'Metal'),
        ]

        fakeman = DetailsManager()

        fakeman.add_detail(details[0])
        self.assertListEqual(fakeman.details, [details[0]])

        fakeman.add_detail(details[1])
        self.assertListEqual(fakeman.details, details)

    def test_add_detail(self):
        details = [
            Doors(10232, 'German', 'Metal'),
            Wheels(20456, 'England', 'Metal'),
            Motors(20866, 'German', 'Metal'),
            Doors(10646, 'Spain', 'Metal'),
            Wheels(30564, 'England', 'Metal'),
            Motors(17777, 'Spain', 'Metal'),
        ]

        fakeman = DetailsManager()
        fakeman.add_details(details)

        self.assertListEqual(fakeman.details, details)


if __name__ == '__main__':
    unittest.main()
