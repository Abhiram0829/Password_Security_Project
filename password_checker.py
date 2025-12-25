import re
import requests
import hashlib

def check_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    return score

def check_breach(password):
    sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5, tail = sha1[:5], sha1[5:]
    url = f'https://api.pwnedpasswords.com/range/{first5}'
    res = requests.get(url)
    if res.status_code != 200:
        return False
    hashes = (line.split(':') for line in res.text.splitlines())
    for h, count in hashes:
        if h == tail:
            return True
    return False

def calculate_risk(password):
    score = check_strength(password)
    breached = check_breach(password)
    if breached:
        risk = "HIGH"
    elif score <= 2:
        risk = "MEDIUM"
    else:
        risk = "LOW"
    return score, risk, breached
