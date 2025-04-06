from pdfquery import PDFQuery
import re
import os

filename="example7.pdf"

pdf = PDFQuery(filename)

pdf.load()

print(pdf.doc.catalog)
# print(pdf.get_layouts())

text_elements = pdf.pq('LTTextLineHorizontal')

# Extract the text from the elements
text = [t.text for t in text_elements]
print("\n")

print(text)

print("\n\n")

# print(type(text))

# print(text[0])


cardTitle=""
cardCategory=text[0]

for val in text:
    # print("Value: ",val)
    if val==cardCategory:
        # print("Skip Title")
        continue
    if cardTitle == "":
        # print("First title Title")
        cardTitle = val
    elif '●●' in val:
        # print("Quit")
        break
    elif val ==", ":
        break
    elif val ==" ":
        break
    elif val =="":
        break
    elif "If you" in val:
        break
    elif "While it" in val:
        break
    elif val == "NAME ":
        continue
    else:
        # print("Append to title")
        cardTitle += val
    
# print(cardTitle.title())
newCardName=cardTitle.title().rstrip() + " - " + cardCategory.title().rstrip() + ".pdf"

print(newCardName)

# os.rename(filename,newCardName)




# stringtext=str(text)
# print("\n\n")
# print stringtext

# fn= re.search("\['\w+ ', (['\w+ ',]+).*",text)
# print(fn)


# txt = "The rain in Spain"
# print(txt)
# print("\n")
# myExtract = re.search("^The(.*)Spain$", txt)
# print(myExtract)
# print("\n")
# m = re.search("^The(.*)Spain$", txt).group(1)
# print(m);
