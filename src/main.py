import re
import json

# emails

with open ("input/raw-text.txt", "r") as file:
    data = file.readlines()

email_pattern = r"([a-zA-Z0-9](?:[a-zA-Z0-9._]*[a-zA-Z0-9])?)@((?:alueducation|alumni\.alueducation|si\.alueducation)\.com)(?![.\w<])"
emails = []
for line in data:
    clean_line = line.strip()  # Removes trailing \n and spaces
    if not clean_line:
        continue
    match = re.search(email_pattern, clean_line)

    if match:
        username = match.group(1)
        domain = match.group(2)
        extracted_email = username + "@" + domain
        emails.append(extracted_email)
with open("output/sample-output.json", "r") as file:
    data1 = json.load(file)
for email in emails:
    data1["emails"].append(email)

with open("output/sample-output.json", "w") as file:
    json.dump(data1, file, indent=4)

# phone number

phone_pattern = r"(?:(?:\+?250[\s-]?)?(\d{3}[ -]\d{3}[ -]\d{3}))|(0\d{9})"
phone_numbers = []
for line in data:
    clean_line = line.strip()  
    if not clean_line:
        continue
    match = re.search(phone_pattern, clean_line)
    if match:
        phone_number = match.group(0)
        phone_numbers.append(phone_number)

with open("output/sample-output.json", "r") as file:
    data1 = json.load(file)
for phone_number in phone_numbers:
    data1["phone_numbers"].append(phone_number)

with open("output/sample-output.json", "w") as file:
    json.dump(data1, file, indent=4)


credit_pattern = r"(\d{4}[ -]?\d{4}[ -]?\d{4}[ -]?\d{4})(?![-\w])"
credit_card_numbers = []
for line in data:
    clean_line = line.strip()  
    if not clean_line:
        continue
    match = re.search(credit_pattern, clean_line)
    if match:
        credit_card_number = match.group(0)
        credit_card_numbers.append(credit_card_number)

with open("output/sample-output.json", "r") as file:
    data1 = json.load(file)
for credit_card_number in credit_card_numbers:
    data1["credit_cards"].append(credit_card_number)

with open("output/sample-output.json", "w") as file:
    json.dump(data1, file, indent=4)
