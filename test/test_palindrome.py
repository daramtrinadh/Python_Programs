# Implement a function that checks if a string is a palindrome.
# Use pytest to create parameterized tests that validate the function against a variety of input cases.
import pytest



def palindrome(user_string):
    if not isinstance(user_string,str):
        raise ValueError("Enter only String")
    normalized_string=" ".join(char.lower() for char in user_string if char.isalnum())
    return normalized_string==normalized_string[::-1]

@pytest.mark.parametrize("test_input,expected", [
    ("A man, a plan, a canal, Panama", True),  # Palindrome with punctuation and spaces
    ("racecar", True),                         # Simple palindrome
    ("hello", False),                          # Not a palindrome
    ("", True),                                # Empty string (considered a palindrome)
    ("12321", True),                           # Numeric palindrome
    ("12345", False),                          # Numeric non-palindrome
    ("No 'x' in Nixon", True),                 # Palindrome with mixed case and punctuation
    ("Was it a car or a cat I saw?", True),    # Palindrome with punctuation and spaces
    ("Not a palindrome", False)                # Clearly not a palindrome
])
def test_valid_palindrome(test_input,expected):
    assert palindrome(test_input)==expected

def test_invalid_palindrome():
    with pytest.raises(ValueError):
        palindrome(1242)


