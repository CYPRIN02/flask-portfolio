import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from config import Config
from dotenv import load_dotenv
from flask_mail import Mail

# Load environment variables
load_dotenv()

# Initialize extensions
mail = Mail()

def create_app(config_class=Config):
    """Application factory pattern"""
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions
    mail.init_app(app)
    
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