# Flask-specific configurations
DEBUG = False
SECRET_KEY = 'SOME-SECRET-KEY'
SESSION_COOKIE_SECURE = False
SQLALCHEMY_DATABASE_URI = 'postgresql://admin:admin-pwd@localhost'

# Redis configuration (if your app uses Redis)
REDIS_URL = 'redis://localhost:6379/0'

# Application-specific configurations
APP_NAME = 'ChefApp'

# Third-party API keys (if your app uses external APIs)

# Other application-specific settings
