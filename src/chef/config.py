# Flask-specific configurations
DEBUG = False
SECRET_KEY = '8d39f0c6befb60ac7d62885d617a6bee'
SESSION_COOKIE_SECURE = False
SQLALCHEMY_DATABASE_URI = 'postgresql://admin:admin-pwd@us-east-1.ea53f2e6-4666-4fce-999c-2f7d7fc6b4ea.aws.ybdb.io:5433/yugabyte?ssl=true&sslmode=verify-full&sslrootcert=../../certs/root.crt'

# Redis configuration (if your app uses Redis)
REDIS_URL = 'redis://localhost:6379/0'

# Application-specific configurations
APP_NAME = 'ChefApp'

# Third-party API keys (if your app uses external APIs)

# Other application-specific settings
