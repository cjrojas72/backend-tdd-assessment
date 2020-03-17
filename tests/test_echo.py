#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo
import subprocess

# Your test case class goes here


class TestEcho(unittest.TestCase):

    def setUp(self):
        self.parser = echo.create_parser()
    
    def tests_no_options(self):
        #self.fail("Need to write test")
        args = ["HelLo WoRld"]
        ns = self.parser.parse_args(args)
        self.assertFalse(ns.upper)
        self.assertFalse(ns.lower)
        self.assertFalse(ns.title)
        actual = echo.main(args)
        expected = args[0]
        self.assertEqual(actual, expected)
    
    def tests_all_options(self):
        #self.fail("Need to write test")
        args = ["-tul", "HelLo WoRld"]
        try:
            ns = self.parser.parse_args(args)
        except Exception as e:
            print(str(e))
        self.assertTrue(ns.upper)   
        self.assertTrue(ns.lower)
        self.assertTrue(ns.title)
        actual = echo.main(args)
        expected = "Hello World"
        self.assertEqual(actual, expected)

    def tests_upper_short(self):
        #self.fail("Need to write test")
        args = ["-u", "hello world"]
        ns = self.parser.parse_args(args)
        self.assertTrue(ns.upper)
        actual = echo.main(args)
        expected = "HELLO WORLD"
        self.assertEqual(actual, expected)

    def tests_lower_short(self):
        #self.fail("Need to write test")
        args = ["-l", "hello world"]
        ns = self.parser.parse_args(args)
        self.assertTrue(ns.lower)
        actual = echo.main(args)
        expected = "hello world"
        self.assertEqual(actual, expected)

    def tests_title_short(self):
        #self.fail("Need to write test")
        args = ["-t", "HelLo WoRld"]
        ns = self.parser.parse_args(args)
        self.assertTrue(ns.title)
        actual = echo.main(args)
        expected = "Hello World"
        self.assertEqual(actual, expected)

    def tests_title_long(self):
        #self.fail("Need to write test")
        args = ["--title", "HelLo WoRld"]
        ns = self.parser.parse_args(args)
        self.assertTrue(ns.title)
        actual = echo.main(args)
        expected = "Hello World"
        self.assertEqual(actual, expected)
    
    def tests_upper_long(self):
        #self.fail("Need to write test")
        args = ["--upper", "hello world"]
        ns = self.parser.parse_args(args)
        self.assertTrue(ns.upper)
        actual = echo.main(args)
        expected = "HELLO WORLD"
        self.assertEqual(actual, expected)
    
    def tests_lower_long(self):
        #self.fail("Need to write test")
        args = ["--lower", "hello world"]
        ns = self.parser.parse_args(args)
        self.assertTrue(ns.lower)
        actual = echo.main(args)
        expected = "hello world"
        self.assertEqual(actual, expected)


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
