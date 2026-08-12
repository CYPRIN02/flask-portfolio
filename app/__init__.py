import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, flash, redirect, url_for
from config import Config
from dotenv import load_dotenv
from flask_mail import Mail
from flask_wtf.csrf import CSRFError, CSRFProtect

# Load environment variables
load_dotenv()

# Initialize extensions
mail = Mail()
csrf = CSRFProtect()

def create_app(config_class=Config):
    """Application factory pattern"""
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions
    mail.init_app(app)
    csrf.init_app(app)

    @app.errorhandler(CSRFError)
    def handle_csrf_error(error):
        app.logger.warning("CSRF validation failed: %s", error.description)
        flash('Your session expired. Please try again.', 'warning')
        return redirect(url_for('contact'))

    @app.after_request
    def add_security_headers(response):
        response.headers.setdefault('X-Content-Type-Options', 'nosniff')
        response.headers.setdefault('X-Frame-Options', 'DENY')
        response.headers.setdefault('Referrer-Policy', 'strict-origin-when-cross-origin')
        response.headers.setdefault('Permissions-Policy', 'camera=(), microphone=(), geolocation=()')
        response.headers.setdefault(
            'Content-Security-Policy',
            "default-src 'self'; "
            "img-src 'self' data: https://gauxrigjmrovzsqygmqx.supabase.co; "
            "media-src 'self' https://gauxrigjmrovzsqygmqx.supabase.co; "
            "style-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net https://cdnjs.cloudflare.com; "
            "script-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net https://cdnjs.cloudflare.com; "
            "font-src 'self' data: https://cdnjs.cloudflare.com; "
            "connect-src 'self'; "
            "frame-ancestors 'none'; "
            "base-uri 'self'; "
            "form-action 'self'"
        )
        return response
    
    # Configure logging
    if not app.debug:
        if not os.path.exists('logs'):
            os.mkdir('logs')
        
        file_handler = RotatingFileHandler('logs/portfolio.log', 
                                         maxBytes=10240,
                                         backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
        ))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
        app.logger.setLevel(logging.INFO)
        app.logger.info('Portfolio startup')
    
    # Import and register routes
    from app.routes import init_routes
    init_routes(app)
    
    return app
