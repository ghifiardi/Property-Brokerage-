"""
Configuration file for AI-powered Property Brokerage System
"""
import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Base configuration"""
    
    # Application settings
    APP_NAME = "AI Property Brokerage System"
    VERSION = "1.0.0"
    
    # Database settings
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///property_brokerage.db")
    
    # AI Model settings
    AI_MODEL_PATH = os.getenv("AI_MODEL_PATH", "models/")
    LEAD_SCORING_MODEL = "lead_scoring_model.pkl"
    PROPERTY_VALUATION_MODEL = "property_valuation_model.pkl"
    
    # Chatbot settings
    CHATBOT_MODEL = os.getenv("CHATBOT_MODEL", "gpt2")
    MAX_RESPONSE_LENGTH = 150
    CHATBOT_TEMPERATURE = 0.7
    
    # Fair Housing Compliance
    PROTECTED_CLASSES = [
        "race",
        "color",
        "national_origin",
        "religion",
        "sex",
        "familial_status",
        "disability"
    ]
    
    # Content Generation settings
    MAX_DESCRIPTION_LENGTH = 500
    CONTENT_LANGUAGES = ["en", "id"]  # English and Indonesian
    
    # Image Processing settings
    IMAGE_MAX_SIZE = (1920, 1080)
    VIRTUAL_STAGING_ENABLED = True
    
    # Privacy and Security
    DATA_ENCRYPTION_ENABLED = True
    LOG_RETENTION_DAYS = 90
    REQUIRE_CONSENT = True
    
    # API Rate Limiting
    API_RATE_LIMIT = "100/hour"
    
    # Disclosure requirements
    AI_DISCLOSURE_REQUIRED = True
    VIRTUAL_STAGING_DISCLOSURE = "This image has been digitally staged"
    AI_GENERATED_CONTENT_DISCLOSURE = "This content was generated with AI assistance"


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False


class TestingConfig(Config):
    """Testing configuration"""
    DEBUG = True
    TESTING = True
    DATABASE_URL = "sqlite:///:memory:"


# Configuration dictionary
config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
    "default": DevelopmentConfig
}
