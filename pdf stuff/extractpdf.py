from pdfquery import PDFQuery
import re
import os

filename="example8.pdf"

pdf = PDFQuery(filename)

pdf.load()

print(pdf.doc.catalog)
# print(pdf.get_layouts())

text_elements = pdf.pq('LTTextLineHorizontal')

# Extract the text from the elements
text = [t.text for t in text_elements]
print("\n")

print(text)
