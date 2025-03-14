import sys

def decimal_to_hex(decimal_value):
    """Convert a non-negative integer to its hexadecimal representation."""
    if decimal_value == 0:
        return "0"

    hex_chars = "0123456789ABCDEF"
    hexadecimal = ""
    num = decimal_value

    while num > 0:
        rem = num % 16
        hexadecimal = hex_chars[rem] + hexadecimal
        num //= 16

    return hexadecimal

if __name__ == "__main__":
    # Ensure exactly one argument is provided
    if len(sys.argv) != 2:
        print("Error: Please provide exactly one integer argument.")
        sys.exit(1)

    try:
        # Try to convert the argument to an integer
        decimal_value = int(sys.argv[1])

        # Ensure the provided value is non-negative
        if decimal_value < 0:
            print("Error: Please provide a non-negative integer.")
            sys.exit(1)

        # Call the conversion function and print the result
        hex_result = decimal_to_hex(decimal_value)
        print(f"Hexadecimal representation is: {hex_result}")

    except ValueError:
        # Handle case where the input is not a valid integer
        print("Error: Please provide a valid integer.")
        sys.exit(1)
