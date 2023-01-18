import sys
from tech_news.analyzer.ratings import top_5_categories, top_5_news
from tech_news.analyzer.search_engine import (
    search_by_category,
    search_by_date,
    search_by_tag,
    search_by_title,
)
from tech_news.scraper import get_tech_news


options_array = [
    'Selecione uma das opções a seguir:\n',
    ' 0 - Popular o banco com notícias;\n',
    ' 1 - Buscar notícias por título;\n',
    ' 2 - Buscar notícias por data;\n',
    ' 3 - Buscar notícias por tag;\n',
    ' 4 - Buscar notícias por categoria;\n',
    ' 5 - Listar top 5 notícias;\n',
    ' 6 - Listar top 5 categorias;\n',
    ' 7 - Sair.\n',
]


def zero_to_three(option):
    if option == "0":
        get_tech_news(int(input("Digite quantas notícias serão buscadas:")))
    elif option == "1":
        search_by_title(input("Digite o título:"))
    elif option == "2":
        search_by_date(input("Digite a data no formato aaaa-mm-dd:"))
    else:
        search_by_tag(input("Digite a tag:"))


def four_to_six(option):
    if option == "4":
        search_by_category(input("Digite a categoria:"))
    elif option == "5":
        print(top_5_news())
    else:
        print(top_5_categories())


# Requisito 12
def analyzer_menu():
    option = input("".join(options_array))
    if option <= "3":
        zero_to_three(option)
    elif option <= "6":
        four_to_six(option)
    elif option == "7":
        sys.stdout.write("Encerrando script\n")
    else:
        sys.stderr.write("Opção inválida\n")
