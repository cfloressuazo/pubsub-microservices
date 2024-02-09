from flask import Flask, request
from flask_redis import FlaskRedis
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_caching import Cache

db = SQLAlchemy()
migrate = Migrate()
redis_client = FlaskRedis()
cache = Cache()

def create_app():
    app = Flask(__name__)

    # Load configuration from a file or environment variable
    app.config.from_pyfile('config.py')

    # Import database models
    import staff.models

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    redis_client.init_app(app)
    cache.init_app(app)

    # Index route
    @app.route('/')
    def index():
        port = request.environ.get('SERVER_PORT')
        return f'Hello, I am your waiter on {port}!'

    # Import and register blueprints
    from staff.views import staff_bp
    app.register_blueprint(staff_bp)

    return app
