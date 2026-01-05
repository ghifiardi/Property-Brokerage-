"""
AI-Powered Property Brokerage System
Module 1: Lead Generation & Nurturing

This module provides AI capabilities for:
- Automated lead scoring and qualification
- Intelligent lead nurturing with personalized communication
- Predictive analytics for lead conversion
"""

from typing import List, Dict, Optional
from datetime import datetime
import json


class LeadGenerator:
    """AI-powered lead generation and scoring system"""
    
    def __init__(self, ai_client=None):
        """
        Initialize the Lead Generator
        
        Args:
            ai_client: OpenAI or similar AI client for NLP tasks
        """
        self.ai_client = ai_client
        self.lead_database = []
    
    def analyze_lead(self, lead_data: Dict) -> Dict:
        """
        Analyze and score a lead using AI
        
        Args:
            lead_data: Dictionary containing lead information
            
        Returns:
            Dictionary with lead score and insights
        """
        score = 0
        insights = []
        
        # Budget analysis
        if lead_data.get('budget', 0) > 0:
            if lead_data['budget'] >= 1000000:
                score += 30
                insights.append("High budget potential")
            elif lead_data['budget'] >= 500000:
                score += 20
                insights.append("Medium budget potential")
            else:
                score += 10
                insights.append("Budget-conscious buyer")
        
        # Urgency analysis
        urgency = lead_data.get('urgency', 'medium').lower()
        if urgency == 'high':
            score += 25
            insights.append("High urgency - immediate follow-up required")
        elif urgency == 'medium':
            score += 15
            insights.append("Medium urgency - follow-up within 48 hours")
        else:
            score += 5
            insights.append("Low urgency - periodic follow-up")
        
        # Location preference analysis
        if lead_data.get('preferred_location'):
            score += 15
            insights.append(f"Specific location interest: {lead_data['preferred_location']}")
        
        # Contact quality
        if lead_data.get('email') and lead_data.get('phone'):
            score += 15
            insights.append("Complete contact information")
        elif lead_data.get('email') or lead_data.get('phone'):
            score += 10
            insights.append("Partial contact information")
        
        # Previous interaction
        if lead_data.get('previous_inquiries', 0) > 0:
            score += 15
            insights.append("Returning lead - higher conversion probability")
        
        return {
            'lead_id': lead_data.get('id', str(datetime.now().timestamp())),
            'score': min(score, 100),
            'priority': self._get_priority(score),
            'insights': insights,
            'recommended_actions': self._get_recommended_actions(score, lead_data),
            'analyzed_at': datetime.now().isoformat()
        }
    
    def _get_priority(self, score: int) -> str:
        """Determine priority level based on score"""
        if score >= 70:
            return "HIGH"
        elif score >= 40:
            return "MEDIUM"
        else:
            return "LOW"
    
    def _get_recommended_actions(self, score: int, lead_data: Dict) -> List[str]:
        """Generate recommended actions based on lead analysis"""
        actions = []
        
        if score >= 70:
            actions.append("Immediate phone call within 2 hours")
            actions.append("Send personalized property portfolio")
            actions.append("Schedule in-person viewing")
        elif score >= 40:
            actions.append("Send email with curated property listings")
            actions.append("Follow-up call within 24 hours")
            actions.append("Add to weekly newsletter")
        else:
            actions.append("Add to nurture campaign")
            actions.append("Send monthly market updates")
            actions.append("Monitor engagement metrics")
        
        return actions
    
    def generate_personalized_message(self, lead_data: Dict, message_type: str = "initial") -> str:
        """
        Generate personalized communication for leads
        
        Args:
            lead_data: Lead information
            message_type: Type of message (initial, follow_up, property_match)
            
        Returns:
            Personalized message string
        """
        name = lead_data.get('name', 'valued client')
        budget = lead_data.get('budget', 'your budget')
        location = lead_data.get('preferred_location', 'your preferred area')
        
        templates = {
            'initial': f"""Dear {name},

Thank you for your interest in finding a property. I understand you're looking for properties in {location} with a budget around {budget}.

I would love to help you find your dream property. Based on your preferences, I have several excellent options that might interest you.

When would be a good time for a quick call to discuss your requirements in detail?

Best regards,
Property Broker Team""",
            
            'follow_up': f"""Hi {name},

I wanted to follow up on our previous conversation about properties in {location}. 

I've identified some new listings that match your criteria perfectly. Would you like me to send you the details?

Looking forward to hearing from you!

Best regards,
Property Broker Team""",
            
            'property_match': f"""Dear {name},

Exciting news! I found a property that perfectly matches your requirements in {location} within your budget range.

This property won't last long on the market. Would you be available for a viewing this week?

Let me know your preferred time, and I'll arrange everything.

Best regards,
Property Broker Team"""
        }
        
        return templates.get(message_type, templates['initial'])
    
    def batch_score_leads(self, leads: List[Dict]) -> List[Dict]:
        """
        Score multiple leads in batch
        
        Args:
            leads: List of lead dictionaries
            
        Returns:
            List of analyzed leads with scores
        """
        return [self.analyze_lead(lead) for lead in leads]
    
    def get_high_priority_leads(self, leads: List[Dict]) -> List[Dict]:
        """
        Filter and return high priority leads
        
        Args:
            leads: List of analyzed leads
            
        Returns:
            List of high priority leads
        """
        analyzed_leads = self.batch_score_leads(leads)
        return [lead for lead in analyzed_leads if lead['priority'] == 'HIGH']


