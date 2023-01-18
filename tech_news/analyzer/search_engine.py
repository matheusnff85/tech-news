from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    search = search_news(query)
    return [
        (news["title"], news["url"])
        for news in search
    ]


# Requisito 7
def search_by_date(date):
    try:
        news = []
        news_by_date = datetime.fromisoformat(date).strftime("%d/%m/%Y")
        query = {"timestamp": {"$eq": news_by_date}}
        for new in search_news(query):
            news.append((new["title"], new["url"]))
        return news
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    news = []
    query = {"tags": {"$regex": tag, "$options": "i"}}
    for new in search_news(query):
        news.append((new["title"], new["url"]))
    return news


# Requisito 9
def search_by_category(category):
    news = []
    query = {"category": {"$regex": category, "$options": "i"}}
    for new in search_news(query):
        news.append((new["title"], new["url"]))
    return news
