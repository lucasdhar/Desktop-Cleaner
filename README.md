# Desktop Cleaner

A Python script that automatically cleans up your desktop by organizing files into categorized folders. The script helps you keep your desktop organized by moving files into folders based on file types, such as Documents, Images, Videos, Music, etc.

## Features

- Automatically organizes files on your desktop.
- Moves files into predefined categories (Documents, Images, Videos, Music, etc.).
- Option to specify custom folders for different file types.
- Simple to use and runs as a standalone Python script.

## Technologies Used

- **Python**: The script is written in Python.
- **os module**: Used to interact with the operating system for file management.
- **shutil module**: Used for moving files between directories.

## Installation

### Prerequisites

- Python 3.x installed on your system.

### Steps to Run the Script

1. Clone the repository:
   ```bash
   git clone https://github.com/lucasdhar/Desktop-Cleaner.git
Navigate to the Desktop-Cleaner directory:

bash
Copy code
cd Desktop-Cleaner
Run the script:

bash
Copy code
python desktop_cleaner.py
The script will start cleaning your desktop by organizing the files into respective folders.

###How It Works
The script scans your desktop for all files.
It categorizes the files based on file extensions (e.g., .txt for Documents, .jpg for Images).
It moves the files into corresponding folders such as Documents, Images, Videos, Music, etc.
If the folder does not exist, the script will create it automatically.

###Customizing the Script
You can customize the file types and their corresponding categories in the script by editing the file_types dictionary.
You can also specify the folders where the files should be moved by modifying the destination_folders.

###License
This project is licensed under the MIT License - see the LICENSE file for details.
