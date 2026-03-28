# Lesson 10: BitPlay 2 - Reverse all bits in a number

def reverse_bits(num):
    """
    Reverse all bits present in a number
    """
    # Convert number to binary (remove '0b' prefix)
    binary_str = bin(num)[2:]
    
    # Reverse the binary string
    reversed_binary = binary_str[::-1]
    
    # Convert back to decimal
    reversed_num = int(reversed_binary, 2)
    
    return reversed_num


def main():
    # Get input from user
    number = int(input("Enter a number: "))
    
    # Get the reversed number
    result = reverse_bits(number)
    
    # Print results
    print(f"Original number: {number}")
    print(f"Binary representation: {bin(number)[2:]}")
    print(f"Reversed binary: {bin(result)[2:]}")
    print(f"Reversed number: {result}")


if __name__ == "__main__":
    main()