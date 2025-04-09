# API de Gestão de Servidores Públicos

Este projeto é parte de um teste prático e implementa uma API RESTful com autenticação JWT, gerenciamento de servidores (efetivos e temporários), unidades, lotações e upload de imagens com MinIO.

## 👤 Dados de Inscrição

- **Nome:** Henrique Alves Monti
- **E-mail:** henrique.amonti@gmail.com
- **Data de entrega:** 09/04/2025

---

## 🚀 Tecnologias utilizadas

- FastAPI
- PostgreSQL (em container)
- MinIO (S3-compatible, em container)
- SQLAlchemy
- JWT (autenticação)
- Docker & Docker Compose

---

## ⚙️ Como executar o projeto

1. Clone o repositório:

``git clone https://github.com/HenriqueMonti/servidores-api.git``

2. Suba os containers com Docker Compose:

``docker-compose up --build``

3. Acesse a documentação interativa:

``http://localhost:8000/docs``
(Ou, se quiser a versão redoc: ``http://localhost:8000/redoc``)

---

## 📦 Endpoints principais

- Autenticação:
  - `POST /auth/register` - Criação de usuário
  - `POST /auth/login` - Geração de token (expira em 5 min)
  - `GET /auth/renew` - Renovação do token

- CRUDs:
  - `POST /unidades/`
  - `POST /efetivos/`
  - `POST /temporarios/`
  - `POST /lotacoes/`

  Todos com suporte a `GET`, `PUT`, `DELETE` e paginação por `skip` e `limit`.

- Upload de fotos:
  - `POST /upload/foto` - Multipart/form-data (1 ou mais imagens)

- Consultas especiais:
  - `GET /consultas/efetivos/unidade/{unid_id}` - Nome, idade, unidade, fotografia
  - `GET /consultas/endereco?nome=parte_do_nome` - Endereço funcional da unidade de lotação

---

## ☁️ MinIO (S3)

- Console de administração: `http://localhost:9001`
- Credenciais:
  - Usuário: `minioadmin`
  - Senha: `minioadmin`
- As imagens são acessíveis apenas via **links temporários (5 minutos)**.

---

## 🐘 Banco de dados

- Acesso ao PostgreSQL:
  - Host: `localhost`
  - Porta: `5432`
  - Usuário: `user`
  - Senha: `password`
  - Banco: `servidores`

---

## 📄 Observações

- A API exige autenticação (Bearer Token) para todos os endpoints, exceto registro e login.
- Todos os scripts e dependências estão incluídos.
- A estrutura está pronta para expansão com testes e validações adicionais.

---

## ✅ Para corrigir/testar

- Acesse o Swagger UI: `http://localhost:8000/docs`
- Faça login e copie o token JWT
- Clique em **Authorize** e use `Bearer <seu-token>`
- Teste os endpoints protegidos

---

