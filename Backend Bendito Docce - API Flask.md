# Backend Bendito Docce - API Flask

Este é o backend completo para o site da Bendito Docce, desenvolvido em Flask com integração ao banco de dados MySQL. O backend fornece uma API RESTful para gerenciar produtos e categorias, além de servir os arquivos estáticos do frontend.

## 🚀 Funcionalidades

### ✅ API RESTful Completa
- **Produtos**: CRUD completo (Create, Read, Update, Delete)
- **Categorias**: Gerenciamento de categorias de produtos
- **Filtros**: Busca por categoria e produtos novos
- **Validação**: Validação de dados e tratamento de erros

### ✅ Integração com MySQL
- **Modelos SQLAlchemy**: Estrutura de dados robusta
- **Relacionamentos**: Foreign keys entre produtos e categorias
- **Migrações**: Suporte a Flask-Migrate para evolução do schema

### ✅ Frontend Integrado
- **Arquivos Estáticos**: Serve o site completo da Bendito Docce
- **CORS**: Configurado para permitir requisições cross-origin
- **SPA Support**: Roteamento para Single Page Applications

## 📁 Estrutura do Projeto

```
bendito-docce-backend/
├── src/
│   ├── models/
│   │   ├── category.py      # Modelo de categorias
│   │   └── product.py       # Modelo de produtos
│   ├── routes/
│   │   ├── categories.py    # Endpoints de categorias
│   │   ├── products.py      # Endpoints de produtos
│   │   └── init_data.py     # Inicialização de dados
│   ├── static/              # Arquivos do frontend
│   │   ├── index.html
│   │   ├── style.css
│   │   ├── script.js
│   │   └── *.jpeg          # Imagens dos produtos
│   ├── config.py           # Configurações da aplicação
│   └── main.py             # Arquivo principal
├── venv/                   # Ambiente virtual Python
├── requirements.txt        # Dependências
└── README.md              # Esta documentação
```

## 🛠️ Configuração e Instalação

### Pré-requisitos
- Python 3.8+
- MySQL Server 8.0+
- MySQL Workbench (opcional, para gerenciamento visual)

### 1. Configuração do Banco de Dados
Antes de executar o backend, configure o banco de dados MySQL:

1. **Instale o MySQL Server** em sua máquina
2. **Crie o banco de dados**:
   ```sql
   CREATE DATABASE bendito_docce_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```
3. **Configure as credenciais** no arquivo `src/config.py` ou via variáveis de ambiente

### 2. Instalação do Backend

1. **Clone/extraia o projeto** para sua máquina
2. **Ative o ambiente virtual**:
   ```bash
   cd bendito-docce-backend
   source venv/bin/activate  # Linux/Mac
   # ou
   venv\Scripts\activate     # Windows
   ```
3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

### 3. Configuração de Variáveis de Ambiente (Opcional)
Você pode configurar as credenciais do banco via variáveis de ambiente:

```bash
export MYSQL_HOST=localhost
export MYSQL_PORT=3306
export MYSQL_USER=root
export MYSQL_PASSWORD=sua_senha
export MYSQL_DATABASE=bendito_docce_db
```

### 4. Executar o Backend

```bash
python src/main.py
```

O servidor estará disponível em: `http://localhost:5000`

## 📚 Documentação da API

### Endpoints de Produtos

#### GET /api/products
Retorna todos os produtos cadastrados.

**Resposta:**
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
Retorna um produto específico por ID.

#### POST /api/products
Cria um novo produto.

**Body:**
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
Atualiza um produto existente.

#### DELETE /api/products/{id}
Remove um produto.

#### GET /api/products/category/{category_name}
Retorna produtos de uma categoria específica (tradicional, gourmet, novo).

#### GET /api/products/new
Retorna apenas produtos marcados como novidade.

### Endpoints de Categorias

#### GET /api/categories
Retorna todas as categorias.

#### GET /api/categories/{id}
Retorna uma categoria específica por ID.

#### POST /api/categories
Cria uma nova categoria.

#### PUT /api/categories/{id}
Atualiza uma categoria existente.

#### DELETE /api/categories/{id}
Remove uma categoria (apenas se não houver produtos associados).

#### GET /api/categories/name/{category_name}
Retorna uma categoria específica por nome.

### Endpoint de Inicialização

#### POST /api/init-data
Inicializa o banco de dados com dados de exemplo (categorias e produtos padrão).

## 🔧 Configuração Avançada

### Configuração do Banco de Dados
Edite o arquivo `src/config.py` para ajustar as configurações:

```python
class Config:
    MYSQL_HOST = 'localhost'
    MYSQL_PORT = 3306
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'sua_senha'
    MYSQL_DATABASE = 'bendito_docce_db'
```

### Configuração de CORS
O CORS está configurado para aceitar requisições de qualquer origem. Para produção, considere restringir:

```python
CORS(app, origins=["http://localhost:3000", "https://seudominio.com"])
```

## 🚀 Deploy e Produção

### Preparação para Deploy
1. **Atualize as dependências**:
   ```bash
   pip freeze > requirements.txt
   ```

2. **Configure variáveis de ambiente** para produção

3. **Use um servidor WSGI** como Gunicorn:
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 src.main:app
   ```

### Considerações de Segurança
- Configure `SECRET_KEY` com valor seguro
- Use HTTPS em produção
- Configure firewall para proteger o banco de dados
- Implemente autenticação para endpoints administrativos

## 🐛 Solução de Problemas

### Erro de Conexão com MySQL
```
(pymysql.err.OperationalError) (2003, "Can't connect to MySQL server")
```

**Soluções:**
1. Verifique se o MySQL Server está rodando
2. Confirme as credenciais no `config.py`
3. Teste a conexão manualmente:
   ```bash
   mysql -h localhost -u root -p
   ```

### Erro de Importação de Módulos
Certifique-se de que o ambiente virtual está ativado e as dependências instaladas.

### Problemas com CORS
Se o frontend não conseguir acessar a API, verifique a configuração do CORS no `main.py`.

## 📞 Suporte

Para dúvidas ou problemas:
1. Verifique esta documentação
2. Consulte os logs do Flask para erros específicos
3. Teste os endpoints individualmente usando ferramentas como Postman ou curl

## 🔄 Próximas Funcionalidades

Funcionalidades que podem ser implementadas no futuro:
- Sistema de autenticação JWT
- Upload de imagens para produtos
- Sistema de pedidos e carrinho persistente
- Relatórios e analytics
- Sistema de avaliações de produtos
- Integração com gateways de pagamento

