from tech_news.database import find_news
from operator import itemgetter


# Requisito 10
def top_5_news():
    news_comments = []
    for new in find_news():
        news_comments.append(new)
    sort_title = sorted(news_comments, key=itemgetter("title"))
    sort_comments = sorted(
        sort_title, key=itemgetter("comments_count"), reverse=True
    )
    return [(new["title"], new["url"]) for new in sort_comments][:5]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
