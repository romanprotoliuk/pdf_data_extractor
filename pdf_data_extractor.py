import PyPDF2
import re
import json

pdf_file = open('roman-allergy-results.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Define regular expressions
food_name_regex = r'[A-Za-z\'\s]+'

# Extract the text from the PDF file
pdf_text = ""
for page_num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[page_num]
    pdf_text += page.extract_text()

# Extract the food items using regular expressions
food_items = []
for match in re.finditer(food_name_regex, pdf_text):
    name = match.group(0)
    food_items.append({'name': name.strip()})

# Write the extracted data to a JSON file
with open('output.json', 'w') as outfile:
    json.dump(food_items, outfile)

# Print a success message
print("Data written to output.json", food_items)
