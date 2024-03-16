import PyPDF2
import sys
import os

#Created a variable for merging the pdf

merger = PyPDF2.PdfMerger()

#check over all the files in the directory

for file  in os.listdir(os.curdir):
    #check if the file ends with pdf
    if file.endswith("pdf"):
        merger.append(file)
        #make the final merged file
    merger.write("CombinedDocs.pdf")
    