class LeadNurturingEngine:
    """Automated lead nurturing and follow-up system"""
    
    def __init__(self):
        self.nurture_campaigns = {}
        self.follow_up_schedule = {}
    
    def create_nurture_campaign(self, campaign_name: str, campaign_config: Dict) -> Dict:
        """
        Create an automated nurture campaign
        
        Args:
            campaign_name: Name of the campaign
            campaign_config: Configuration including schedule and content
            
        Returns:
            Campaign details
        """
        campaign = {
            'name': campaign_name,
            'created_at': datetime.now().isoformat(),
            'status': 'active',
            'config': campaign_config,
            'leads_enrolled': 0
        }
        
        self.nurture_campaigns[campaign_name] = campaign
        return campaign
    
    def enroll_lead_in_campaign(self, lead_id: str, campaign_name: str) -> bool:
        """
        Enroll a lead in a nurture campaign
        
        Args:
            lead_id: Unique lead identifier
            campaign_name: Name of the campaign
            
        Returns:
            Success status
        """
        if campaign_name in self.nurture_campaigns:
            campaign = self.nurture_campaigns[campaign_name]
            campaign['leads_enrolled'] += 1
            
            # Schedule follow-ups
            self.follow_up_schedule[lead_id] = {
                'campaign': campaign_name,
                'next_contact': datetime.now().isoformat(),
                'contact_count': 0
            }
            return True
        return False
    
    def get_due_follow_ups(self) -> List[Dict]:
        """
        Get leads that need follow-up today
        
        Returns:
            List of leads requiring follow-up
        """
        due_follow_ups = []
        current_date = datetime.now().date()
        
        for lead_id, schedule in self.follow_up_schedule.items():
            next_contact = datetime.fromisoformat(schedule['next_contact']).date()
            if next_contact <= current_date:
                due_follow_ups.append({
                    'lead_id': lead_id,
                    'campaign': schedule['campaign'],
                    'contact_count': schedule['contact_count']
                })
        
        return due_follow_ups


# Example usage and demonstration
if __name__ == "__main__":
    # Initialize lead generator
    lead_gen = LeadGenerator()
    
    # Example lead data
    sample_leads = [
        {
            'id': '001',
            'name': 'John Doe',
            'email': 'john@example.com',
            'phone': '+1234567890',
            'budget': 1500000,
            'urgency': 'high',
            'preferred_location': 'Downtown',
            'previous_inquiries': 2
        },
        {
            'id': '002',
            'name': 'Jane Smith',
            'email': 'jane@example.com',
            'budget': 600000,
            'urgency': 'medium',
            'preferred_location': 'Suburbs',
            'previous_inquiries': 0
        }
    ]
    
    # Analyze leads
    print("=== Lead Analysis Results ===")
    for lead in sample_leads:
        analysis = lead_gen.analyze_lead(lead)
        print(f"\nLead ID: {analysis['lead_id']}")
        print(f"Score: {analysis['score']}/100")
        print(f"Priority: {analysis['priority']}")
        print(f"Insights: {', '.join(analysis['insights'])}")
        print(f"Recommended Actions:")
        for action in analysis['recommended_actions']:
            print(f"  - {action}")
    
    # Generate personalized message
    print("\n=== Personalized Message ===")
    message = lead_gen.generate_personalized_message(sample_leads[0], 'initial')
    print(message)
    
    # Lead nurturing
    nurture_engine = LeadNurturingEngine()
    campaign = nurture_engine.create_nurture_campaign(
        'New Buyer Campaign',
        {
            'duration_days': 30,
            'touchpoints': 5,
            'channels': ['email', 'sms', 'phone']
        }
    )
    print(f"\n=== Nurture Campaign Created ===")
    print(f"Campaign: {campaign['name']}")
    print(f"Status: {campaign['status']}")
