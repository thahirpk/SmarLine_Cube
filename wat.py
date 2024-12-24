import fitz  # PyMuPDF
import os

def remove_annotations_and_form_fields(pdf_path, output_path):
    pdf_document = fitz.open(pdf_path)

    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)

        # Remove annotations
        annotations = page.annots()
        if annotations:
            for annot in annotations:
                page.delete_annot(annot)

        # Remove form fields
        for field in page.widgets():
            page.delete_widget(field)

    pdf_document.save(output_path)
    print(f"Processed PDF saved as: {output_path}")

def main():
    input_dir = r'C:\Users\JESVIN\Desktop\water mark\Input'  # Input directory containing PDF files
    output_dir = r'C:\Users\JESVIN\Desktop\water mark\Output'  # Output directory

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Fetch all PDF files in the input directory
    pdf_files = [f for f in os.listdir(input_dir) if f.lower().endswith('.pdf')]

    for pdf_file in pdf_files:
        input_pdf_path = os.path.join(input_dir, pdf_file)
        output_pdf_path = os.path.join(output_dir, pdf_file)

        # Remove annotations and form fields
        remove_annotations_and_form_fields(input_pdf_path, output_pdf_path)

if __name__ == '__main__':
    main()
