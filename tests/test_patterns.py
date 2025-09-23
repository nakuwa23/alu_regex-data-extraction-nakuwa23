import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Import each function directly from its module
from patterns.email_pattern import extract_emails
from patterns.url_pattern import extract_urls
from patterns.phone_pattern import extract_phones
from patterns.credit_card_pattern import extract_credit_cards
from patterns.html_tag_pattern import extract_html_tags
from patterns.hashtag_pattern import extract_hashtags

def test_patterns():
    """Test all pattern extractors."""
    print("Testing pattern extractors...")
    print("=" * 40)
    
    # Test email address extraction
    email_text = "Contact hustler1838@gmail.com and bk.nakuwa@tamam.co.uk"
    emails = extract_emails(email_text)
    assert "hustler1838@gmail.com" in emails
    assert "bk.nakuwa@tamam.co.uk" in emails
    print("✓ Email extraction test passed")
    
    # Test URL extraction
    url_text = "Visit https://www.google.com and http://www.github.com/features"
    urls = extract_urls(url_text)
    assert "https://www.google.com" in urls
    assert "http://www.github.com/features" in urls
    print("✓ URL extraction test passed")
    
    # Test phone number extraction
    phone_text = "Call (250) 759-4258 or 445-321-9780"
    phones = extract_phones(phone_text)
    assert "(250) 759-4258" in phones
    assert "445-321-9780" in phones
    print("✓ Phone extraction test passed")
    
    # Test credit card number extraction
    cc_text = "Cards: 3241 7586 1290 5829 and 3456-7865-3456-9012"
    credit_cards = extract_credit_cards(cc_text)
    assert "3241 7586 1290 5829" in credit_cards
    assert "3456-7865-3456-9012" in credit_cards
    print("✓ Credit card extraction test passed")
    
    # Test HTML tag extraction
    html_text = "HTML: <p>Destined for greatness</p> and <div class='box'>"
    html_tags = extract_html_tags(html_text)
    assert "<p>" in html_tags
    assert "<div class='box'>" in html_tags
    print("✓ HTML tag extraction test passed")
    
    # Test hashtag extraction
    hashtag_text = "Trending: #python and #JavaScript"
    hashtags = extract_hashtags(hashtag_text)
    assert "#python" in hashtags
    assert "#JavaScript" in hashtags
    print("✓ Hashtag extraction test passed")
    
    print("=" * 40)
    print("All tests passed successfully☑️")

if __name__ == "__main__":
    test_patterns()