import re

def extract_hashtags(text):
    """
    Extract hashtags from text.
    Pattern: # followed by letters, numbers, or underscores
    Supports: #example, #ThisIsAHashtag, #python3
    """
    pattern = r'#\w+'
    return re.findall(pattern, text)

if __name__ == "__main__":
    test_text = "Trending: #python and #JavaScript"
    print("Test:", test_text)
    print("=" * 41)
    print("Results:", extract_hashtags(test_text))