import re
import json



with open ("input/raw-text.txt", "r") as file:
    raw_lines = file.readlines()

json_data = {
    "emails": [],
    "phone_numbers": [],
    "credit_cards": [],
    "urls": []
}
# emails extraction
def mask_email(email: str) -> str:
    """Mask an email username while keeping the domain visible."""
    username, domain = email.split("@")

    masked_username = username[0] + "*" * (len(username) - 1)

    return masked_username + "@" + domain

# Match valid ALU email addresses from the three allowed ALU domains.
# The username must start and end with an alphanumeric character.
# Dots and underscores are allowed inside the username.
email_pattern = r"([a-zA-Z0-9](?:[a-zA-Z0-9._]*[a-zA-Z0-9])?)@((?:alueducation|alumni\.alueducation|si\.alueducation)\.com)(?!\.[a-zA-Z0-9]|<)"
emails = []
for line in raw_lines:
    clean_line = line.strip()  
    if not clean_line:
        continue
    matches = re.finditer(email_pattern, clean_line)

    for match in matches:
        extracted_email = match.group(0)
        extracted_email = mask_email(extracted_email)
        emails.append(extracted_email)



# phone number extraction

def mask_phone(phone: str) -> str:
    """Mask the sensitive part of a Rwandan phone number."""
    if phone.startswith("+250"):
        if "-" in phone:
            parts = phone.split("-")
            return parts[0] + "-" + parts[1] + "-***-***"
        else:
            parts = phone.split()
            return parts[0] + " " + parts[1] + " *** ***"

    return phone[:4] + "*** ***"


# Match Rwandan phone numbers in international and local formats.
# Supports +250 numbers with optional spaces/hyphens and
# local numbers beginning with 0.
phone_pattern = r"(?<!\d)(?:\+250[\s-]?\d{3}[\s-]?\d{3}[\s-]?\d{3}|0\d{9})(?!\d)"
phone_numbers = []
for line in raw_lines:
    clean_line = line.strip()  
    if not clean_line:
        continue
    matches = re.finditer(phone_pattern, clean_line)

    for match in matches:
        phone_number = match.group(0)
        phone_number = mask_phone(phone_number)
        phone_numbers.append(phone_number)



# credit card number extraction

def mask_credit(credit: str) -> str:
    """Mask a credit card number and keep only the last four digits visible."""
    digits_only = "".join(char for char in credit if char.isdigit())
    last_4_digits = digits_only[-4:]
    masked = "*" * (len(digits_only) - 4)
    return masked + last_4_digits


# Match 16-digit credit card numbers with optional spaces or hyphens.
# The final boundary prevents matching a valid-looking card number
# when it is followed by additional word or separator characters.
credit_pattern = r"(\d{4}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4})(?![-\w])"
credit_card_numbers = []
for line in raw_lines:
    clean_line = line.strip()  
    if not clean_line:
        continue
    matches = re.finditer(credit_pattern, clean_line)

    for match in matches:
        credit_card_number = match.group(0)
        credit_card_number = mask_credit(credit_card_number)
        credit_card_numbers.append(credit_card_number)



# URL extraction


# Match HTTP and HTTPS URLs with a valid domain and optional path.
# The pattern is intentionally restrictive so malformed URLs
# such as "https://" are ignored.
url_pattern = r"https?:\/\/(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}(?:\/[a-zA-Z0-9](?:[a-zA-Z0-9._-]*[a-zA-Z0-9])?)*(?!\.[a-zA-Z0-9-])"
urls_addresses = []
for line in raw_lines:
    clean_line = line.strip()  
    if not clean_line:
        continue
    matches = re.finditer(url_pattern, clean_line)

    for match in matches:
        url_address = match.group(0)
        urls_addresses.append(url_address)



json_data["emails"] = emails
json_data["phone_numbers"] = phone_numbers
json_data["credit_cards"] = credit_card_numbers
json_data["urls"] = urls_addresses

with open("output/sample-output.json", "w") as file:
    json.dump(json_data, file, indent=4)


