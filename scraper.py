import requests
from bs4 import BeautifulSoup
import time

BASE_URL = "https://easyitaliannews.com/category/notizie/"
HEADERS = {"User-Agent": "Mozilla/5.0"}

def get_articles_from_page(url):
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = []

    # Chaque article est dans un <article>
    for article in soup.find_all("article"):
        title_tag = article.find("h2")
        if title_tag:
            title = title_tag.get_text(strip=True)
            link = title_tag.find("a")["href"]
            articles.append((title, link))

    return articles


def scrape_all_pages(max_pages=5):
    all_articles = []

    for page in range(1, max_pages + 1):
        if page == 1:
            url = BASE_URL
        else:
            url = f"{BASE_URL}page/{page}/"

        print(f"Scraping: {url}")

        articles = get_articles_from_page(url)
        if not articles:
            break  # plus de pages

        all_articles.extend(articles)
        time.sleep(1)  # éviter de surcharger le site

    return all_articles


def get_article_content(url):
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")

    content_div = soup.find("div", class_="entry-content")
    if content_div:
        return content_div.get_text(strip=True)

    return ""


# --- utilisation ---
articles = scrape_all_pages(max_pages=3)

for title, link in articles:
    print("\n", title)
    content = get_article_content(link)
    print(content[:300])  # aperçu
