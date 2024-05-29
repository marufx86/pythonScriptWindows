import csv

# Prompt the user for the CSV file path
csv_file_path = r"C:\Users\Mifunee\Desktop\CSV TEST\test.csv"

# Open the CSV file
with open(csv_file_path, 'r') as file:
    # Create a CSV reader object
    reader = csv.reader(file)

    # Skip the header row
    next(reader)

    # Iterate over each row in the CSV file
    for row in reader:
        # Print the row data
        print(row)


######################################################################

import csv

# Prompt the user for the CSV file path
csv_file_path = r"C:\Users\Mifunee\Desktop\CSV TEST\test.csv"

# Open the CSV file
with open(csv_file_path, 'r') as file:
    # Create a CSV reader object
    reader = csv.reader(file)

    # Skip the header row
    header = next(reader)

    # Iterate over each row in the CSV file
    for row in reader:
        # Unpack the row data
        Fruit, Color, Usual_Size = row

        # Print the row data in the desired format
        print("Fruit =", Fruit)
        print("Color =", Color)
        print("Usual_Size =", Usual_Size)
        print()  # Print an empty line for readability