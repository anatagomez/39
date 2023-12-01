git@github.com:anatagomez/39.git


def main(keyword, pdf_file):
    pdf_parser = pdf2text()
    table_text = pdf_parser(pdf_file)
    print(table_text)
    # return table


if __name__ == "__main__":
    main("keyword", "docs/1.pdf")
    main("keyword", "docs/2.pdf")
