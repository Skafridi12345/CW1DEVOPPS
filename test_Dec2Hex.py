import unittest
from final_version import decimal_to_hex

class TestDecimalToHex(unittest.TestCase):
    def test_valid_input(self):
        # Test valid inputs
        self.assertEqual(decimal_to_hex(0), "0")  # Test 0
        self.assertEqual(decimal_to_hex(10), "A")  # Test 10
        self.assertEqual(decimal_to_hex(255), "FF")  # Test 255
        self.assertEqual(decimal_to_hex(16), "10")  # Test 16

    def test_negative_input(self):
        # Test negative input (should be handled by the main script, not the function)
        with self.assertRaises(ValueError):
            decimal_to_hex(-10)  # Function doesn't handle negatives, but main script does

    def test_large_input(self):
        # Test large input
        self.assertEqual(decimal_to_hex(4096), "1000")  # Test 4096

if __name__ == "__main__":
    unittest.main()
