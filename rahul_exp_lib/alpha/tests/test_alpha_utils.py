#!/usr/bin/env python3

import unittest
from rahul_exp_lib.alpha.alpha_utils import add

class TestAlpha(unittest.TestCase):
    def test_add(self) -> None:
        self.assertEquals(add(2, 3), 5)
        

if __name__ == "__main__":
    unittest.main()