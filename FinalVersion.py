import sys  # Importing the sys module to work with command-line arguments

def decimal_to_hex(decimal_value):
    # A list of characters that represent the hexadecimal digits (0-9, A-F)
    hex_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    
    # Initialize an empty string to store the hexadecimal result
    hexadecimal = ""
    
    # Store the original decimal value for conversion
    num = decimal_value

    # Inform the user about the start of the conversion process
    print(f"Converting the Decimal Value {num} to Hex...")

    # Loop to convert the decimal number to hexadecimal
    while num != 0:  # Continue until the number becomes 0
        rem = num % 16  # Get the remainder when dividing the number by 16 (this corresponds to a hex digit)
        
        # Add the corresponding hexadecimal character to the front of the result string
        hexadecimal = hex_chars[rem] + hexadecimal
        
        # Perform integer division by 16 to reduce the number for the next iteration
        num //= 16

    # Output the final hexadecimal value
    print(f"Hexadecimal representation is: {hexadecimal}")
    
    # Return the hexadecimal value, so it can be used later or tested
    return hexadecimal

# Check if no argument is provided
if len(sys.argv) != 2:
    print("Error: Please provide exactly one integer argument.")
    try:
        sys.exit(1)
    except SystemExit:
        pass  # Avoid the traceback in interactive environments

# Try to convert the input to an integer
try:
    decimal_value = int(sys.argv[1])
    if decimal_value < 0:  # Check if the provided value is negative
        print("Error: Please provide a non-negative integer.")
        sys.exit(1)
    
    # Call the function to convert the valid non-negative integer to hexadecimal
    decimal_to_hex(decimal_value)

except ValueError:
    # Handle case where the input is not a valid integer
    print("Error: Please provide a valid integer.")
    try:
        sys.exit(1)
    except SystemExit:
        pass  # Avoid the traceback in interactive environments
