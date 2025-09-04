-- SQL Script para Criação das Tabelas do Banco de Dados Bendito Docce
-- Versão: 1.0
-- Data: 25 de Julho de 2025
-- Autor: Manus AI

-- -----------------------------------------------------
-- Schema `bendito_docce_db`
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `bendito_docce_db` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci ;
USE `bendito_docce_db` ;

-- -----------------------------------------------------
-- Table `bendito_docce_db`.`categories`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bendito_docce_db`.`categories` (
  `category_id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NOT NULL UNIQUE,
  `description` TEXT NULL,
  PRIMARY KEY (`category_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;

-- -----------------------------------------------------
-- Table `bendito_docce_db`.`products`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `bendito_docce_db`.`products` (
  `product_id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `description` TEXT NULL,
  `price` DECIMAL(10, 2) NOT NULL,
  `price_per_hundred` DECIMAL(10, 2) NULL,
  `image_url` VARCHAR(255) NULL,
  `category_id` INT NOT NULL,
  `is_new` BOOLEAN NOT NULL DEFAULT FALSE,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`product_id`),
  INDEX `fk_products_categories_idx` (`category_id` ASC) VISIBLE,
  CONSTRAINT `fk_products_categories`
    FOREIGN KEY (`category_id`)
    REFERENCES `bendito_docce_db`.`categories` (`category_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;

-- -----------------------------------------------------
-- End of Script
-- -----------------------------------------------------

