# Simple File Organization Script

A simple file organization script written in Python.

## Description

This script organizes files in the `Downloads` folder into subfolders based on their file extensions. The subfolders are created for different file types such as Documents, Images, Videos, Music, Archives, Scripts, and Others.

## Setup

1. Ensure you have Python installed on your system.
2. Clone this repository or download the script.

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory containing `index.py`.
3. Run the script using the following command:

    - For macOS and Linux:
      ```sh
      python3 index.py
      ```
    - For Windows:
      ```sh
      python index.py
      ```

## How It Works

- The script defines a dictionary `file_types` that maps folder names to lists of file extensions.
- It creates subfolders in the `Downloads` directory OR any folder of your choice for each file type if they do not already exist.
- It moves files from the `Downloads` folder Or any folder of your choice to the appropriate subfolder based on their file extension.
- Files that do not match any of the specified extensions are moved to the `Others` folder.

## Dependencies

- This script uses the built-in `os` and `shutil` modules, so no additional dependencies are required.

## License

This project is licensed under the MIT License.
