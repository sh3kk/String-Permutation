# Abhishek Kundu
# CPE 202
# Assignment 1
# perm_lex_testcases.py

import unittest
import perm_lex


class TestAss1(unittest.TestCase):
    def test_perm_gen_lex_3chars(self):
        self.assertEquals(perm_lex.perm_gen_lex("abc"), ["abc", "acb", "bac", "bca", "cab", "cba"])

    def test_perm_gen_lex_1char(self):
        self.assertEquals(perm_lex.perm_gen_lex("a"), ["a"])

    def test_perm_gen_lex_2chars(self):
        self.assertEquals(perm_lex.perm_gen_lex("ab"), ["ab", "ba"])

    def test_perm_gen_lex_nochar(self):
        self.assertEquals(perm_lex.perm_gen_lex(""), [""])

if __name__ == "__main__":
        unittest.main()
