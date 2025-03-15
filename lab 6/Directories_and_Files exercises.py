# 1. List only directories, files, and all contents in a specified path

import os

def list_contents(path):
    print("Directories:")
    print([d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])

    print("\nFiles:")
    print([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])

    print("\nAll Contents:")
    print(os.listdir(path))

# Example usage
path = "."  # Change this to your desired path
list_contents(path)

# 2. Check access to a specified path (existence, readability, writability, executability)

import os

def check_access(path):
    print(f"Exists: {os.path.exists(path)}")
    print(f"Readable: {os.access(path, os.R_OK)}")
    print(f"Writable: {os.access(path, os.W_OK)}")
    print(f"Executable: {os.access(path, os.X_OK)}")

# Example usage
path = "test.txt"  # Change this to your file or directory
check_access(path)

# 3. Check if a path exists and find filename and directory portion

import os

def check_path(path):
    if os.path.exists(path):
        print(f"Path exists: {path}")
        print(f"Directory: {os.path.dirname(path)}")
        print(f"Filename: {os.path.basename(path)}")
    else:
        print("Path does not exist")

# Example usage
path = "test.txt"
check_path(path)

# 4. Count the number of lines in a text file

def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            return sum(1 for line in file)
    except FileNotFoundError:
        print("File not found")

# Example usage
filename = "test.txt"
print(f"Number of lines: {count_lines(filename)}")

# 5. Write a list to a file

def write_list_to_file(filename, data):
    with open(filename, 'w') as file:
        file.writelines(f"{item}\n" for item in data)

# Example usage
data = ["Apple", "Banana", "Cherry"]
write_list_to_file("fruits.txt", data)

# 6. Generate 26 text files (A.txt to Z.txt)

import string

for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", 'w') as file:
        file.write(f"This is file {letter}.txt\n")

print("26 files created.")

# 7. Copy the contents of a file to another file

def copy_file(source, destination):
    try:
        with open(source, 'r') as src, open(destination, 'w') as dest:
            dest.write(src.read())
        print("File copied successfully")
    except FileNotFoundError:
        print("Source file not found")

# Example usage
copy_file("source.txt", "destination.txt")

# 8. Delete a file after checking access and existence

import os

def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print("File deleted")
        else:
            print("No permission to delete file")
    else:
        print("File does not exist")

# Example usage
delete_file("test.txt")


