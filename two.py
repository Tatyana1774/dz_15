import csv

with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'first_name': 'Tatyana', 'last_name': 'Chulkova'})
    writer.writerow({'first_name': 'Anetta', 'last_name': 'Sergeeva'})
    writer.writerow({'first_name': 'Elya', 'last_name': 'Sallina'})
    writer.writerow({'first_name': 'Alyuona', 'last_name': 'Saharova'})
# 13
# 13
# 16

with open('names.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['first_name'], row['last_name'])
