import os
from fpdf import FPDF

def save_to_pdf(content, filename, folder):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    # Splitting content into lines to fit in PDF
    lines = content.split('\n')
    for line in lines:
        pdf.multi_cell(0, 10, line)
    
    # Create folder if it doesn't exist
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    pdf_output_path = os.path.join(folder, f"{filename}.pdf")
    pdf.output(pdf_output_path)
    print(f"Saved PDF: {pdf_output_path}")
