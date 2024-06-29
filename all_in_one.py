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
        if filename.endswith('.mrc'):
            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(destination_folder, filename)
            shutil.copy2(source_path, destination_path)
            print(f"Copied: {filename}")

def process_subdirectory(subdir):
    subdir_path = os.path.join(current_directory, subdir)
    
    # Check if the item is a directory
    if os.path.isdir(subdir_path):
        # Copy files to the 'all_in_one' folder
        copy_files(subdir_path, all_in_one_folder)

# Get the current working directory
current_directory = os.getcwd()

# Create 'all_in_one' folder
all_in_one_folder = os.path.join(current_directory, 'all_in_one')
create_folder(all_in_one_folder)

# List of subdirectories to process
subdirectories = [subdir for subdir in os.listdir(current_directory) if os.path.isdir(os.path.join(current_directory, subdir))]

# Calculate the number of threads to use
num_threads = min(multiprocessing.cpu_count(), 60)

# Use ThreadPoolExecutor for parallel processing without limiting concurrency
start_time = time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
    executor.map(process_subdirectory, subdirectories)

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Script completed in {elapsed_time:.2f} seconds.")