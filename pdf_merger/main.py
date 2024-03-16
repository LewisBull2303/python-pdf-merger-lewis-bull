import PyPDF2
import sys
import os

#Created a variable for merging the pdf

merge_pdf = PyPDF2.PdfMerger()

#check over all the files in the directory

for file  in os.listdir(os.curdir):
    #check if the file ends with pdf
    if file.endswith("pdf"):
        merge_pdf.append(file)
        #make the final merged file
    merge_pdf.write("CombinedDocs.pdf")
    
