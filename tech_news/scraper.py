import requests
import time
from parsel import Selector
import re
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(
            url, timeout=3, headers={"user-agent": "Fake user-agent"}
        )
        if (response.status_code != 200):
            return None
        else:
            return response.text
    except requests.Timeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    news_links = selector.css(".entry-title a::attr(href)").getall()
    return news_links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page_link = selector.css(".next::attr(href)").get()
    return next_page_link


# Requisito 4
def remove_html(text):
    pattern = re.compile("<.*?>")
    return re.sub(pattern, "", text)


def scrape_news(html_content):
    news_infos = {}
    selector = Selector(text=html_content)

    news_infos["url"] = (
        selector.css("link[rel='canonical']::attr(href)").get()
    )
    news_infos["title"] = (
        selector.css(".entry-title::text").get().strip()
    )
    news_infos["timestamp"] = (
        selector.css(".meta-date::text").get()
    )
    news_infos["writer"] = (
        selector.css(".author a::text").get()
    )
    news_infos["comments_count"] = (
        len(selector.css("comment-list li").getall()) or 0
    )
    news_infos["summary"] = (
        remove_html(selector.css(".entry-content p").get()).strip()
    )
    news_infos["tags"] = (
        selector.css(".post-tags li a::text").getall()
    )
    news_infos["category"] = (
        selector.css(".meta-category .label::text").get()
    )

    if not news_infos["title"] or not news_infos["summary"]:
        return None
    return news_infos


# Requisito 5
def get_tech_news(amount):
    html_content = fetch("https://blog.betrybe.com/")
    url_list = []

    while len(url_list) < amount:
        url_list += scrape_updates(html_content)

        if len(url_list) < amount:
            html_content = fetch(scrape_next_page_link(html_content))

    news_list = [
        scrape_news(fetch(url))
        for url in url_list[0:amount]
    ]

    create_news(news_list)

    return news_list
