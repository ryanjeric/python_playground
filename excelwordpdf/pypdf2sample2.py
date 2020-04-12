import PyPDF2
import os
os.chdir('pdf')

pdfFile1 = open('meetingminutes1.pdf','rb')
pdfFile2 = open('meetingminutes2.pdf','rb')

reader1 = PyPDF2.PdfFileReader(pdfFile1)
reader2 = PyPDF2.PdfFileReader(pdfFile2)

writer = PyPDF2.PdfFileWriter()
for pageNum in range(reader1.numPages):
    page = reader1.getPage(pageNum)
    writer.addPage(page)

for pageNum in range(reader2.numPages):
    page = reader2.getPage(pageNum)
    writer.addPage(page)

ouputFile = open('combinedMinutes.pdf','wb')
writer.write(ouputFile)
ouputFile.close()
pdfFile1.close()
pdfFile2.close()