import unittest
from adder import add_element
from checker import check_guitarist, check_band
import os


class TestMain(unittest.TestCase):

    def setUp(self):
        self.temporary_file = "/tmp/emptyfile"
        f = open(self.temporary_file, 'w')
        f.close()

    def test_no_datafile(self):
       u, r = check_guitarist(datafile="/tmp/nonexistentfile-wewefwwe")
       self.assertFalse(u)
       self.assertFalse(r)

    def test_empty_datafile(self):
       u, r = check_band(datafile=self.temporary_file)
       self.assertFalse(u)
       self.assertFalse(r)

    def tearDown(self):
        os.remove(self.temporary_file)

