import re

# Read text from file
with open("test_inputs.txt", "r") as file:
    text = file.read()

def extract_emails(text):
    # Regex to match emails, avoid trailing punctuation
    pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+(?=\s|$|[,.\)])'
    return re.findall(pattern, text)

def extract_urls(text):
    # Regex to match URLs, avoid trailing punctuation
    pattern = r'https?://[^\s,.]+'
    return re.findall(pattern, text)

def extract_phone_numbers(text):
    # Match different phone formats
    pattern = r'(\(\d{3}\)\s?\d{3}[-.]\d{4}|\d{3}[-.]\d{3}[-.]\d{4})'
    return re.findall(pattern, text)

def extract_credit_cards(text):
    # Match credit cards with spaces or dashes
    pattern = r'\b(?:\d{4}[- ]?){3}\d{4}\b'
    return re.findall(pattern, text)

def extract_times(text):
    # Match 24h and 12h times with AM/PM optional
    pattern = r'\b((1[0-9]|2[0-3]|0?[0-9]):[0-5][0-9]\s?(AM|PM|am|pm)?)\b'
    return re.findall(pattern, text)

def extract_html_tags(text):
    # Match HTML tags with attributes
    pattern = r'<[^>]+>'
    return re.findall(pattern, text)

def extract_hashtags(text):
    # Match hashtags
    pattern = r'#[A-Za-z0-9_]+'
    return re.findall(pattern, text)

def extract_currency(text):
    # Match dollar amounts with commas and decimals
    pattern = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
    return re.findall(pattern, text)

# Print extracted data
print("📧 Emails:", extract_emails(text))
print("🌐 URLs:", extract_urls(text))
print("📞 Phone Numbers:", extract_phone_numbers(text))
print("💳 Credit Card Numbers:", extract_credit_cards(text))
print("⏰ Times:", [t[0] for t in extract_times(text)])
print("🔖 HTML Tags:", extract_html_tags(text))
print("🏷️ Hashtags:", extract_hashtags(text))
print("💵 Currency Amounts:", extract_currency(text))


