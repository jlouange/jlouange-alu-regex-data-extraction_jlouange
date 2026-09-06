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
# emails

email_pattern = r"([a-zA-Z0-9](?:[a-zA-Z0-9._]*[a-zA-Z0-9])?)@((?:alueducation|alumni\.alueducation|si\.alueducation)\.com)(?![.\w<])"
emails = []
for line in raw_lines:
    clean_line = line.strip()  # Removes trailing \n and spaces
    if not clean_line:
        continue
    matches = re.finditer(email_pattern, clean_line)

    for match in matches:
        extracted_email = match.group(0)
        emails.append(extracted_email)



# phone number

phone_pattern = r"(?<!\d)(?:\+250[\s-]?\d{3}[\s-]?\d{3}[\s-]?\d{3}|0\d{9})(?!\d)"
phone_numbers = []
for line in raw_lines:
    clean_line = line.strip()  
    if not clean_line:
        continue
    matches = re.finditer(phone_pattern, clean_line)

    for match in matches:
        phone_number = match.group(0)
        phone_numbers.append(phone_number)



# credit card number

credit_pattern = r"(\d{4}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4})(?![-\w])"
credit_card_numbers = []
for line in raw_lines:
    clean_line = line.strip()  
    if not clean_line:
        continue
    matches = re.finditer(credit_pattern, clean_line)

    for match in matches:
        credit_card_number = match.group(0)
        credit_card_numbers.append(credit_card_number)



# URLs

url_pattern = r"https?:\/\/(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}(?:\/[a-zA-Z0-9](?:[a-zA-Z0-9._-]*[a-zA-Z0-9])?)*(?![a-zA-Z0-9._/-])"
urls_addresses = []
for line in raw_lines:
    clean_line = line.strip()  
    if not clean_line:
        continue
    matches = re.finditer(url_pattern, clean_line)

    for match in matches:
        url_address = match.group(0)
        urls_addresses.append(url_address)

print("EMAILS:", len(emails))
print(emails)

print("PHONES:", len(phone_numbers))
print(phone_numbers)

print("CARDS:", len(credit_card_numbers))
print(credit_card_numbers)

print("URLS:", len(urls_addresses))
print(urls_addresses)

json_data["emails"] = emails
json_data["phone_numbers"] = phone_numbers
json_data["credit_cards"] = credit_card_numbers
json_data["urls"] = urls_addresses

with open("output/sample-output.json", "w") as file:
    json.dump(json_data, file, indent=4)