# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-only
import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location("fib", Path(__file__).resolve().parents[1] / "fibonacci.py")
fib = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fib)

class FibonacciTests(unittest.TestCase):
    def test_sequence(self):
        self.assertEqual(fib.first_n(8), [1, 1, 2, 3, 5, 8, 13, 21])
    def test_empty(self):
        self.assertEqual(fib.first_n(0), [])
    def test_invalid(self):
        for value in (-1, True, "5"):
            with self.assertRaises(ValueError):
                fib.first_n(value)

if __name__ == "__main__":
    unittest.main()
