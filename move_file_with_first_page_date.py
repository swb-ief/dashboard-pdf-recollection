import datetime
import pdfplumber
import argparse
import os
from pathlib import Path
from shutil import copyfile

parser = argparse.ArgumentParser(description='Process with path.')

parser.add_argument('pdf_path', metavar='N', type=str,
                    help='PDF path')

args = parser.parse_args()


PDF_RESULT_PATH = Path('./pdf-with-correct-date')
new_pdf_dir = os.makedirs(PDF_RESULT_PATH, exist_ok=True)
pdf_path = args.pdf_path

with pdfplumber.open(pdf_path) as pdf:
    first_page = pdf.pages[0]
    date_of_pdf = first_page.extract_text().split('\n')[2]
    parsed_date = datetime.datetime.strptime(date_of_pdf, '%b %d, %Y')
    pdf_name_date = parsed_date.strftime('%Y-%m-%d')
    new_pdf_filename = f"{pdf_name_date}-mcgm.stopcoronavirus.pdf"
    copyfile(pdf_path, os.path.join(PDF_RESULT_PATH, new_pdf_filename))

