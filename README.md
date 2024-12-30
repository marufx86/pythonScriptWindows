# Python Scripts for Windows Automation

This repository contains a collection of Python scripts designed to automate various tasks on a Windows operating system. These scripts primarily focus on file processing, data manipulation, and system utilities, aiming to enhance productivity and streamline workflows.

## Overview

The scripts in this repository are designed to address common needs for users working with Windows, such as manipulating CSV files, renaming audio files, and converting contact lists into a format suitable for Google Contacts. They are written in Python and make use of common Python libraries.

## Key Features

*   **CSV Processing:** Scripts for reading and parsing data from CSV files, with options for basic data extraction or customized formatting.
*   **File Renaming:** Scripts designed to handle renaming of files, particularly audio files, with options for removing specific strings, replacing spaces, and adding prefixes for better file organization.
*   **Contact Conversion:** A script that takes a list of contact names and phone numbers, formats them, and saves them as a CSV file ready for importing into Google Contacts.
*   **Windows Focused:** The scripts assume a Windows environment with file paths and system interactions designed for Windows.

## Scripts

### `read_csv_basic.py`
*   **Purpose:** Reads a CSV file and prints each row to the console.
*   **Use Case:** Useful for quickly inspecting data in CSV files.

### `read_csv_formatted.py`
*   **Purpose:** Reads a CSV file, extracts data from each row, and prints it in a formatted manner.
*   **Use Case:** Useful for displaying specific data from CSV files in an organized format.

### `rename_wav_files_simple.py`
*   **Purpose:** Renames WAV files by removing a specific suffix from filenames.
*   **Use Case:** Helpful for batch renaming audio files to remove unwanted suffixes.

### `rename_wav_files_underscores.py`
*   **Purpose:** Renames WAV files by removing a suffix and replacing spaces with underscores in the filename.
*   **Use Case:** Good for standardizing filenames for use in applications or services that do not handle spaces well.

### `rename_wav_files_prefix.py`
*   **Purpose:** Renames WAV files by removing a suffix, replacing spaces with underscores, and adding a prefix to the filename.
*   **Use Case:** Useful for adding unique identifiers or labels to audio files, along with standardizing filename characters.

### `contacts_to_csv.py`
*   **Purpose:** Converts a list of contacts into a CSV format suitable for Google Contacts import.
*   **Use Case:** Makes it easy to move contact data from different sources to Google Contacts.

## Getting Started

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/marufx86/pythonScriptWindows.git
    cd pythonScriptWindows
    ```
2.  **Install Python:**
    If you don't have Python installed on your system, download it from [python.org](https://www.python.org/downloads/). Make sure to install it using options like "Add Python to PATH" to enable running the scripts from anywhere.
3.  **Modify File Paths:**
    The scripts contain hardcoded file paths that need to be updated to match your local file system. Open each script and change the paths to your desired files or folders.
4.  **Run the Scripts:**
    Open a command prompt or PowerShell window, navigate to the repository directory, and execute the scripts using `python <script_name>.py`.

## Requirements
*   Python 3.6 or higher
*   Basic understanding of running Python scripts
*   Correct file system access permissions
*   (Optional) A code editor like VS Code or Sublime Text to modify scripts
*   Required CSV files for scripts 1 and 2 and audio files for scripts 3, 4 and 5
## Contributing

Contributions to this project are welcome. Feel free to fork the repository, make changes, and submit a pull request.

## Disclaimer

The scripts provided here are for personal use and are provided "as-is". It is important to test these scripts on non-critical data before running them on important files or systems.

This project serves as a collection of quick and simple scripts and may not contain advanced error handling or features. Always back up your data before running any script to avoid any potential loss of data.
