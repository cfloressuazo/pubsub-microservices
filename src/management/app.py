from flask import Flask
from flask_redis import FlaskRedis
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
redis_client = FlaskRedis()

def create_app():
    app = Flask(__name__)

    # Configuration
    app.config.from_pyfile('config.py')

    # Initialize extensions
    db.init_app(app)
    redis_client.init_app(app)

    # Index route
    @app.route('/')
    def index():
        return 'Hello, I am the manager!'

    # Blueprints
    from management.views import mgnt_bp
    app.register_blueprint(mgnt_bp)

    return app
