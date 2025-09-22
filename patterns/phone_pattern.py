import re

def extract_phones(text):
    """
    Extract phone numbers from text.
    Supports: (123) 456-7890, 123-456-7890, 123.456.7890
    """
    pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    return re.findall(pattern, text)

if __name__ == "__main__":
    test_text = "Call (250) 759-4258, 445-321-9780, or 250.312.5842"
    print("Test:", test_text)
    print("=" * 58)
    print("Results:", extract_phones(test_text))