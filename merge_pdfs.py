#!/usr/bin/env python
 
from os import sys
from PyPDF2 import PdfFileWriter, PdfFileReader

if __name__ == "__main__":
    if len(sys.argv) <> 3:
        print "Usage:", sys.argv[0] , "path_to_pdf_list_file path_to_out_pdf"
        sys.exit(2)

    l = [line.strip() for line in open(sys.argv[1])]

    writer = PdfFileWriter()

    for s in l:
        reader = PdfFileReader(s,strict=False)

        for i in range(reader.getNumPages()):
            writer.addPage( reader.getPage(i))


    with  open(sys.argv[2], "wb") as f:
        writer.write(f)
