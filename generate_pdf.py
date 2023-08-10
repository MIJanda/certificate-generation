# generate_pdf.py
from weasyprint import HTML

def generate_pdf(input_html, output_pdf):
    # Read the HTML file and generate PDF
    HTML(input_html).write_pdf(output_pdf)

if __name__ == "__main__":
    input_html_file = "certificate.html"  # Path to your input HTML file
    output_pdf_file = "certificate.pdf"  # Path to the output PDF file

    generate_pdf(input_html_file, output_pdf_file)
