import re

def extract_html_tags(text):
    """
    Extract HTML tags from text.
    Pattern: matches any HTML tag with attributes
    Supports: <p>, <div class="container">
    """
    pattern = r'<[^>]+>'
    return re.findall(pattern, text)

if __name__ == "__main__":
    test_text = "HTML: <p>Destined for greatness!</p> and <div class='box'>"
    print("Test:", test_text)
    print("=" * 65)
    print("Results:", extract_html_tags(test_text))