#!/usr/bin/env python3

import unittest
from rahul_exp_lib.beta.beta_utils import mul

class TestBeta(unittest.TestCase):
    def test_mul(self) -> None:
        self.assertEquals(mul(2, 3), 6)
        

if __name__ == "__main__":
    unittest.main()