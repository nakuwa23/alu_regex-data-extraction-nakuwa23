# Import each function directly from its module
from patterns.email_pattern import extract_emails
from patterns.url_pattern import extract_urls
from patterns.phone_pattern import extract_phones
from patterns.credit_card_pattern import extract_credit_cards
from patterns.html_tag_pattern import extract_html_tags
from patterns.hashtag_pattern import extract_hashtags

class DataExtractor:
    def __init__(self):
        self.extractors = {
            "email_addresses": extract_emails,
            "urls": extract_urls,
            "phone_numbers": extract_phones,
            "credit_cards": extract_credit_cards,
            "html_tags": extract_html_tags,
            "hashtags": extract_hashtags
        }
    
    def extract_all(self, text):
        """Extract all data types from text."""
        results = {}
        for data_type, extractor in self.extractors.items():
            results[data_type] = extractor(text)
        return results
    
    def extract_specific(self, text, data_type):
        """Extract specific data type from text."""
        if data_type in self.extractors:
            return self.extractors[data_type](text)
        else:
            raise ValueError(f"Unsupported data type: {data_type}")

def main():
    extractor = DataExtractor()
    
    # Read sample text
    try:
        with open('sample_input.txt', 'r') as file:
            text = file.read()
    except FileNotFoundError:
        print("sample_input.txt not found! Using default text.")
        text = """
        Contact us at info@example.com or support@company.co.uk.
        Visit https://www.example.com and http://subdomain.example.org/page.
        Call (123) 456-7890 or 123-456-7890.
        Payment: 1234 5678 9012 3456 or 1234-5678-9012-3456.
        HTML: <p>Hello</p> and <div class="container">.
        Trending: #example and #ThisIsAHashtag.
        """
    
    # Extract all the data types
    results = extractor.extract_all(text)
    
    # Print results
    print("=" * 40)
    print("Data Extraction Results:")
    print("=" * 40)
    
    for data_type, values in results.items():
        print(f"\n{data_type.upper()} ({len(values)} found):")
        for value in values:
            print(f"  - {value}")

if __name__ == "__main__":
    main()