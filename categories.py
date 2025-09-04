from flask import Blueprint, request, jsonify
from src.models.category import db, Category
from sqlalchemy.exc import IntegrityError

categories_bp = Blueprint('categories', __name__)

@categories_bp.route('/categories', methods=['GET'])
def get_all_categories():
    """Retorna todas as categorias"""
    try:
        categories = Category.query.all()
        return jsonify([category.to_dict() for category in categories]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@categories_bp.route('/categories/<int:category_id>', methods=['GET'])
def get_category(category_id):
    """Retorna uma categoria específica por ID"""
    try:
        category = Category.query.get_or_404(category_id)
        return jsonify(category.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@categories_bp.route('/categories', methods=['POST'])
def create_category():
    """Cria uma nova categoria"""
    try:
        data = request.get_json()
        
        # Validar dados obrigatórios
        if not data or not data.get('name'):
            return jsonify({'error': 'Nome da categoria é obrigatório'}), 400
        
        # Criar nova categoria
        category = Category(
            name=data['name'],
            description=data.get('description')
        )
        
        db.session.add(category)
        db.session.commit()
        
        return jsonify(category.to_dict()), 201
        
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Categoria com este nome já existe'}), 409
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@categories_bp.route('/categories/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    """Atualiza uma categoria existente"""
    try:
        category = Category.query.get_or_404(category_id)
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'Dados não fornecidos'}), 400
        
        # Atualizar campos se fornecidos
        if 'name' in data:
            category.name = data['name']
        if 'description' in data:
            category.description = data['description']
        
        db.session.commit()
        
        return jsonify(category.to_dict()), 200
        
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Categoria com este nome já existe'}), 409
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@categories_bp.route('/categories/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    """Remove uma categoria"""
    try:
        category = Category.query.get_or_404(category_id)
        
        # Verificar se existem produtos associados a esta categoria
        if category.products:
            return jsonify({
                'error': 'Não é possível excluir categoria com produtos associados'
            }), 400
        
        db.session.delete(category)
        db.session.commit()
        
        return jsonify({'message': 'Categoria removida com sucesso'}), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@categories_bp.route('/categories/name/<string:category_name>', methods=['GET'])
def get_category_by_name(category_name):
    """Retorna uma categoria específica por nome"""
    try:
        category = Category.query.filter_by(name=category_name).first()
        if not category:
            return jsonify({'error': 'Categoria não encontrada'}), 404
        
        return jsonify(category.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

