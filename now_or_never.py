import os
import shutil
import concurrent.futures
import time
import multiprocessing

def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def copy_files(source_folder, destination_folder):
    for filename in os.listdir(source_folder):
        if filename.endswith('.mrc') and 'Fractions' not in filename:
            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(destination_folder, filename)
            shutil.copy2(source_path, destination_path)
            print(f"Copied: {filename}")

def process_subdirectory(subdir):
    subdir_path = os.path.join(current_directory, subdir)
    
    # Check if the item is a directory and contains a 'Data' folder
    if os.path.isdir(subdir_path) and 'Data' in os.listdir(subdir_path):
        data_folder_path = os.path.join(subdir_path, 'Data')
        destination_folder = os.path.join(ready_to_process_folder, f'without_fractions_{subdir}')

        # Create the 'without_fractions' folder for each subdirectory
        create_folder(destination_folder)

        # Copy files with the specified conditions to the new folder
        copy_files(data_folder_path, destination_folder)

# Get the current working directory
current_directory = os.getcwd()

# Create 'ready_to_processinseconds' folder
ready_to_process_folder = os.path.join(current_directory, 'ready_to_processinseconds')
create_folder(ready_to_process_folder)

# List of subdirectories to process
subdirectories = [subdir for subdir in os.listdir(current_directory) if os.path.isdir(os.path.join(current_directory, subdir))]

# Use ThreadPoolExecutor for parallel processing without limiting concurrency
start_time = time.time()
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(process_subdirectory, subdirectories)

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Script completed in {elapsed_time:.2f} seconds.")