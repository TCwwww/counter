import os
import re

def rename_pdf_files(directory):
    """Rename all PDF files in the directory by removing preceding alphabets and keeping only the numeric part."""
    # Get all files in the directory
    all_files = os.listdir(directory)
    
    # Filter only PDF files
    pdf_files = [f for f in all_files if f.lower().endswith('.pdf')]
    
    # Iterate through each PDF file and rename it
    for pdf_file in pdf_files:
        # Extract the numeric part of the file name
        new_name = re.sub(r'^[a-zA-Z]+', '', pdf_file)
        
        # Construct the full path for the old and new file names
        old_path = os.path.join(directory, pdf_file)
        new_path = os.path.join(directory, new_name)
        
        # Rename the file
        os.rename(old_path, new_path)
        print(f'Renamed "{pdf_file}" to "{new_name}"')

def main():
    # Prompt the user for the directory containing PDF files
    directory = input("Enter the directory containing the PDF files: ").strip()
    
    # Check if the directory exists
    if not os.path.isdir(directory):
        print("The specified directory does not exist.")
        return

    # Rename the PDF files in the directory
    rename_pdf_files(directory)
    print("Renaming complete.")

# Run the program
if __name__ == "__main__":
    main()
