def reverse_words(text: str) -> str:
    """Reverse the order of words in a string."""
    return " ".join(reversed(text.split()))


def count_words(text: str) -> int:
    """Return the number of whitespace-separated words."""
    return len(text.split())


def shout(text: str) -> str:
    """Convert text to uppercase and add an exclamation mark."""
    return text.upper().rstrip("!") + "!"
