import re

def extract_urls(text):
    """
    Extract URLs from text.
    Pattern: http/https with optional subdomain, path, and query parameters
    Supports: https://www.example.com, http://subdomain.example.org/page
    """
    pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+(?:[/\w\.-]*)*/?\??(?:[-\w+=&;%@\.]*)*'
    return re.findall(pattern, text)

if __name__ == "__main__":
    test_text = "Visit https://www.google.com and http://www.github.com/features"
    print("Test:", test_text)
    print("=" * 68)
    print("Results:", extract_urls(test_text))