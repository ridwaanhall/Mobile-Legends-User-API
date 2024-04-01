import re
import requests
from html.parser import HTMLParser
from tabulate import tabulate
from dotenv import load_dotenv
import os

load_dotenv()
url = os.getenv("URL_WIN")
response = requests.get(url)
json_data = response.json()

# Find the content with the desired ID
target_id = 2670508  # ID to search for
target_content = None
for item in json_data:
    if item["id"] == target_id:
        target_content = item["content"]["上周获奖名单"]["text"]
        break

if target_content:
    # Define a HTML parser
    class TableParser(HTMLParser):
        def __init__(self):
            super().__init__()
            self.data = []
            self.current_row = []
            self.in_row = False
            self.in_cell = False
            self.first_row_skipped = False

        def handle_starttag(self, tag, attrs):
            if tag == "tr":
                if not self.first_row_skipped:
                    self.first_row_skipped = True
                else:
                    self.in_row = True
                    self.current_row = []
            elif tag == "td":
                self.in_cell = True

        def handle_endtag(self, tag):
            if tag == "tr":
                if self.in_row:
                    self.in_row = False
                    self.data.append(self.current_row)
            elif tag == "td":
                self.in_cell = False

        def handle_data(self, data):
            if self.in_cell:
                data = re.sub(r'<span.*?>|</span>', '', data)
                self.current_row.append(data.strip())

    # Parse HTML table
    parser = TableParser()
    parser.feed(target_content)

    # Format the extracted data as a table
    table_data = []
    for row in parser.data:
        if row:
            table_data.append(row)

    # Print the table
    print(tabulate(table_data, headers=["User ID", "Server", "Prize"], tablefmt="grid"))
else:
    print("Content with the specified ID not found.")
