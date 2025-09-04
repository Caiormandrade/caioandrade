from flask import Blueprint, request, jsonify
from src.models.category import db
from src.models.product import Product
from src.models.category import Category
from sqlalchemy.exc import IntegrityError

products_bp = Blueprint('products', __name__)

@products_bp.route('/products', methods=['GET'])
def get_all_products():
    """Retorna todos os produtos"""
    try:
        products = Product.query.all()
        return jsonify([product.to_dict() for product in products]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@products_bp.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Retorna um produto específico por ID"""
    try:
        product = Product.query.get_or_404(product_id)
        return jsonify(product.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@products_bp.route('/products', methods=['POST'])
def create_product():
    """Cria um novo produto"""
    try:
        data = request.get_json()
        
        # Validar dados obrigatórios
        if not data or not data.get('name') or not data.get('price') or not data.get('category_id'):
            return jsonify({'error': 'Nome, preço e categoria são obrigatórios'}), 400
        
        # Verificar se a categoria existe
        category = Category.query.get(data['category_id'])
        if not category:
            return jsonify({'error': 'Categoria não encontrada'}), 404
        
        # Criar novo produto
        product = Product(
            name=data['name'],
            description=data.get('description'),
            price=data['price'],
            price_per_hundred=data.get('price_per_hundred'),
            image_url=data.get('image_url'),
            category_id=data['category_id'],
            is_new=data.get('is_new', False)
        )
        
        db.session.add(product)
        db.session.commit()
        
        return jsonify(product.to_dict()), 201
        
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Produto com este nome já existe'}), 409
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@products_bp.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """Atualiza um produto existente"""
    try:
        product = Product.query.get_or_404(product_id)
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'Dados não fornecidos'}), 400
        
        # Atualizar campos se fornecidos
        if 'name' in data:
            product.name = data['name']
        if 'description' in data:
            product.description = data['description']
        if 'price' in data:
            product.price = data['price']
            # Recalcular preço por cento se não fornecido
            if 'price_per_hundred' not in data:
                product.price_per_hundred = product.calculate_price_per_hundred(data['price'])
        if 'price_per_hundred' in data:
            product.price_per_hundred = data['price_per_hundred']
        if 'image_url' in data:
            product.image_url = data['image_url']
        if 'category_id' in data:
            # Verificar se a categoria existe
            category = Category.query.get(data['category_id'])
            if not category:
                return jsonify({'error': 'Categoria não encontrada'}), 404
            product.category_id = data['category_id']
        if 'is_new' in data:
            product.is_new = data['is_new']
        
        db.session.commit()
        
        return jsonify(product.to_dict()), 200
        
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Produto com este nome já existe'}), 409
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@products_bp.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """Remove um produto"""
    try:
        product = Product.query.get_or_404(product_id)
        
        db.session.delete(product)
        db.session.commit()
        
        return jsonify({'message': 'Produto removido com sucesso'}), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@products_bp.route('/products/category/<string:category_name>', methods=['GET'])
def get_products_by_category(category_name):
    """Retorna produtos de uma categoria específica"""
    try:
        category = Category.query.filter_by(name=category_name).first()
        if not category:
            return jsonify({'error': 'Categoria não encontrada'}), 404
        
        products = Product.query.filter_by(category_id=category.category_id).all()
        return jsonify([product.to_dict() for product in products]), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@products_bp.route('/products/new', methods=['GET'])
def get_new_products():
    """Retorna apenas produtos marcados como novidade"""
    try:
        products = Product.query.filter_by(is_new=True).all()
        return jsonify([product.to_dict() for product in products]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

