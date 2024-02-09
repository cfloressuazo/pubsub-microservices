# Flask-specific configurations
DEBUG = False
SECRET_KEY = '8d39f0c6befb60ac7d62885d617a6bee'
SESSION_COOKIE_SECURE = False

# Flask-user configurations
USER_APP_NAME = "Flask-User Staff App"
USER_ENABLE_EMAIL = False
USER_ENABLE_USERNAME = True
USER_REQUIRE_RETYPE_PASSWORD = False

# YugabyteDB configurations
YBDB_USER = 'qdt'
YBDB_PASSWORD = 'QDTSuperSecretPassword'
YBDB_CERTS = '/Users/cesar/workspaces/pubsub-microservices/certs/root.crt'
YBDB_HOST = 'us-east-1.de9da17e-994d-49c3-9418-eec104edeeeb.aws.ybdb.io'
YBDB_PORT = 5433
YBDB_DB = 'qdt'
SQLALCHEMY_DATABASE_URI = f'postgresql://{YBDB_USER}:{YBDB_PASSWORD}@{YBDB_HOST}:{YBDB_PORT}/{YBDB_DB}?sslmode=verify-full&sslrootcert={YBDB_CERTS}'

# Redis configuration (if your app uses Redis)
REDIS_URL = 'redis://localhost:6379/0'

# Application-specific configurations
APP_NAME = 'StaffApp'

# Third-party API keys (if your app uses external APIs)

# Other application-specific settings
CACHE_TYPE = 'SimpleCache'
CACHE_DEFAULT_TIMEOUT = 300
