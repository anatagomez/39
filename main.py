import fitz
import re
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class Pdf2Text:
    def __call__(self, pdf_file):
        doc = fitz.open(pdf_file)
        text = ""
        for page_num in range(doc.page_count):
            page = doc[page_num]
            text += page.get_text()
        return text

class Text2Vector:
    def __call__(self, text):
        vectorizer = CountVectorizer().fit_transform([text])
        return vectorizer.toarray()

class CosineSim:
    def __call__(self, vector_from_table, vector_from_keyword):
        return cosine_similarity(vector_from_table, vector_from_keyword)[0][0]

def find_table_with_keyword(keyword, pdf_file):
    pdf2text = Pdf2Text()
    text2vector = Text2Vector()
    cosine_sim = CosineSim()

    pdf_text = pdf2text(pdf_file)

    tables = re.split(r'\n\s*\n', pdf_text)

    keyword_vector = text2vector(keyword)

    max_similarity = 0
    selected_table = None

    for table in tables:
        table_vector = text2vector(table)
        similarity = cosine_sim(table_vector, keyword_vector)
        
        if similarity > max_similarity:
            max_similarity = similarity
            selected_table = table

    return selected_table


def main(keyword, pdf_file):
    pdf_parser = pdf2text()
    table_text = pdf_parser(pdf_file)
    print(table_text)
    # return table


if __name__ == "__main__":
    main("keyword", "docs/1.pdf")
    main("keyword", "docs/2.pdf")
