# Flask-specific configurations
DEBUG = False
SECRET_KEY = 'SOME-SECRET-KEY'
SESSION_COOKIE_SECURE = False

# Flask-user configurations
USER_APP_NAME = "Flask-User Staff App"
USER_ENABLE_EMAIL = False
USER_ENABLE_USERNAME = True
USER_REQUIRE_RETYPE_PASSWORD = False

# YugabyteDB configurations
YBDB_USER = 'admin'
YBDB_PASSWORD = 'admin-pwd'
YBDB_CERTS = '../../certs/root.crt'
YBDB_HOST = 'localhost'
YBDB_PORT = 5433
YBDB_DB = 'admin'
SQLALCHEMY_DATABASE_URI = f'postgresql://{YBDB_USER}:{YBDB_PASSWORD}@{YBDB_HOST}:{YBDB_PORT}/{YBDB_DB}?sslmode=verify-full&sslrootcert={YBDB_CERTS}'

# Redis configuration (if your app uses Redis)
REDIS_URL = 'redis://localhost:6379/0'

# Application-specific configurations
APP_NAME = 'StaffApp'

# Third-party API keys (if your app uses external APIs)

# Other application-specific settings
CACHE_TYPE = 'SimpleCache'
CACHE_DEFAULT_TIMEOUT = 300
