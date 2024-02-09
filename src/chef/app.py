from flask import Flask, request
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
        # get the port of the running app
        port = request.environ.get('SERVER_PORT')
        return f'Hello, I am your Chef on {port}!'

    # Blueprints
    from chef.views import chef_bp
    app.register_blueprint(chef_bp)

    return app
