#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo
import subprocess

# Your test case class goes here


class TestEcho(unittest.TestCase):
    def setUP(self):
        pass

    def tests_upper_short(self):
        self.fail("Need to write test")
    
    def tests_lower_short(self):
        self.fail("Need to write test")

    def tests_title_short(self):
        self.fail("Need to write test")

    def tests_title_long(self):
        self.fail("Need to write test")
    
    def tests_upper_longt(self):
        self.fail("Need to write test")
    
    def tests_lower_long(self):
        self.fail("Need to write test")



    def test_help(self):
        """ Running the program without arguments should show usage. """

        # Run the command `python ./echo.py -h` in a separate process, then
        # collect it's output.
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        with open("USAGE") as f:
            usage = f.read()

        self.assertEquals(stdout, usage)


if __name__ == '__main__':
    unittest.main()
