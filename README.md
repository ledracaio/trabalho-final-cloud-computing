# Projeto Final de Cloud Computing: API de Cursos Online com DevOps

Este repositório contém o projeto final da disciplina de Cloud Computing, que consiste em uma API REST para gerenciamento de cursos online, implementada com um fluxo DevOps utilizando GitHub Actions.

## Aluno

- **Nome**: Caio Augusto Ledra
- **Matrícula**: 1033490
- **Turma**: T28

## Tema Individual

**Plataforma de Cursos Online**

## Estrutura do Repositório

```
.github/
└── workflows/
    └── ci.yml
api/
├── data/
│   └── cursos.json
├── test/
│   └── test_api.py
└── app.py
README.md
```

## Requisitos

Para executar a API e os testes localmente, você precisará ter o Python 3 e o `pip` instalados. É altamente recomendável usar um ambiente virtual.

## Instalação e Execução Local

Siga os passos abaixo para configurar e executar a API em seu ambiente local:

1.  **Clone o repositório**:
    ```bash
    git clone <url-do-seu-repositorio>
    cd "Final Project Caio Ledra"
    ```

2.  **Crie e ative um ambiente virtual** (opcional, mas recomendado):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Linux/macOS
    # venv\Scripts\activate  # No Windows
    ```

3.  **Instale as dependências**:
    ```bash
    pip install Flask
    pip install requests # Para testes, se necessário
    ```

4.  **Execute a API**:
    ```bash
    cd api
    python app.py
    ```
    A API estará disponível em `http://127.0.0.1:5001`.

## Endpoints da API

-   **GET /status**
    -   Retorna o status da API, nome e versão.
    -   Exemplo de resposta:
        ```json
        {
            "api_name": "Online Courses API",
            "status": "running",
            "version": "1.0.0"
        }
        ```

-   **GET /cursos**
    -   Retorna uma lista de todos os cursos disponíveis.
    -   Exemplo de resposta (parcial):
        ```json
        [
            {
                "id": 1,
                "title": "Introdução à Programação com Python",
                "category": "Programação",
                "instructor": "Dr. Ana Silva",
                "duration_hours": 40,
                "level": "Iniciante",
                "price": 299.90,
                "description": "..."
            }
        ]
        ```

-   **GET /cursos/{id}**
    -   Retorna os detalhes de um curso específico pelo seu ID.
    -   Exemplo de resposta para `/cursos/1`:
        ```json
        {
            "id": 1,
            "title": "Introdução à Programação com Python",
            "category": "Programação",
            "instructor": "Dr. Ana Silva",
            "duration_hours": 40,
            "level": "Iniciante",
            "price": 299.90,
            "description": "..."
        }
        ```
    -   Se o curso não for encontrado, retorna `404 Not Found`.

## Execução dos Testes Unitários

Para executar os testes unitários, navegue até o diretório `api` e execute:

```bash
cd api
python -m unittest test/test_api.py
```

## Fluxo de Integração Contínua (CI) com GitHub Actions

Este projeto utiliza GitHub Actions para automatizar o processo de integração contínua. O workflow está configurado para ser executado a cada `push` no repositório.

O arquivo de workflow (`.github/workflows/ci.yml`) define os seguintes passos:

1.  **Checkout do código**.
2.  **Configuração do ambiente Python**.
3.  **Instalação de dependências**.
4.  **Execução dos testes unitários**.
5.  **Análise de código com Flake8** (etapa adicional).

Qualquer `push` que falhe nos testes ou na análise de código resultará em uma falha no pipeline de CI, indicando a necessidade de revisão do código.

## Docker (Execução com Container)

Para executar a API usando Docker, siga os passos:

1.  **Construa a imagem Docker** (no diretório raiz do projeto):
    ```bash
    docker build -t cursos-api .
    ```

2.  **Execute o container Docker**:
    ```bash
    docker run -p 5001:5001 cursos-api
    ```
    A API estará disponível em `http://localhost:5001`.

