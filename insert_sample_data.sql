-- SQL Script para Inserção de Dados de Exemplo - Bendito Docce
-- Versão: 1.0
-- Data: 25 de Julho de 2025
-- Autor: Manus AI

USE `bendito_docce_db`;

-- -----------------------------------------------------
-- Inserção de Categorias
-- -----------------------------------------------------
INSERT INTO `categories` (`name`, `description`) VALUES
('tradicional', 'Brigadeiros tradicionais com sabores clássicos e receitas familiares'),
('gourmet', 'Brigadeiros gourmet com ingredientes premium e sabores sofisticados'),
('novo', 'Novidades e lançamentos especiais da casa');

-- -----------------------------------------------------
-- Inserção de Produtos
-- -----------------------------------------------------
INSERT INTO `products` (`name`, `description`, `price`, `price_per_hundred`, `image_url`, `category_id`, `is_new`) VALUES
-- Produtos Gourmet
('Brigadeiro Ferrero Rocher', 'Brigadeiro gourmet com sabor Ferrero Rocher', 5.00, 425.00, 'img1.jpeg', 
 (SELECT category_id FROM categories WHERE name = 'gourmet'), FALSE),

('Brigadeiro Red Velvet', 'Brigadeiro com sabor Red Velvet', 4.00, 340.00, 'img2.jpeg', 
 (SELECT category_id FROM categories WHERE name = 'gourmet'), FALSE),

('Brigadeiro Churros', 'Brigadeiro com sabor de churros', 3.50, 297.50, 'img1.jpeg', 
 (SELECT category_id FROM categories WHERE name = 'gourmet'), FALSE),

('Brigadeiro Maracujá', 'Brigadeiro com sabor de maracujá', 3.50, 297.50, 'img2.jpeg', 
 (SELECT category_id FROM categories WHERE name = 'gourmet'), FALSE),

-- Produtos Tradicionais
('Brigadeiro Tradicional', 'Brigadeiro tradicional de chocolate', 3.00, 255.00, 'img1.jpeg', 
 (SELECT category_id FROM categories WHERE name = 'tradicional'), FALSE),

-- Produtos Novos
('Brigadeiro Ninho com Nutella', 'Brigadeiro de leite ninho com nutella', 5.00, 425.00, 'img3.jpeg', 
 (SELECT category_id FROM categories WHERE name = 'novo'), TRUE);

-- -----------------------------------------------------
-- Verificação dos dados inseridos
-- -----------------------------------------------------
-- Para verificar se os dados foram inseridos corretamente, execute:
-- SELECT * FROM categories;
-- SELECT * FROM products;
-- SELECT p.name, p.price, c.name as category FROM products p JOIN categories c ON p.category_id = c.category_id;

-- -----------------------------------------------------
-- End of Script
-- -----------------------------------------------------

