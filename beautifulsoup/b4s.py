from bs4 import BeautifulSoup
import csv

# html = open("mlb.html").read()
html = open("table.html").read()
soup = BeautifulSoup(html, features="lxml")
table = soup.find("table")
output_rows = []
for table_row in table.findAll('tr')[1:]:
    columns = table_row.findAll('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
with open('output.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)
