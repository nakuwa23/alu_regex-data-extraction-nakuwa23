import re

def extract_credit_cards(text):
    """
    Extract credit card numbers from text.
    Pattern: 16 digits with optional spaces or dashes
    Supports: 1234 5678 9012 3456, 1234-5678-9012-3456
    """
    pattern = r'\b(?:\d{4}[- ]?){3}\d{4}\b'
    return re.findall(pattern, text)

if __name__ == "__main__":
    test_text = "Cards: 3241 7586 1290 5829 and 3456-7865-3456-9012"
    print("Test:", test_text)
    print("=" * 55)
    print("Results:", extract_credit_cards(test_text))