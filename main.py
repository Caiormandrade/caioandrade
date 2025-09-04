import os
import sys
# DON'T CHANGE THIS !!!
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, send_from_directory
from flask_cors import CORS
from src.config import config
from src.models.category import db
from src.models.product import Product
from src.models.category import Category

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'))

# Configuração da aplicação
config_name = os.environ.get('FLASK_ENV') or 'development'
app.config.from_object(config[config_name])

# Habilitar CORS para todas as rotas
CORS(app, origins="*")

# Inicializar banco de dados
db.init_app(app)

# Importar e registrar blueprints
from src.routes.products import products_bp
from src.routes.categories import categories_bp
from src.routes.init_data import init_bp

app.register_blueprint(products_bp, url_prefix='/api')
app.register_blueprint(categories_bp, url_prefix='/api')
app.register_blueprint(init_bp, url_prefix='/api')

# Criar tabelas se não existirem
with app.app_context():
    try:
        db.create_all()
        print("Tabelas criadas com sucesso!")
    except Exception as e:
        print(f"Erro ao criar tabelas: {e}")

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    static_folder_path = app.static_folder
    if static_folder_path is None:
            return "Static folder not configured", 404

    if path != "" and os.path.exists(os.path.join(static_folder_path, path)):
        return send_from_directory(static_folder_path, path)
    else:
        index_path = os.path.join(static_folder_path, 'index.html')
        if os.path.exists(index_path):
            return send_from_directory(static_folder_path, 'index.html')
        else:
            return "index.html not found", 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
