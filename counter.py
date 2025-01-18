import os
import PyPDF2
import re
import pandas as pd

def count_pdf_pages(pdf_file):
    """Count the number of pages in a PDF file."""
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        return num_pages

def list_pdf_files_in_directory(directory):
    """List all PDF files in the specified directory, sorted in ascending numerical order based on the file name."""
    # Get all files in the directory
    all_files = os.listdir(directory)
    
    # Filter only PDF files
    pdf_files = [f for f in all_files if f.lower().endswith('.pdf')]
    
    # Sort PDF files based on the numeric part of the file name
    pdf_files.sort(key=lambda f: int(re.findall(r'\d+', f)[0]))
    
    return pdf_files

def save_to_excel(pdf_data, output_file):
    """Save the PDF file name and page count data to an Excel file."""
    df = pd.DataFrame(pdf_data, columns=['name of file', 'number of pages'])
    df.to_excel(output_file, index=False)

def main():
    # Prompt the user for the directory containing PDF files
    directory = input("Enter the directory containing the PDF files: ").strip()
    
    # Check if the directory exists
    if not os.path.isdir(directory):
        print("The specified directory does not exist.")
        return

    # Get the list of PDF files in the directory
    pdf_files = list_pdf_files_in_directory(directory)

    if not pdf_files:
        print("No PDF files found in the specified directory.")
        return

    # List to hold file name (without .pdf) and page count
    pdf_data = []

    # Iterate through each PDF file, count pages, and store the result
    for pdf_file in pdf_files:
        pdf_path = os.path.join(directory, pdf_file)
        num_pages = count_pdf_pages(pdf_path)
        
        # Remove '.pdf' extension and store file name and number of pages
        pdf_data.append([pdf_file.replace('.pdf', ''), num_pages])
    
    # Prompt the user for the output Excel file name
    output_file = input("Enter the name of the output Excel file (with .xlsx extension): ").strip()
    
    # Save the data to Excel
    save_to_excel(pdf_data, output_file)
    print(f"Data has been saved to {output_file}")

# Run the program
if __name__ == "__main__":
    main()
