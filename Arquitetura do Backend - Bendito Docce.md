# Arquitetura do Backend - Bendito Docce

## 1. Visão Geral da Arquitetura

O backend para o site da Bendito Docce será desenvolvido utilizando Flask, um framework web leve e flexível para Python. Esta escolha foi feita considerando a simplicidade de implementação, a robustez do framework e a facilidade de integração com bancos de dados MySQL. O backend seguirá uma arquitetura RESTful, fornecendo endpoints claros e bem definidos para operações CRUD (Create, Read, Update, Delete) em produtos e categorias.

A arquitetura será composta pelos seguintes componentes principais:

- **Flask Application**: O núcleo da aplicação que gerenciará as rotas e requisições HTTP.
- **Database Layer**: Camada de acesso aos dados utilizando SQLAlchemy como ORM (Object-Relational Mapping).
- **API Endpoints**: Endpoints RESTful para gerenciar produtos e categorias.
- **CORS Support**: Suporte para requisições cross-origin, permitindo que o frontend se comunique com o backend.
- **Static File Serving**: Capacidade de servir os arquivos estáticos do frontend (HTML, CSS, JS, imagens).

## 2. Estrutura de Diretórios

A estrutura de diretórios do backend seguirá as melhores práticas do Flask:

```
bendito-docce-backend/
├── app.py                 # Arquivo principal da aplicação Flask
├── config.py              # Configurações da aplicação
├── models.py              # Modelos de dados (SQLAlchemy)
├── routes/
│   ├── __init__.py
│   ├── products.py        # Rotas para produtos
│   └── categories.py      # Rotas para categorias
├── static/                # Arquivos estáticos do frontend
│   ├── index.html
│   ├── style.css
│   ├── script.js
│   └── images/
├── requirements.txt       # Dependências Python
└── README.md             # Documentação do backend
```

## 3. Definição das APIs

### 3.1 Endpoints para Produtos

#### GET /api/products
- **Descrição**: Retorna todos os produtos cadastrados
- **Método**: GET
- **Resposta**: Lista de produtos em formato JSON
- **Exemplo de resposta**:
```json
[
  {
    "product_id": 1,
    "name": "Brigadeiro Ferrero Rocher",
    "description": "Brigadeiro gourmet com sabor Ferrero Rocher",
    "price": 5.00,
    "price_per_hundred": 425.00,
    "image_url": "img1.jpeg",
    "category_id": 2,
    "category_name": "gourmet",
    "is_new": false,
    "created_at": "2025-01-25T10:00:00",
    "updated_at": "2025-01-25T10:00:00"
  }
]
```

#### GET /api/products/{id}
- **Descrição**: Retorna um produto específico por ID
- **Método**: GET
- **Parâmetros**: id (integer) - ID do produto
- **Resposta**: Dados do produto em formato JSON

#### POST /api/products
- **Descrição**: Cria um novo produto
- **Método**: POST
- **Body**: Dados do produto em JSON
- **Exemplo de requisição**:
```json
{
  "name": "Brigadeiro Pistache",
  "description": "Brigadeiro gourmet com pistache",
  "price": 5.50,
  "image_url": "img_pistache.jpeg",
  "category_id": 2,
  "is_new": true
}
```

#### PUT /api/products/{id}
- **Descrição**: Atualiza um produto existente
- **Método**: PUT
- **Parâmetros**: id (integer) - ID do produto
- **Body**: Dados atualizados do produto em JSON

#### DELETE /api/products/{id}
- **Descrição**: Remove um produto
- **Método**: DELETE
- **Parâmetros**: id (integer) - ID do produto
- **Resposta**: Confirmação da exclusão

### 3.2 Endpoints para Categorias

#### GET /api/categories
- **Descrição**: Retorna todas as categorias
- **Método**: GET
- **Resposta**: Lista de categorias em formato JSON

#### GET /api/categories/{id}
- **Descrição**: Retorna uma categoria específica
- **Método**: GET
- **Parâmetros**: id (integer) - ID da categoria

#### POST /api/categories
- **Descrição**: Cria uma nova categoria
- **Método**: POST
- **Body**: Dados da categoria em JSON

#### PUT /api/categories/{id}
- **Descrição**: Atualiza uma categoria existente
- **Método**: PUT
- **Parâmetros**: id (integer) - ID da categoria

#### DELETE /api/categories/{id}
- **Descrição**: Remove uma categoria
- **Método**: DELETE
- **Parâmetros**: id (integer) - ID da categoria

### 3.3 Endpoints Especiais

#### GET /api/products/category/{category_name}
- **Descrição**: Retorna produtos de uma categoria específica
- **Método**: GET
- **Parâmetros**: category_name (string) - Nome da categoria (tradicional, gourmet, novo)

#### GET /api/products/new
- **Descrição**: Retorna apenas produtos marcados como novidade
- **Método**: GET

## 4. Tecnologias e Dependências

### 4.1 Dependências Principais
- **Flask**: Framework web principal
- **Flask-SQLAlchemy**: ORM para integração com banco de dados
- **Flask-CORS**: Suporte para requisições cross-origin
- **PyMySQL**: Driver para conexão com MySQL
- **Flask-Migrate**: Gerenciamento de migrações de banco de dados

### 4.2 Configuração do Banco de Dados
- **Host**: localhost (configurável)
- **Porta**: 3306 (padrão MySQL)
- **Database**: bendito_docce_db
- **Charset**: utf8mb4

## 5. Segurança e Validação

### 5.1 Validação de Dados
- Validação de tipos de dados nas requisições
- Verificação de campos obrigatórios
- Sanitização de entradas para prevenir SQL injection

### 5.2 Tratamento de Erros
- Respostas padronizadas para erros HTTP
- Logging de erros para debugging
- Mensagens de erro amigáveis para o frontend

## 6. Próximos Passos

Com a arquitetura definida, os próximos passos incluem:
1. Configuração do ambiente de desenvolvimento
2. Implementação dos modelos de dados
3. Desenvolvimento dos endpoints da API
4. Testes e validação
5. Documentação completa

Esta arquitetura fornece uma base sólida e escalável para o backend da Bendito Docce, permitindo futuras expansões como autenticação de usuários, sistema de pedidos e relatórios avançados.

