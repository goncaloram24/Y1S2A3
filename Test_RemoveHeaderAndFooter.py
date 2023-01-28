import unittest
import re

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

class TestRemoveHeaderAndFooter(unittest.TestCase):
    def test_RemoveHeaderAndFooter(self):
        self.assertEqual(RemoveHeaderAndFooter("Ulysses", "random string"), 1)
        self.assertEqual(RemoveHeaderAndFooter("Ulysses", "random string Ulysses"), 1)
        self.assertEqual(RemoveHeaderAndFooter("Ulysses", "1 of 1305 bla bla"), 0)
        self.assertEqual(RemoveHeaderAndFooter("Ulysses", "5 of 1305 bla bla Trieste-Zurich-Paris 1914-1921"), " bla bla ")
        self.assertEqual(RemoveHeaderAndFooter("Ulysses", "1000 of 1305 bla Ulysses bla Trieste-Zurich-Paris 1914-1921"), " bla Ulysses bla ")
        self.assertEqual(RemoveHeaderAndFooter("Ulysses", "wtv of 1305 bla bla Ulysses"), " bla bla ")
        self.assertEqual(RemoveHeaderAndFooter("Ulysses", "1305 of 1305 bla bla Ulysses"), " bla bla ")

if __name__ == '__main__':
    unittest.main()
