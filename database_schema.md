# Esquema do Banco de Dados para Bendito Docce

Este documento detalha o esquema proposto para o banco de dados MySQL da doceria Bendito Docce. O objetivo é fornecer uma estrutura robusta e escalável para armazenar informações sobre produtos, categorias e, futuramente, pedidos e usuários. A integração com o MySQL Workbench 8.0 CE será abordada nas próximas seções.

## 1. Visão Geral do Modelo de Dados

O modelo de dados inicial será focado na gestão de produtos, que é a funcionalidade central do site atualmente. Serão criadas tabelas para armazenar os produtos e suas respectivas categorias, permitindo uma organização eficiente e fácil consulta.

### Entidades Principais:

- **Produtos**: Representa os itens vendidos pela doceria, como brigadeiros gourmet e tradicionais.
- **Categorias**: Define os tipos de produtos, como 'tradicional', 'gourmet' e 'novo'.

## 2. Detalhamento das Tabelas

### Tabela: `products`

Esta tabela armazenará todos os detalhes dos produtos disponíveis na doceria. Cada linha representará um produto único.

| Coluna           | Tipo de Dados     | Restrições           | Descrição                                        |
|------------------|-------------------|----------------------|--------------------------------------------------|
| `product_id`     | `INT`             | `PRIMARY KEY`, `AUTO_INCREMENT` | Identificador único do produto.                  |
| `name`           | `VARCHAR(255)`    | `NOT NULL`           | Nome do produto (ex: 


`Brigadeiro Ferrero Rocher`).         |
| `description`    | `TEXT`            | `NULL`               | Descrição detalhada do produto.                  |
| `price`          | `DECIMAL(10, 2)`  | `NOT NULL`           | Preço unitário do produto.                       |
| `price_per_hundred` | `DECIMAL(10, 2)`  | `NULL`               | Preço do produto ao comprar 100 unidades (opcional, para descontos). |
| `image_url`      | `VARCHAR(255)`    | `NULL`               | URL ou caminho da imagem do produto.             |
| `category_id`    | `INT`             | `NOT NULL`, `FOREIGN KEY` | Chave estrangeira para a tabela `categories`. |
| `is_new`         | `BOOLEAN`         | `DEFAULT FALSE`      | Indica se o produto é uma novidade.              |
| `created_at`     | `TIMESTAMP`       | `DEFAULT CURRENT_TIMESTAMP` | Data e hora de criação do registro.      |
| `updated_at`     | `TIMESTAMP`       | `DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP` | Data e hora da última atualização do registro. |

### Tabela: `categories`

Esta tabela armazenará as categorias dos produtos, permitindo uma categorização flexível e fácil de gerenciar.

| Coluna           | Tipo de Dados     | Restrições           | Descrição                                        |
|------------------|-------------------|----------------------|--------------------------------------------------|
| `category_id`    | `INT`             | `PRIMARY KEY`, `AUTO_INCREMENT` | Identificador único da categoria.                |
| `name`           | `VARCHAR(100)`    | `NOT NULL`, `UNIQUE` | Nome da categoria (ex: `Gourmet`, `Tradicional`, `Novo`). |
| `description`    | `TEXT`            | `NULL`               | Descrição da categoria.                          |

## 3. Relacionamentos

O relacionamento entre as tabelas `products` e `categories` é de **muitos para um** (`Many-to-One`). Isso significa que muitos produtos podem pertencer a uma única categoria, mas um produto pertence a apenas uma categoria.

- A coluna `category_id` na tabela `products` é uma chave estrangeira que referencia a coluna `category_id` na tabela `categories`.

## 4. Considerações Futuras

Este esquema pode ser expandido para incluir funcionalidades adicionais, como:

- **Tabela `users`**: Para gerenciar usuários e administradores, com papéis e permissões.
- **Tabela `orders`**: Para registrar pedidos, incluindo detalhes do cliente, status do pedido e data.
- **Tabela `order_items`**: Para detalhar os produtos incluídos em cada pedido, com quantidade e preço no momento da compra.
- **Tabela `reviews`**: Para armazenar avaliações e comentários dos clientes sobre os produtos.

## 5. Próximos Passos

Com este esquema definido, o próximo passo será gerar os scripts SQL para criar essas tabelas no MySQL e fornecer instruções sobre como usar o MySQL Workbench para gerenciar o banco de dados. Isso permitirá que o site da Bendito Docce utilize um sistema de persistência de dados mais robusto e escalável, substituindo o armazenamento local atual (localStorage).

