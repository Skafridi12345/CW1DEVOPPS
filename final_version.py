import sys

def decimal_to_hex(decimal_value):
<<<<<<< HEAD
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
=======
    hex_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
>>>>>>> ea96176aeaa63ad13aef301ff7f15bc39b61047d
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
<<<<<<< HEAD
    # Check if no argument is provided
=======
>>>>>>> ea96176aeaa63ad13aef301ff7f15bc39b61047d
    if len(sys.argv) != 2:
        print("Error: Please provide exactly one integer argument.")
        sys.exit(1)

    # Try to convert the input to an integer
    try:
<<<<<<< HEAD
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
=======
        decimal_value = int(sys.argv[1])  # Convert the argument to an integer
        decimal_to_hex(decimal_value)
    except ValueError:
        print("Error: The provided argument is not a valid integer.")
        sys.exit(1)
>>>>>>> ea96176aeaa63ad13aef301ff7f15bc39b61047d
