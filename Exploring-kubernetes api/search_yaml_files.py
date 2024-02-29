import os
def find_file(document_name):
    current_dir = os.getcwd()
    for root, dirs, files in os.walk(current_dir):
        if document_name in files:
            file_path = os.path.join(root, document_name)
            return file_path
    return None

if __name__ == "__main__":
    document_name = input("Enter the yaml file : ")
    file_path = find_file(document_name)
    if file_path:
        print("File found at:", file_path)
    else:
        print("File not found in the current directory or its subdirectories.Enter correct filename.")