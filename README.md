# TodoList API

Este projeto é uma API RESTful para gerenciamento de tarefas (TodoList), construída com Django e Django REST Framework.

## Pré-requisitos

Para rodar o projeto, você precisa ter instalado:

- Docker
- Docker Compose

## Como executar o projeto

1. Primeiro, clone o repositório para o seu ambiente local usando o seguinte comando:

    ```bash
    git clone https://github.com/volneyrock/todolist.git
    cd TodoList
    ```

2. Em seguida, crie e inicie os serviços usando o Docker Compose:

    ```bash
    make build
    make run
    ```

3. Agora, realize as migrações para o banco de dados:

    ```bash
    make migrate
    ```

4. Opcionalmente, você pode carregar os dados iniciais para o banco de dados usando o comando:

    ```bash
    make fixtures
    ```

5. Pronto! A aplicação deve estar rodando em [http://localhost:8000](http://localhost:8000).

## Comandos adicionais

- Para parar a aplicação:

    ```bash
    make stop
    ```

- Para remover os serviços:

    ```bash
    make down
    ```

- Para executar os testes:

    ```bash
    make test
    ```

- Para acessar o shell do Django:

    ```bash
    make shell
    ```

## Documentação da API

A documentação da API está disponível no seguinte endereço: [http://localhost:8000/swagger](http://localhost:8000/swagger)

Você também pode acessar a interface do Django REST Framework em: [http://localhost:8000/api/v1/tasks/](http://localhost:8000/api/v1/tasks/)


## Uso alternativo de comandos

Se preferir, você pode utilizar diretamente os comandos do Docker Compose em vez de usar o `Makefile`. Aqui estão os comandos equivalentes:

- Para construir e iniciar os serviços:

    ```bash
    docker compose build
    docker compose up -d
    ```

- Para realizar as migrações:

    ```bash
    docker compose exec todolist python manage.py makemigrations
    docker compose exec todolist python manage.py migrate
    ```

- Para carregar os dados iniciais:

    ```bash
    docker compose exec todolist python manage.py flush
    docker compose exec todolist python manage.py loaddata fixtures.json
    ```

- Para parar a aplicação:

    ```bash
    docker compose stop
    ```

- Para remover os serviços:

    ```bash
    docker compose down
    ```

- Para executar os testes:

    ```bash
    docker compose exec todolist python manage.py test
    ```

- Para acessar o shell do Django:

    ```bash
    docker compose exec todolist python manage.py shell
    ```

Os comandos do `Makefile` foram adicionados apenas para facilitar o uso dos comandos do Docker Compose. Você pode consultar o arquivo `Makefile` para mais detalhes.