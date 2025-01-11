import os
import shutil

# Define the path to the folder of your choice 
downloads_folder = os.path.expanduser('~/Downloads')

# Define a dictionary to map file extensions to folder names
file_types = {
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Videos': ['.mp4', '.mkv', '.flv', '.avi', '.mov'],
    'Music': ['.mp3', '.wav', '.aac', '.flac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Scripts': ['.py', '.js', '.sh', '.bat'],
    'Others': []
}

# Create folders for each file type if they don't exist
for folder in file_types.keys():
    folder_path = os.path.join(downloads_folder, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Function to move files to their respective folders
def move_files():
    for filename in os.listdir(downloads_folder):
        file_path = os.path.join(downloads_folder, filename)
        if os.path.isfile(file_path):
            moved = False
            for folder, extensions in file_types.items():
                if any(filename.lower().endswith(ext) for ext in extensions):
                    shutil.move(file_path, os.path.join(downloads_folder, folder, filename))
                    moved = True
                    break
            if not moved:
                shutil.move(file_path, os.path.join(downloads_folder, 'Others', filename))


move_files()

print("Files have been organized.")
