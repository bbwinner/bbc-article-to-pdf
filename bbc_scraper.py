import requests
from bs4 import BeautifulSoup

def get_bbc_article_text(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    res = requests.get(url, headers=headers)

    if res.status_code != 200:
        raise Exception(f"Failed to fetch URL: {url}, status code: {res.status_code}")
    
    soup = BeautifulSoup(res.text, 'html.parser')

    # Get the title
    title_tag = soup.find("h1")
    title = title_tag.get_text(strip=True) if title_tag else "Untitled"

    # Find all <div> blocks with the given class
    containers = soup.find_all("div", class_="sc-3b6b161a-0 dEGcKf")
    
    # Collect all <p> tags with the correct class from all containers
    paragraphs = []
    for container in containers:
        paragraphs.extend(container.find_all("p", class_="sc-9a00e533-0 hxuGS"))
    
    # Join the paragraph texts
    body = "\n\n".join(p.get_text(strip=True) for p in paragraphs)

    return title, body
