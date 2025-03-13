  GNU nano 8.3                       Dex2Hex.py
import sys

def decimal_to_hex(decimal_value):
    hex_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C>
    hexadecimal = ""
    num = decimal_value

    print(f"Converting the Decimal Value {num} to Hex...")
    while num != 0:
        rem = num % 16
        hexadecimal = hex_chars[rem] + hexadecimal
        num //= 16

    print(f"Hexadecimal representation is: {hexadecimal}")
    return hexadecimal  # Return the hexadecimal value for testing

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: Please provide exactly one integer argument.")
        sys.exit(1)

