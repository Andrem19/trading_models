import os
import csv

path = 'cases'
target_path = 'finaly'

# Get all CSV files in the specified path
csv_files = [file for file in os.listdir(path) if file.endswith('.csv')]

# Create the output file in the target path
output_file = os.path.join(target_path, 'training_data.csv')

# Iterate over each CSV file and write its data into the output file
with open(output_file, 'w', newline='') as outfile:
    writer = csv.writer(outfile)

    for csv_file in csv_files:
        file_path = os.path.join(path, csv_file)

        with open(file_path, 'r') as infile:
            reader = csv.reader(infile)

            for row in reader:
                writer.writerow(row)
