from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Category(db.Model):
    """Modelo para a tabela de categorias"""
    __tablename__ = 'categories'
    
    category_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=True)
    
    # Relacionamento com produtos
    products = db.relationship('Product', backref='category', lazy=True)
    
    def __init__(self, name, description=None):
        self.name = name
        self.description = description
    
    def to_dict(self):
        """Converte o objeto para dicionário"""
        return {
            'category_id': self.category_id,
            'name': self.name,
            'description': self.description
        }
    
    def __repr__(self):
        return f'<Category {self.name}>'

