import sys

def decimal_to_hex(decimal_value):
    """
    Convert a non-negative integer to its hexadecimal representation.

    Args:
        decimal_value (int): The non-negative integer to convert.

    Returns:
        str: The hexadecimal representation of the input.

    Raises:
        ValueError: If the input is negative or not a valid integer.
    """
    if decimal_value < 0:
        raise ValueError("Input must be a non-negative integer.")
    
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
    # Check if no argument is provided
    if len(sys.argv) != 2:
        print("Error: Please provide exactly one integer argument.")
        sys.exit(1)

    # Try to convert the input to an integer
    try:
        decimal_value = int(sys.argv[1])
        if decimal_value < 0:  # Check if the provided value is negative
            print("Error: Please provide a non-negative integer.")
            sys.exit(1)
        
        # Call the function to convert the valid non-negative integer to hexadecimal
        hex_result = decimal_to_hex(decimal_value)
        print(f"Hexadecimal representation is: {hex_result}")

    except ValueError as e:
        # Handle case where the input is not a valid integer
        print("Error: Please provide a valid integer.")
        raise e  # Re-raise the exception
