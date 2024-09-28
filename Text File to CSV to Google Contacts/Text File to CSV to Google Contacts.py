# Contact numbers Text File to CSV to Google Contacts

import csv
import os

def create_contacts_csv(contacts, file_path):
    """
    Create a CSV file with contact information.
    
    :param contacts: List of tuples containing (name, phone_number)
    :param file_path: Path where the CSV file will be saved
    """
    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Open the CSV file for writing with UTF-8 encoding
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Write the header
        writer.writerow(["Name", "Phone Number"])
        
        # Write the contacts, removing the '+880' prefix if present
        for name, phone in contacts:
            if phone.startswith('+880'):
                phone = '0' + phone[4:]
            elif phone.startswith('880'):
                phone = '0' + phone[3:]
            writer.writerow([name, phone])

    print(f'CSV file saved as {file_path}')

# Example usage
if __name__ == "__main__":
    # File path where the csv will be saved
    csv_file_path = os.path.join(os.path.expanduser("~"), "Desktop", "google_contacts.csv")

    # Data extracted from your contact list, structured as Name, Phone Number pairs
    contacts = [
        ["Name1", "+8801947493737"],
        ["Name2", "+8801763737373"],
        # Add more contact info as needed
    ]

    create_contacts_csv(contacts, csv_file_path)

# Use case
#     - Update the 'contacts' list with your contact information
#     - Run this code and it will save a file onto your desktop
#     - Go to Google Contacts and press import, then pick the .csv file
#     - Done! Now you have all your contacts in your Google Contacts