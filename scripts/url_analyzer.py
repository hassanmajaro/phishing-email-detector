# url_analyzer.py
# Extracts URLs and scores them for phishing patterns

import re

def extract_urls(text):
    # Extract URLs from text using regex
    url_regex = r'(https?://[^\s]+)'
    return re.findall(url_regex, text)

def score_url(url):
    # Basic heuristics for suspicious URLs
    score = 0
    if url.count('-') > 1: score += 1
    if url.count('.') > 3: score += 1
    if len(url) > 75: score += 1
    if '@' in url or '//' in url[8:]: score += 1
    if re.search(r'\d{5,}', url): score += 1
    return score
