from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import Numeric
from src.models.category import db

class Product(db.Model):
    """Modelo para a tabela de produtos"""
    __tablename__ = 'products'
    
    product_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(Numeric(10, 2), nullable=False)
    price_per_hundred = db.Column(Numeric(10, 2), nullable=True)
    image_url = db.Column(db.String(255), nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.category_id'), nullable=False)
    is_new = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    def __init__(self, name, price, category_id, description=None, price_per_hundred=None, 
                 image_url=None, is_new=False):
        self.name = name
        self.description = description
        self.price = price
        self.price_per_hundred = price_per_hundred or self.calculate_price_per_hundred(price)
        self.image_url = image_url
        self.category_id = category_id
        self.is_new = is_new
    
    def calculate_price_per_hundred(self, unit_price):
        """Calcula o preço por cento com 15% de desconto"""
        return float(unit_price) * 100 * 0.85
    
    def to_dict(self):
        """Converte o objeto para dicionário"""
        return {
            'product_id': self.product_id,
            'name': self.name,
            'description': self.description,
            'price': float(self.price),
            'price_per_hundred': float(self.price_per_hundred) if self.price_per_hundred else None,
            'image_url': self.image_url,
            'category_id': self.category_id,
            'category_name': self.category.name if self.category else None,
            'is_new': self.is_new,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
    
    def __repr__(self):
        return f'<Product {self.name}>'

