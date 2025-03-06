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

if __name__ == "__main__":  # This block is executed only if the script is run directly, not imported
    # Check if the user has provided exactly one command-line argument (besides the script name)
    if len(sys.argv) != 2:
        print("Error: Please provide exactly one integer argument.")  # Error message if argument count is wrong
        sys.exit(1)  # Exit the program with a non-zero status code to indicate an error

    try:
        # Try to convert the command-line argument into an integer
        decimal_value = int(sys.argv[1])  
        
        # Check if the input value is negative
        if decimal_value < 0:
            print("Error: Please provide a non-negative integer.")  # Error message for negative integers
            sys.exit(1)  # Exit the program with an error code
        
        # Call the function to convert the valid non-negative integer to hexadecimal
        decimal_to_hex(decimal_value)
    
    except ValueError:
        # Handle the case where the input is not a valid integer
        print("Error: Please provide a valid integer.")  # Error message for invalid input
        sys.exit(1)  # Exit the program with an error code
