from tech_news.database import find_news
from operator import itemgetter
from collections import Counter


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
    news_categories = []
    for new in find_news():
        news_categories.append(new["category"])
    count_categories = []
    for name, _ in Counter(sorted(news_categories)).most_common(5):
        count_categories.append(name)
    return count_categories
