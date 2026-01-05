"""
Unit tests for Lead Generation AI modules
"""

import pytest
from src.ai_modules.lead_generation import (
    LeadScoringSystem,
    AIchatbot,
    LeadNurturingSystem
)


class TestLeadScoringSystem:
    """Test Lead Scoring System"""
    
    def setup_method(self):
        """Setup test fixtures"""
        self.scorer = LeadScoringSystem()
    
    def test_score_lead_high_score(self):
        """Test scoring a high-quality lead"""
        lead_data = {
            'page_views': 15,
            'time_on_site': 45,
            'property_inquiries': 5,
            'contact_attempts': 3,
            'budget_match': 0.9
        }
        score = self.scorer.score_lead(lead_data)
        
        assert isinstance(score, float)
        assert score >= 75, "High quality lead should score above 75"
        assert score <= 100, "Score should not exceed 100"
    
    def test_score_lead_low_score(self):
        """Test scoring a low-quality lead"""
        lead_data = {
            'page_views': 1,
            'time_on_site': 2,
            'property_inquiries': 0,
            'contact_attempts': 0,
            'budget_match': 0.3
        }
        score = self.scorer.score_lead(lead_data)
        
        assert isinstance(score, float)
        assert score < 50, "Low quality lead should score below 50"
    
    def test_analyze_behavior(self):
        """Test behavior analysis"""
        lead_data = {
            'page_views': 8,
            'time_on_site': 25,
            'property_inquiries': 3,
            'contact_attempts': 1,
            'budget_match': 0.7,
            'timeline_weeks': 10
        }
        analysis = self.scorer.analyze_behavior(lead_data)
        
        assert 'engagement_level' in analysis
        assert 'intent_score' in analysis
        assert 'readiness_score' in analysis
        assert analysis['engagement_level'] in ['HIGH', 'MEDIUM', 'LOW']
    
    def test_prioritize_leads(self):
        """Test lead prioritization"""
        leads = [
            {'name': 'Lead 1', 'page_views': 5, 'time_on_site': 10, 'property_inquiries': 1,
             'contact_attempts': 0, 'budget_match': 0.5},
            {'name': 'Lead 2', 'page_views': 15, 'time_on_site': 40, 'property_inquiries': 5,
             'contact_attempts': 3, 'budget_match': 0.9},
            {'name': 'Lead 3', 'page_views': 8, 'time_on_site': 20, 'property_inquiries': 2,
             'contact_attempts': 1, 'budget_match': 0.7}
        ]
        
        prioritized = self.scorer.prioritize_leads(leads)
        
        assert len(prioritized) == 3
        assert prioritized[0]['priority_rank'] == 1
        assert prioritized[0]['score'] >= prioritized[1]['score']
        assert prioritized[1]['score'] >= prioritized[2]['score']
        assert 'priority_level' in prioritized[0]


class TestAIChatbot:
    """Test AI Chatbot"""
    
    def setup_method(self):
        """Setup test fixtures"""
        self.chatbot = AIchatbot()
    
    def test_chatbot_response(self):
        """Test chatbot generates response"""
        message = "Hello, I'm looking for a house"
        response = self.chatbot.get_response(message)
        
        assert isinstance(response, str)
        assert len(response) > 0
    
    def test_property_inquiry_response(self):
        """Test chatbot responds to property inquiry"""
        message = "Do you have any 3-bedroom properties available?"
        response = self.chatbot.get_response(message)
        
        assert isinstance(response, str)
        assert 'property' in response.lower() or 'bedroom' in response.lower()
    
    def test_conversation_history(self):
        """Test conversation history tracking"""
        self.chatbot.get_response("Hello")
        self.chatbot.get_response("I need help finding a house")
        
        summary = self.chatbot.get_conversation_summary()
        
        assert summary['total_messages'] == 4  # 2 user + 2 bot
        assert summary['user_messages'] == 2
        assert summary['bot_messages'] == 2
    
    def test_reset_conversation(self):
        """Test conversation reset"""
        self.chatbot.get_response("Hello")
        self.chatbot.reset_conversation()
        
        summary = self.chatbot.get_conversation_summary()
        assert summary['total_messages'] == 0


class TestLeadNurturingSystem:
    """Test Lead Nurturing System"""
    
    def setup_method(self):
        """Setup test fixtures"""
        self.nurturer = LeadNurturingSystem()
    
    def test_create_engagement_plan(self):
        """Test engagement plan creation"""
        lead = {
            'name': 'John Doe',
            'score': 85,
            'analysis': {
                'readiness_score': 'READY'
            }
        }
        
        plan = self.nurturer.create_engagement_plan(lead)
        
        assert isinstance(plan, list)
        assert len(plan) > 0
        assert all('action' in item for item in plan)
        assert all('timing' in item for item in plan)
    
    def test_generate_personalized_message(self):
        """Test personalized message generation"""
        lead = {'name': 'Jane Smith'}
        message = self.nurturer.generate_personalized_message('welcome', lead)
        
        assert isinstance(message, str)
        assert 'Jane Smith' in message


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
