import unittest
from final_version import decimal_to_hex

class TestDecimalToHex(unittest.TestCase):
    def test_valid_input(self):
      
        self.assertEqual(decimal_to_hex(0), "0")  
        self.assertEqual(decimal_to_hex(10), "A") 
        self.assertEqual(decimal_to_hex(255), "FF")  
        self.assertEqual(decimal_to_hex(16), "10") 

    def test_negative_input(self):
        
        with self.assertRaises(ValueError):
            decimal_to_hex(-10)  

    def test_large_input(self):
      
        self.assertEqual(decimal_to_hex(4096), "1000") 

if __name__ == "__main__":
    unittest.main()
