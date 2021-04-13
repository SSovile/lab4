import os
import unittest

import pep8

import details
from details import DetailType
from details.doors import Doors
from details.manager import DetailsManager
from details.motors import Motors
from details.wheels import Wheels
from typing import List

class TestManage(unittest.TestCase):
    def setUp(self):
        self.details = [
            Motors(20866, 'German', 'Metal'),
            Wheels(20456, 'England', 'Metal'),
            Doors(10232, 'German', 'Metal')
        ]

        self.fadetails = DetailsManager()
        self.fadetails.add_details(self.details)

    def test_sort_by_ser_num(self):
        expect = sorted(self.details, key=lambda s: s.sser_num, reverse=DetailType.NoChassis.value)
        self.assertEqual(self.fadetails.sort_by_ser_num(details=self.details, order=DetailType.NoChassis), expect)

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


class ManagerTest(unittest.TestCase):
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
