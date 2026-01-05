"""
AI-Powered Property Brokerage System

This package provides comprehensive AI capabilities for modern property brokers,
including lead generation, market analysis, content creation, workflow automation,
client experience personalization, and property operations management.

All modules are designed with ethical AI principles in mind, including:
- Fair Housing Act compliance
- Transparency and disclosure requirements
- Data privacy and security
- Human oversight and verification
"""

__version__ = "1.0.0"
__author__ = "Property Brokerage AI Team"

from .lead_generation import LeadScoringSystem, AIchatbot, LeadNurturingSystem
from .market_analysis import AutomatedValuationModel, MarketAnalyzer
from .content_marketing import (
    PropertyDescriptionGenerator,
    SocialMediaContentGenerator,
    ImageEnhancementService,
    MarketingAutomation
)
from .workflow_automation import (
    AppointmentScheduler,
    ContractReviewSystem,
    DocumentProcessor
)
from .client_experience import (
    PropertyRecommendationSystem,
    MeetingSummarizer,
    ClientInteractionAnalyzer
)
from .property_operations import (
    TenantScreeningSystem,
    MaintenanceScheduler,
    DroneImageAnalyzer
)
from .ethical_compliance import (
    FairHousingCompliance,
    TransparencyManager,
    DataPrivacyManager,
    AccuracyVerificationSystem
)

__all__ = [
    # Lead Generation
    'LeadScoringSystem',
    'AIchatbot',
    'LeadNurturingSystem',
    
    # Market Analysis
    'AutomatedValuationModel',
    'MarketAnalyzer',
    
    # Content & Marketing
    'PropertyDescriptionGenerator',
    'SocialMediaContentGenerator',
    'ImageEnhancementService',
    'MarketingAutomation',
    
    # Workflow Automation
    'AppointmentScheduler',
    'ContractReviewSystem',
    'DocumentProcessor',
    
    # Client Experience
    'PropertyRecommendationSystem',
    'MeetingSummarizer',
    'ClientInteractionAnalyzer',
    
    # Property Operations
    'TenantScreeningSystem',
    'MaintenanceScheduler',
    'DroneImageAnalyzer',
    
    # Ethics & Compliance
    'FairHousingCompliance',
    'TransparencyManager',
    'DataPrivacyManager',
    'AccuracyVerificationSystem',
]
