# String reverse using for loop in python
"""
Enter a number: 12345
Reverse of the number: 54321
"""
def reverse_string(input_string):
    reversed_string = ''
    for char in reversed(input_string):
        reversed_string += char
    return reversed_string

# Example usage
original_string = "Hello, World!"
reversed_string = reverse_string(original_string)

print(reversed_string)

