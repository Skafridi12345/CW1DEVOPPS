import sys

HEX_CHARS = "0123456789ABCDEF"

def decimal_to_hex(decimal_value):
    """Convert a non-negative integer to its hexadecimal representation."""
    if decimal_value == 0:
        return "0"
    
    hexadecimal_list = []
    num = decimal_value

    while num > 0:
        rem = num % 16
        hexadecimal_list.append(HEX_CHARS[rem])
        num //= 16

    return ''.join(reversed(hexadecimal_list))

def main():
    """Handle command-line input and conversion."""
    if len(sys.argv) != 2:
        print("Error: Please provide exactly one integer argument.")
        sys.exit(1)

    try:
        decimal_value = int(sys.argv[1])
        if decimal_value < 0:
            print("Error: Please provide a non-negative integer.")
            sys.exit(1)

        hex_result = decimal_to_hex(decimal_value)
        print(f"Hexadecimal representation is: {hex_result}")

    except ValueError:
        print("Error: Please provide a valid integer.")
        sys.exit(1)

if __name__ == "__main__":
    main()
