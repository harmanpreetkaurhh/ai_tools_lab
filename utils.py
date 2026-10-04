def is_palindrome(s):
    """Check if a string is a palindrome, ignoring case, spaces and punctuation."""
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]


def count_words(text):
    """Count the words in a text. Returns 0 for empty text."""
    return len(text.split())


def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit, rounded to 2 decimal places."""
    return round(c * 9 / 5 + 32, 2)


print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(count_words("  I love   Python  "))               # 3
print(celsius_to_fahrenheit(36.6))                      # 97.88