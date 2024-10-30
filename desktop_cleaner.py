import os
import shutil

# Define your desktop path
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Define folders for each file type
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Audio": [".mp3", ".wav"],
    "Videos": [".mp4", ".mov"],
    "Archives": [".zip", ".rar", ".tar"],
    "Others": []
}

# Create folders if they don't exist
for folder in file_types:
    folder_path = os.path.join(desktop_path, folder)
    os.makedirs(folder_path, exist_ok=True)

# Move files into their respective folders
for filename in os.listdir(desktop_path):
    file_path = os.path.join(desktop_path, filename)
    if os.path.isfile(file_path):
        file_ext = os.path.splitext(filename)[1].lower()
        moved = False
        for folder, extensions in file_types.items():
            if file_ext in extensions:
                shutil.move(file_path, os.path.join(desktop_path, folder))
                moved = True
                break
        if not moved:
            shutil.move(file_path, os.path.join(desktop_path, "Others"))
