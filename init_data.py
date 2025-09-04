from flask import Blueprint, jsonify
from src.models.category import db, Category
from src.models.product import Product

init_bp = Blueprint('init', __name__)

@init_bp.route('/init-data', methods=['POST'])
def initialize_data():
    """Inicializa o banco de dados com dados de exemplo"""
    try:
        # Verificar se já existem dados
        if Category.query.count() > 0:
            return jsonify({'message': 'Dados já foram inicializados'}), 200
        
        # Criar categorias
        categories_data = [
            {'name': 'tradicional', 'description': 'Brigadeiros tradicionais com sabores clássicos e receitas familiares'},
            {'name': 'gourmet', 'description': 'Brigadeiros gourmet com ingredientes premium e sabores sofisticados'},
            {'name': 'novo', 'description': 'Novidades e lançamentos especiais da casa'}
        ]
        
        categories = {}
        for cat_data in categories_data:
            category = Category(name=cat_data['name'], description=cat_data['description'])
            db.session.add(category)
            db.session.flush()  # Para obter o ID
            categories[cat_data['name']] = category.category_id
        
        # Criar produtos
        products_data = [
            {
                'name': 'Brigadeiro Ferrero Rocher',
                'description': 'Brigadeiro gourmet com sabor Ferrero Rocher',
                'price': 5.00,
                'image_url': 'img1.jpeg',
                'category': 'gourmet',
                'is_new': False
            },
            {
                'name': 'Brigadeiro Red Velvet',
                'description': 'Brigadeiro com sabor Red Velvet',
                'price': 4.00,
                'image_url': 'img2.jpeg',
                'category': 'gourmet',
                'is_new': False
            },
            {
                'name': 'Brigadeiro Churros',
                'description': 'Brigadeiro com sabor de churros',
                'price': 3.50,
                'image_url': 'img1.jpeg',
                'category': 'gourmet',
                'is_new': False
            },
            {
                'name': 'Brigadeiro Maracujá',
                'description': 'Brigadeiro com sabor de maracujá',
                'price': 3.50,
                'image_url': 'img2.jpeg',
                'category': 'gourmet',
                'is_new': False
            },
            {
                'name': 'Brigadeiro Tradicional',
                'description': 'Brigadeiro tradicional de chocolate',
                'price': 3.00,
                'image_url': 'img1.jpeg',
                'category': 'tradicional',
                'is_new': False
            },
            {
                'name': 'Brigadeiro Ninho com Nutella',
                'description': 'Brigadeiro de leite ninho com nutella',
                'price': 5.00,
                'image_url': 'img3.jpeg',
                'category': 'novo',
                'is_new': True
            }
        ]
        
        for prod_data in products_data:
            product = Product(
                name=prod_data['name'],
                description=prod_data['description'],
                price=prod_data['price'],
                image_url=prod_data['image_url'],
                category_id=categories[prod_data['category']],
                is_new=prod_data['is_new']
            )
            db.session.add(product)
        
        db.session.commit()
        
        return jsonify({
            'message': 'Dados inicializados com sucesso',
            'categories_created': len(categories_data),
            'products_created': len(products_data)
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

