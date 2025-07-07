from bbc_scraper import get_bbc_article_text

url = "https://www.bbc.com/news/articles/c07dmx38kyeo"
title, text = get_bbc_article_text(url)

print("TITLE:", title)
print("CONTENT:\n", text)
