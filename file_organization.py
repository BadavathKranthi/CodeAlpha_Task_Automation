import os
import shutil

def organize_files(source_folder, destination_folder):
    # Create destination folders if they don't exist
    for folder_name in file_extensions_mapping.values():
        os.makedirs(os.path.join(destination_folder, folder_name), exist_ok=True)

    # Iterate through files in the source folder
    for filename in os.listdir(source_folder):
        # Get the full path of the file
        source_file = os.path.join(source_folder, filename)

        # Check if it's a file
        if os.path.isfile(source_file):
            # Get the file extension
            _, file_extension = os.path.splitext(filename)
            file_extension = file_extension.lower()

            # Check if the file extension is in our mapping
            if file_extension in file_extensions_mapping:
                # Get the destination folder for the file extension
                destination_subfolder = file_extensions_mapping[file_extension]

                # Move the file to the appropriate folder
                destination_file = os.path.join(destination_folder, destination_subfolder, filename)
                shutil.move(source_file, destination_file)
                print(f"Moved '{filename}' to '{destination_subfolder}' folder.")

# Mapping of file extensions to destination folders
file_extensions_mapping = {
    ".txt": "TextFiles",
    ".pdf": "PDFs",
    ".jpg": "Images",
    ".png": "Images",
    ".xlsx": "Spreadsheets",
    ".csv": "Spreadsheets",
    ".docx": "Documents",
    ".zip": "Archives"
}

# Source and destination folders
source_folder = "source_folder"
destination_folder = "destination_folder"

# Call the function to organize files
organize_files(source_folder, destination_folder)
