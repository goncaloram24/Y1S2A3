import PyPDF2
import re

BookTitle = "Ulysses"


'''
Function Name: RemoveHeaderAndFooter

Purpose: The function takes in the title of the book being converted and a string of one of the book's page. The goal
is to remove the header and footer off of that string.

Input:
- pdf_title (string): The title of the book
- pgtxt (string): The string to be filtered

Output:
- (string) pgtxt filtered (meaning: without Header and Footer)

Pseudo-Example:
>>> RemoveHeaderAndFooter("Ulysses", "HEADER Ulysses was a strong man. FOOTER")
Ulysses was a strong man.

'''
def RemoveHeaderAndFooter(pdf_title, pgtxt):
    if(pdf_title == "Ulysses"):
        # the string to search

        # search for the number
        match1 = re.search(r"of 1305", pgtxt)
        match2 = re.search(r"Ulysses"[::-1], pgtxt[::-1])
        lastmatch = re.search(r"Trieste-Zurich-Paris 1914-1921"[::-1], pgtxt[::-1])

        # if match1 is found
        if match1:
            # get the starting position of the number
            start = match1.end()
            # extract the substring after the number
            pgtxt = pgtxt[start:]
        else:
            #print("Footer not found.")
            return 1

        # if match2 is found
        if lastmatch:
            # get the starting position of the number
            end = len(pgtxt) - lastmatch.end()
            # extract the substring after the number
            pgtxt = pgtxt[:end]
        elif match2:
            # get the starting position of the number
            end = len(pgtxt) - match2.end()
            # extract the substring after the number
            pgtxt = pgtxt[:end]
        else:
            #print("Header not found.")
            return 0

    return pgtxt


# open the pdf file
with open("PDFs/" + BookTitle + ".pdf", "rb") as file:
    # create a pdf reader object
    pdf_reader = PyPDF2.PdfFileReader(file)

    # get the number of pages in the pdf
    num_pages = pdf_reader.numPages

    # create a variable to store the text
    text = ""

    # iterate through each page
    for page_num in range(num_pages):

        # get the page object
        page = pdf_reader.getPage(page_num)

        # extract the text from the page
        page_text = page.extractText()
        if re.search(r"Trieste-Zurich-Paris 1914-1921", page_text):
            print("break")

        page_text = RemoveHeaderAndFooter(BookTitle, page_text)

        if not isinstance(page_text, (int, float)):
            text += page_text

# print the text
print(text)

# write the text to a new text file
with open("TXTs/Ulysses.txt", "w") as file:
    file.write(text)
