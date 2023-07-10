# Flask MySQL Backend

Este é um projeto de backend simples usando Flask com banco de dados MySQL. O projeto possui endpoints para recuperar todos os produtos, inserir um novo produto e excluir um produto. Siga as instruções abaixo para rodar o projeto e testá-lo.

## Pré-requisitos

Antes de iniciar, certifique-se de ter os seguintes requisitos instalados em seu ambiente de desenvolvimento:

- Python 3.7 ou superior instalado
- MySQL Server instalado

## Instalação

1. Clone este repositório para o seu ambiente de desenvolvimento local.

2. Certifique-se de ter o MySQL Server instalado no seu sistema. Caso não tenha, siga as etapas apropriadas para instalar o MySQL para o seu sistema operacional.

3. Crie um ambiente virtual (venv) para o projeto. No terminal, navegue até a pasta raiz do projeto e execute o seguinte comando:

   ```shell
   python -m venv venv
   ```

4. Ative o ambiente virtual:

* No Windows:

   ```shell
   venv\Scripts\activate
   ```
* No macOS/Linux:

   ```shell
   source venv/bin/activate
   ```

5. Instale as dependências do projeto executando o seguinte comando:

   ```shell
   pip install -r requirements.txt
   ```

6. Crie um arquivo .env na pasta raiz do projeto e adicione as seguintes linhas:
   ```
   DB_HOST=localhost
   DB_DATABASE=products_db
   DB_USER=<seu usuário do db>
   DB_PASSWORD=<sua senha do db>
   ```

## Configuração do Banco de Dados

1. No terminal, certifique-se de estar dentro do ambiente virtual (venv) e navegue até a pasta raiz do projeto.

2. Execute o seguinte comando para configurar o banco de dados e criar a tabela de produtos com dados iniciais:

   ```shell
   python setup_database.py
   ```

   Este comando criará o banco de dados (se ainda não existir), criará a tabela de produtos e inserirá alguns dados iniciais.

   **Observação**: Execute este comando apenas uma vez, pois ele configurará o banco de dados e adicionará os dados iniciais necessários.

## Executando o Projeto

1. No terminal, certifique-se de estar dentro do ambiente virtual (venv) e navegue até a pasta raiz do projeto.

2. Execute o seguinte comando para iniciar o servidor Flask:

   ```shell
   python app.py
   ```

   O servidor Flask será iniciado e estará pronto para receber solicitações.