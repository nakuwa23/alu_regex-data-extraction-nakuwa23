# Formative Assessment 1: Regex Onboarding Hackathon

This is basically a beginner-friendly Python project that demonstrates how to extract common patterns from text with regular expressions (regex). It includes:

- Email addresses
- URLs
- Phone numbers
- Credit card numbers
- HTML opening tags
- Hashtags

Use it via the provided script to scan a text file, or import the functions/classes in your own Python code.

## Features

- **Simple API**: Call a single class `DataExtractor` to extract everything, or use individual functions per pattern.
- **No external dependencies**: Uses Python’s built-in `re` module only.
- **Clear examples**: Ready-to-run examples and a sample input file.
- **Lightweight tests**: Quick script with assertions to validate each extractor.

## Project Structure

```
alu_regex-data-extraction-nakuwa23/
  main.py                      # CLI-style entry script
  sample_input.txt             # Example text to extract from
  patterns/
    email_pattern.py           # Extract emails
    url_pattern.py             # Extract urls
    phone_pattern.py           # Extract phone numbers
    credit_card_pattern.py     # Extract credit cards numbers
    html_tag_pattern.py        # Extract html tags
    hashtag_pattern.py         # Extract hashtags
  tests/
    test_patterns.py           # Quick assertions for each extractor
```

## Requirements

- Python 3.8+ (tested with modern Python 3 versions)
- No third-party packages required

## Quick Start

1) Clone or download the repository.

2) Run the script using the included sample input:
```bash
cd alu_regex-data-extraction-nakuwa23
python main.py
```

You should see a summary of the extracted items grouped by type.

## Usage

### Run the script (reads `sample_input.txt` by default)

```bash
python main.py
```

If `sample_input.txt` is not found, the script will fall back to built-in demo text.

## Examples

### Using the included sample file

```bash
python main.py
```

Example output (shortened):

```text
========================================
Data Extraction Results:
========================================

EMAIL_ADDRESSES (2 found):
  - hustler1838@gmail.com
  - bknakuwa@tamam.co.uk

URLS (1 found):
  - https://www.google.com

... etc ...
```

### What each extractor matches

- **Emails**: `username@domain.tld`, including subdomains and multi-part TLDs
- **URLs**: `http` or `https` with optional subdomain, path, and query
- **Phone numbers**: Formats like `(123) 456-7890` or `123-456-7890`
- **Credit cards**: 16-digit groups with spaces or dashes
- **HTML tags**: Opening tags like `<p>` or `<div class="container">`
- **Hashtags**: Words prefixed by `#` (letters/numbers/underscore)

## Running Tests

This project uses a straightforward Python script with assertions. Run:

```bash
python tests/test_patterns.py
```

If all assertions pass, you'll see a confirmation message.

## Troubleshooting

- Ensure you are in the `alu_regex-data-extraction-nakuwa23` directory before running commands.
- If `python` invokes Python 2 on your system, use `python3` instead.

## Contributing

Contributions are highly welcome!

## Author

- Brian Nakuwa — `b.nakuwa@alustudent.com`
  - GitHub: https://github.com/nakuwa23
  - African Leadership University
