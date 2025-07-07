from bbc_scraper import get_bbc_article_text
from pdf_writer import save_pdf

# url = "https://www.bbc.com/news/articles/c07dmx38kyeo"
url = input("Please input the url: ")
title, text = get_bbc_article_text(url)

# print("TITLE:", title)
# print("CONTENT:\n", text)

save_pdf(title, text, filename="_".join(list(title.split())))
