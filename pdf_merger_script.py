import PyPDF2
import sys

inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
	merger = PyPDF2.PdfFileMerger()
	for pdf in pdf_list:
		merger.append(pdf)
	merger.write('merged_pdf.pdf')
	print('PDF files merged successfully!')

pdf_combiner(inputs)

