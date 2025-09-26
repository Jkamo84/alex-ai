import csv

file_path = "example.csv"  # Replace with your CSV file path

with open(file_path, "r", newline="") as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        print(row)  # Each row is a list of strings
        ## transformar esto a un dict, y eso pasarlo a DB
