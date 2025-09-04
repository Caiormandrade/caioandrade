# Documentação Completa do Banco de Dados - Bendito Docce

## 1. Introdução

Esta documentação fornece uma visão abrangente do banco de dados MySQL projetado para o site da Bendito Docce. O objetivo é detalhar a estrutura, os relacionamentos e as funcionalidades do banco de dados, além de fornecer um guia completo para sua integração com o MySQL Workbench 8.0 CE.

## 2. Esquema do Banco de Dados

O esquema do banco de dados foi projetado para ser simples, mas escalável, atendendo às necessidades atuais do site e permitindo futuras expansões.

### 2.1 Tabela `categories`

- **Descrição**: Armazena as categorias dos produtos (ex: Gourmet, Tradicional).
- **Colunas Principais**:
  - `category_id` (INT, PK, AI): Identificador único.
  - `name` (VARCHAR(100), NOT NULL, UNIQUE): Nome da categoria.

### 2.2 Tabela `products`

- **Descrição**: Armazena os detalhes de cada produto.
- **Colunas Principais**:
  - `product_id` (INT, PK, AI): Identificador único.
  - `name` (VARCHAR(255), NOT NULL): Nome do produto.
  - `price` (DECIMAL(10, 2), NOT NULL): Preço unitário.
  - `category_id` (INT, FK): Chave estrangeira para a tabela `categories`.

## 3. Scripts SQL

Dois scripts SQL foram criados para facilitar a configuração do banco de dados:

- **`create_tables.sql`**: Cria o esquema e as tabelas `categories` e `products`.
- **`insert_sample_data.sql`**: Popula as tabelas com dados de exemplo para testes.

## 4. Integração com MySQL Workbench 8.0 CE

O guia detalhado `mysql_workbench_instructions.md` fornece um passo a passo completo para:

- Instalar o MySQL Server e o MySQL Workbench.
- Configurar uma nova conexão com o banco de dados.
- Importar o esquema e os dados usando os scripts SQL fornecidos.
- Navegar, visualizar e gerenciar os dados no Workbench.

## 5. Próximos Passos e Evolução

Com o banco de dados implementado, o próximo passo é integrar o site da Bendito Docce com este banco de dados. Isso exigirá o desenvolvimento de um backend (por exemplo, em Node.js, PHP ou Python) que se comunicará com o banco de dados e fornecerá os dados para o frontend do site. Esta integração permitirá funcionalidades mais avançadas, como:

- Gerenciamento de usuários e autenticação segura.
- Histórico de pedidos e carrinhos de compras persistentes.
- Sistema de avaliações e comentários de produtos.
- Relatórios de vendas e análise de dados.

Esta documentação serve como um ponto de partida para o desenvolvimento e a manutenção contínua do banco de dados da Bendito Docce.

