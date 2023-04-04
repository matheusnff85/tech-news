# Tech News

- O objetivo desse empreendimento é extrair informações de um portal que apresenta informações atualizadas sobre tecnologia. A fim de alcançar esse propósito, foi implementada a técnica de raspagem de dados, que consiste em capturar informações diretamente de plataformas online. Essa ação é efetuada por meio de scripts e softwares que coletam e filtram os dados necessários. Ao término da raspagem, as informações são arquivadas em um banco de dados.

- Com os dados coletados organizados e armazenados, o sistema possibilita a busca por assunto, data, categorias e etiquetas de notícias. Além disso, um menu interativo foi desenvolvido para facilitar o processo de utilização por parte do usuário.

---

# Tecnologias utilizadas :books:

- Python, MongoDB.

---

# Como Utilizar a aplicação

  1. Clone o repositório

  - Use o comando: `git clone git@github.com:matheusnff85/tech-news.git`
  - Entre na pasta do repositório que você acabou de clonar:
    - `cd tech-news`

  2. Crie o ambiente virtual para o projeto

  - `python3 -m venv .venv && source .venv/bin/activate`
  
  3. Instale as dependências

  - `python3 -m pip install -r dev-requirements.txt`

  4. Inicie o serviço do MongoDB iniciando o container docker com o comando:

  - `docker-compose up -d mongodb`

  5. Após tudo feito, utilize no terminal o comando abaixo para interagir com a aplicação:

  - `python3 -m tech_news.menu`
    - Caso seja a primeira vez utilizando a aplicação, utilize a opção **0** para popular o banco de dados com as informações obtidas.

---

- Desenvolvido por [Matheus Marinho](https://www.linkedin.com/in/matheus-marinhodsp/).