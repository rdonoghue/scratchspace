from pdfquery import PDFQuery

import os
directoryString='/Users/rdonoghue/projects/Card PDFs/Staging Folder'
directory = os.fsencode(directoryString)
    
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".pdf"):
        # print(filename)
        fullFileName=str(directoryString+"/"+filename)
        pdf = PDFQuery(fullFileName)
        pdf.load()
        text_elements = pdf.pq('LTTextLineHorizontal')
        # print(fullFileName)


        text_elements = pdf.pq('LTTextLineHorizontal')
        text = [t.text for t in text_elements]
        cardCategory=text[0]
        cardTitle=""
        for val in text:
            if val==cardCategory:
                continue
            if cardTitle == "":
                cardTitle = val
            elif '●●' in val:
                break
            elif val == ", ":
                break
            elif val ==" ":
                break
            elif val =="":
                break
            elif "If you" in val:
                break
            elif "Once you" in val:
                break
            elif "While it" in val:
                break
            elif val == "NAME ":
                continue
            else:
                cardTitle += val
        newCardName=cardTitle.title().rstrip() + " - " + cardCategory.title().rstrip() + ".pdf"
        print(newCardName)
        newFileName=str(directoryString+"/"+newCardName)

        # print(newFileName)
        # os.rename(fullFileName,newFileName)


    else:
        continue
