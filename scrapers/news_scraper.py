import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json
import os

# def scrape_moneycontrol():
#     url = "https://www.moneycontrol.com/news/business/markets/"
#     response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
#     soup = BeautifulSoup(response.text, 'html.parser')

#     articles = []

#     for item in soup.select('li.clearfix'):
#         title_tag = item.find('h2').find('a')
#         # title1 = title_tag.get('title', '')
#         summary_tag = item.find('p')
#         # print("Title:" , title1)
#         # print("Summary:" , summary_tag)
#         if title_tag and summary_tag:
#             title = title_tag.get('title', '')
#             summary = summary_tag.get_text(strip=True)
#             link = title_tag['href']
#             # print("Link:" , link)
#             articles.append({
#                 'source': 'Moneycontrol',
#                 'title': title,
#                 'summary': summary,
#                 'url': link,
#                 'timestamp': datetime.now().isoformat()
#             })

#     return articles

def scrape_moneycontrol(max_pages=30):
    base_url = "https://www.moneycontrol.com/news/business/markets"
    articles = []

    for page in range(1, max_pages + 1):
        url = base_url if page == 1 else f"{base_url}/page-{page}/"
        print(f"🔎 Scraping page {page}: {url}")
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        
        if response.status_code != 200:
            print(f"❌ Failed to load page {page}")
            break

        soup = BeautifulSoup(response.text, 'html.parser')
        items = soup.select('li.clearfix')

        if not items:
            print("🚫 No more articles found.")
            break

        for item in items:
            title_tag = item.find('h2')
            if title_tag:
                a_tag = title_tag.find('a')
                summary_tag = item.find('p')

                if a_tag and summary_tag:
                    title = a_tag.get('title', '')
                    summary = summary_tag.get_text(strip=True)
                    link = a_tag['href']
                    articles.append({
                        'source': 'Moneycontrol',
                        'title': title,
                        'summary': summary,
                        'url': link,
                        'timestamp': datetime.now().isoformat()
                    })

    print(f"✅ Total articles scraped: {len(articles)}")
    return articles


def scrape_livemint():
    url = "https://www.livemint.com/market"
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = []

    for item in soup.select('section.listingPage > ul > li'):
        link_tag = item.find('a', href=True)
        if link_tag:
            title = link_tag.get_text(strip=True)
            link = "https://www.livemint.com" + link_tag['href']

            articles.append({
                'source': 'LiveMint',
                'title': title,
                'summary': '',
                'url': link,
                'timestamp': datetime.now().isoformat()
            })

    return articles


def scrape_all_news():
    mc = scrape_moneycontrol()
    # lm = scrape_livemint()
    return mc


if __name__ == "__main__":
    news = scrape_all_news()
    with open("scraped_news.json", "w") as f:
        json.dump(news, f, indent=2)
    # for article in news[:5]:  # Just show top 5 for now
    #     print(f"{article['source']} | {article['title']} | {article['timestamp']}")
    #     print(article['summary'])
    #     print(article['url'])
    #     print("---")