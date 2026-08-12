import os
import secrets


def _str_to_bool(value, default=False):
    if value is None:
        return default
    if isinstance(value, bool):
        return value
    return value.strip().lower() in {"1", "true", "yes", "on"}

class Config:
    """Configuration settings for the Flask application"""
    
    # Secret key for session management and CSRF protection
    SECRET_KEY = (
        os.environ.get('SECRET_KEY')
        or os.environ.get('FLASK_SECRET_KEY')
        or secrets.token_urlsafe(32)
    )
    WTF_CSRF_TIME_LIMIT = int(os.environ.get('WTF_CSRF_TIME_LIMIT') or 3600)
    MAX_CONTENT_LENGTH = int(os.environ.get('MAX_CONTENT_LENGTH') or 16 * 1024)
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    SESSION_COOKIE_SECURE = _str_to_bool(os.environ.get('SESSION_COOKIE_SECURE'), bool(os.environ.get('RENDER')))
    
    # Database configuration (SQLite for development)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///portfolio.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Mail server settings (for contact form)
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.gmail.com'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
    MAIL_USE_TLS = _str_to_bool(os.environ.get('MAIL_USE_TLS'), True)
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')
    ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL')
    
    # Airtable configuration
    AIRTABLE_BASE_ID = os.environ.get('AIRTABLE_BASE_ID') or 'apphCq9dOEExpWKrf'
    AIRTABLE_TABLE_ID = os.environ.get('AIRTABLE_TABLE_ID') or 'tblC0fElkkfLDlacM'

    # Supabase public storage configuration
    SUPABASE_URL = os.environ.get('SUPABASE_URL') or 'https://gauxrigjmrovzsqygmqx.supabase.co'
    SUPABASE_KEY = os.environ.get('SUPABASE_KEY')
    SUPABASE_BUCKET = os.environ.get('SUPABASE_BUCKET') or 'portfolio-media'
