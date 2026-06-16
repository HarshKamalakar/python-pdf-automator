import os
from pypdf import PdfReader, PdfWriter

def compile_master_pdf():
    print("=== PDF BATCH PRINT AUTOMATOR ===")
    print("Compiles multiple PDFs into a single master file, sequenced in 3 sets per document.\n")
    
    # Generic prompt for the user to input their target folder
    folder_path = input(r"Enter the full folder path containing the PDFs: ").strip()
        
    if not os.path.exists(folder_path):
        print("Error: The specified folder does not exist.")
        return

    master_filename = "Master_Ready_To_Print.pdf"
    master_filepath = os.path.join(folder_path, master_filename)

    # Fetch all PDF files except the master if it already exists
    pdf_files = [f for f in os.listdir(folder_path) 
                 if f.lower().endswith(".pdf") and f != master_filename]
    
    total_files = len(pdf_files)
    if total_files == 0:
        print(f"No PDFs found in {folder_path}!")
        return

    print(f"\nFound {total_files} PDFs. Building the Master File...\n")
    writer = PdfWriter()

    # Helper function to add pages and calculate blank page padding for duplex printing
    def add_pages_and_pad(reader, num_pages):
        # Add requested pages
        for i in range(num_pages):
            writer.add_page(reader.pages[i])
            
        # Check if blank pages are needed to round up to a multiple of 4
        remainder = num_pages % 4
        if remainder != 0:
            blanks_to_add = 4 - remainder
            page_width = reader.pages[0].mediabox.width
            page_height = reader.pages[0].mediabox.height
            for _ in range(blanks_to_add):
                writer.add_blank_page(width=page_width, height=page_height)

    # Process each PDF in the directory
    for index, filename in enumerate(pdf_files, start=1):
        filepath = os.path.join(folder_path, filename)
        print(f"Processing ({index}/{total_files}): {filename}")
        
        try:
            reader = PdfReader(filepath)
            total_pages = len(reader.pages)
            
            # The logic extracts up to 4 pages for the short sets, or the full document length
            pages_to_extract = min(4, total_pages)
            
            # Set 1: Short copy (First 4 pages) + blank padding
            add_pages_and_pad(reader, pages_to_extract)
            
            # Set 2: Short copy (First 4 pages) + blank padding
            add_pages_and_pad(reader, pages_to_extract)
            
            # Set 3: Full master copy + blank padding
            add_pages_and_pad(reader, total_pages)
            
        except Exception as e:
            print(f" -> Error reading {filename}: {e}")

    print("\nSaving Master File... This might take a few seconds.")
    with open(master_filepath, "wb") as f:
        writer.write(f)
        
    print(f"\nSUCCESS! Master file created at:\n{master_filepath}")

if __name__ == "__main__":
    compile_master_pdf()