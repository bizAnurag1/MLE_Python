"""
Segregate file in small , medium and large size in different folder
filesize less than and equal to 10KB is small file
filesize more than 10 KB is the medium file
filesize more than 40 kb is the large file
"""
import os
import shutil

def create_folders(base_path):
    """Creates folders for small, medium, and large files if they don't already exist."""
    small_folder = os.path.join(base_path, 'small_files')
    medium_folder = os.path.join(base_path, 'medium_files')
    large_folder = os.path.join(base_path, 'large_files')

    for folder in [small_folder, medium_folder, large_folder]:
        if not os.path.exists(folder):
            os.makedirs(folder)

    return small_folder, medium_folder, large_folder

def segregate_files(base_path):
    """
    Segregates files into small, medium, and large folders based on their size.
    base_path (str): The path of the directory containing files to be segregated.
    """
    small_folder, medium_folder, large_folder = create_folders(base_path)

    for filename in os.listdir(base_path):
        file_path = os.path.join(base_path, filename)
        if os.path.isfile(file_path):
            file_size = os.path.getsize(file_path) / 1024  # size in KB
            if file_size <= 10:
                shutil.move(file_path, small_folder)
            elif file_size <= 40:
                shutil.move(file_path, medium_folder)
            else:
                shutil.move(file_path, large_folder)

if __name__ == "__main__":
    path = input("Enter the directory path :")
    segregate_files(path)
    print("Files have been segregated into small, medium, and large folders.")
