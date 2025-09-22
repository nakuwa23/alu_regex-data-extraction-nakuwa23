import re

def extract_emails(text):
    """
    Extract email addresses from text.
    Pattern: username@domain.tld
    Supports: user@example.com, firstname.lastname@company.co.uk
    """
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(pattern, text)


if __name__ == "__main__":
    test_text = "Contact hustler1838@gmail.com and bk.nakuwa@tamam.co.uk"
    print("Test:", test_text)
    print("=" * 65)
    print("Results:", extract_emails(test_text))