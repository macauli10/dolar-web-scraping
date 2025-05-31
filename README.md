# 💵 Dólar Web Scraping com SQLite + Docker

Este projeto realiza a coleta (scraping) da cotação atual do **dólar (USD/BRL)** a partir de uma API pública e salva os dados em um banco de dados **SQLite**, utilizando **Python**. Toda a aplicação é containerizada com **Docker** e orquestrada via **Docker Compose**.

---

## 🚀 Funcionalidades

- Coleta da cotação atual do dólar via API da [AwesomeAPI](https://docs.awesomeapi.com.br/api-de-moedas).
- Armazenamento estruturado em banco de dados SQLite (`cotacoes.db`).
- Script automatizado com Docker para rodar em qualquer ambiente.

---

## 🧰 Tecnologias utilizadas

- **Python 3.10**
- **SQLite** (banco de dados leve e embutido)
- **Requests** (para realizar o scraping via API)
- **Docker** e **Docker Compose**

---

## 📁 Estrutura de pastas

dolar-web-scraping/
│
├── scripts/
│ └── scraping.py # Script de scraping + persistência
│
├── cotacoes.db # Banco de dados gerado (após execução)
├── Dockerfile # Imagem do container
├── docker-compose.yaml # Orquestração com Docker Compose
├── requirements.txt # Dependências Python
└── README.md # Este arquivo

yaml
Copy
Edit

---

## ⚙️ Como executar

> Pré-requisitos: Docker e Docker Compose instalados

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/dolar-web-scraping.git
cd dolar-web-scraping
Rode o projeto com Docker Compose:

bash
Copy
Edit
docker-compose up --build
Após a execução, o arquivo cotacoes.db será criado na raiz do projeto, contendo os dados coletados.

🗃️ Estrutura da Tabela
A tabela cotacao_dolar possui os seguintes campos:

id: identificador único (autoincremento)

moeda: nome da moeda (Dólar)

codigo: código da moeda (USD)

cotacao: valor atual do dólar

alta: valor máximo no dia

baixa: valor mínimo no dia

data: data da cotação

timestamp_coleta: data/hora em que a coleta foi realizada

🧠 Objetivo do projeto
Este projeto é uma aplicação simples mas prática, com foco em:

Demonstrar coleta automatizada de dados (web scraping com API)

Aplicar armazenamento local com banco de dados relacional (SQLite)

Garantir portabilidade com Docker, podendo ser executado em qualquer máquina com um único comando.

