"""
AI-powered Lead Generation and Nurturing System

This module implements AI capabilities for:
- User behavior analysis
- Lead scoring and prioritization
- 24/7 chatbot interaction
"""

import numpy as np
from typing import Dict, List, Optional
from datetime import datetime


class LeadScoringSystem:
    """AI-powered lead scoring and prioritization"""
    
    def __init__(self):
        self.weights = {
            'page_views': 0.15,
            'time_on_site': 0.20,
            'property_inquiries': 0.25,
            'contact_attempts': 0.20,
            'budget_match': 0.20
        }
    
    def analyze_behavior(self, user_data: Dict) -> Dict:
        """
        Analyze user behavior to generate insights
        
        Args:
            user_data: Dictionary containing user interaction data
            
        Returns:
            Dictionary with behavior analysis results
        """
        analysis = {
            'engagement_level': self._calculate_engagement(user_data),
            'intent_score': self._calculate_intent(user_data),
            'readiness_score': self._calculate_readiness(user_data),
            'timestamp': datetime.now().isoformat()
        }
        return analysis
    
    def score_lead(self, user_data: Dict) -> float:
        """
        Calculate lead score based on multiple factors
        
        Args:
            user_data: Dictionary containing user data
            
        Returns:
            Lead score between 0 and 100
        """
        score = 0.0
        
        # Page views contribution
        page_views = min(user_data.get('page_views', 0) / 10, 1.0)
        score += page_views * self.weights['page_views'] * 100
        
        # Time on site contribution (in minutes)
        time_on_site = min(user_data.get('time_on_site', 0) / 30, 1.0)
        score += time_on_site * self.weights['time_on_site'] * 100
        
        # Property inquiries
        inquiries = min(user_data.get('property_inquiries', 0) / 5, 1.0)
        score += inquiries * self.weights['property_inquiries'] * 100
        
        # Contact attempts
        contacts = min(user_data.get('contact_attempts', 0) / 3, 1.0)
        score += contacts * self.weights['contact_attempts'] * 100
        
        # Budget match
        budget_match = user_data.get('budget_match', 0.5)
        score += budget_match * self.weights['budget_match'] * 100
        
        return round(score, 2)
    
    def prioritize_leads(self, leads: List[Dict]) -> List[Dict]:
        """
        Prioritize leads based on their scores
        
        Args:
            leads: List of lead dictionaries
            
        Returns:
            Sorted list of leads with priority rankings
        """
        scored_leads = []
        for lead in leads:
            lead_copy = lead.copy()
            lead_copy['score'] = self.score_lead(lead)
            lead_copy['analysis'] = self.analyze_behavior(lead)
            scored_leads.append(lead_copy)
        
        # Sort by score descending
        scored_leads.sort(key=lambda x: x['score'], reverse=True)
        
        # Add priority ranking
        for idx, lead in enumerate(scored_leads, 1):
            lead['priority_rank'] = idx
            if lead['score'] >= 75:
                lead['priority_level'] = 'HOT'
            elif lead['score'] >= 50:
                lead['priority_level'] = 'WARM'
            else:
                lead['priority_level'] = 'COLD'
        
        return scored_leads
    
    def _calculate_engagement(self, user_data: Dict) -> str:
        """Calculate engagement level"""
        page_views = user_data.get('page_views', 0)
        time_on_site = user_data.get('time_on_site', 0)
        
        if page_views > 10 and time_on_site > 20:
            return 'HIGH'
        elif page_views > 5 or time_on_site > 10:
            return 'MEDIUM'
        return 'LOW'
    
    def _calculate_intent(self, user_data: Dict) -> str:
        """Calculate purchase intent"""
        inquiries = user_data.get('property_inquiries', 0)
        contacts = user_data.get('contact_attempts', 0)
        
        if inquiries > 3 or contacts > 2:
            return 'HIGH'
        elif inquiries > 1 or contacts > 0:
            return 'MEDIUM'
        return 'LOW'
    
    def _calculate_readiness(self, user_data: Dict) -> str:
        """Calculate readiness to buy/sell"""
        budget_match = user_data.get('budget_match', 0)
        timeline = user_data.get('timeline_weeks', 52)
        
        if budget_match > 0.7 and timeline < 12:
            return 'READY'
        elif budget_match > 0.4 and timeline < 26:
            return 'PREPARING'
        return 'EXPLORING'


class AIchatbot:
    """AI-powered chatbot for 24/7 client interaction"""
    
    def __init__(self, model_name: str = "gpt2"):
        self.model_name = model_name
        self.conversation_history = []
        self.available = True
    
    def get_response(self, user_message: str, context: Optional[Dict] = None) -> str:
        """
        Generate AI response to user message
        
        Args:
            user_message: User's input message
            context: Optional context dictionary
            
        Returns:
            AI-generated response
        """
        # Store message in history
        self.conversation_history.append({
            'role': 'user',
            'message': user_message,
            'timestamp': datetime.now().isoformat()
        })
        
        # Generate response based on intent
        response = self._generate_response(user_message, context)
        
        # Store response in history
        self.conversation_history.append({
            'role': 'assistant',
            'message': response,
            'timestamp': datetime.now().isoformat()
        })
        
        return response
    
    def _generate_response(self, message: str, context: Optional[Dict]) -> str:
        """
        Generate appropriate response based on message content
        
        This is a simplified implementation. In production, this would use
        a more sophisticated NLP model.
        """
        message_lower = message.lower()
        
        # Property inquiry
        if any(word in message_lower for word in ['property', 'house', 'apartment', 'listing']):
            return ("I'd be happy to help you find the perfect property! "
                   "Could you tell me more about what you're looking for? "
                   "For example, your preferred location, budget range, and property type?")
        
        # Pricing inquiry
        elif any(word in message_lower for word in ['price', 'cost', 'expensive', 'budget']):
            return ("I can help you understand property prices in your area. "
                   "Our AI system analyzes market trends and comparable properties "
                   "to provide accurate valuations. Would you like me to connect you "
                   "with a broker for a detailed market analysis?")
        
        # Scheduling
        elif any(word in message_lower for word in ['schedule', 'appointment', 'visit', 'tour']):
            return ("I can help you schedule a property viewing! "
                   "What date and time work best for you? "
                   "I'll coordinate with one of our experienced brokers.")
        
        # General greeting
        elif any(word in message_lower for word in ['hello', 'hi', 'hey', 'greetings']):
            return ("Hello! Welcome to our AI-powered property brokerage service. "
                   "I'm here 24/7 to help you with property inquiries, market information, "
                   "and scheduling appointments. How can I assist you today?")
        
        # Default response
        else:
            return ("Thank you for your message. I'm here to assist you with property-related "
                   "inquiries. You can ask me about available properties, market prices, "
                   "schedule viewings, or connect with one of our brokers. "
                   "How can I help you today?")
    
    def get_conversation_summary(self) -> Dict:
        """
        Summarize the conversation
        
        Returns:
            Dictionary with conversation summary
        """
        return {
            'total_messages': len(self.conversation_history),
            'user_messages': len([m for m in self.conversation_history if m['role'] == 'user']),
            'bot_messages': len([m for m in self.conversation_history if m['role'] == 'assistant']),
            'conversation_start': self.conversation_history[0]['timestamp'] if self.conversation_history else None,
            'conversation_end': self.conversation_history[-1]['timestamp'] if self.conversation_history else None
        }
    
    def reset_conversation(self):
        """Reset conversation history"""
        self.conversation_history = []


class LeadNurturingSystem:
    """System for nurturing leads through automated engagement"""
    
    def __init__(self):
        self.engagement_templates = {
            'welcome': "Welcome! Thank you for your interest in our properties.",
            'follow_up': "I wanted to follow up on your recent property inquiry.",
            'market_update': "Here's the latest market update for your area of interest.",
            'new_listing': "A new property matching your criteria just became available!"
        }
    
    def create_engagement_plan(self, lead: Dict) -> List[Dict]:
        """
        Create personalized engagement plan for a lead
        
        Args:
            lead: Lead information dictionary
            
        Returns:
            List of engagement actions with timing
        """
        score = lead.get('score', 0)
        readiness = lead.get('analysis', {}).get('readiness_score', 'EXPLORING')
        
        plan = []
        
        # Immediate welcome
        plan.append({
            'action': 'send_message',
            'template': 'welcome',
            'timing': 'immediate',
            'channel': 'email'
        })
        
        # Follow-up based on readiness
        if readiness == 'READY':
            plan.append({
                'action': 'broker_contact',
                'timing': '1_hour',
                'priority': 'high'
            })
        elif readiness == 'PREPARING':
            plan.append({
                'action': 'send_message',
                'template': 'follow_up',
                'timing': '24_hours',
                'channel': 'email'
            })
        else:
            plan.append({
                'action': 'send_message',
                'template': 'market_update',
                'timing': '7_days',
                'channel': 'email'
            })
        
        # Regular updates for high-score leads
        if score >= 50:
            plan.append({
                'action': 'send_message',
                'template': 'new_listing',
                'timing': 'when_available',
                'channel': 'email_and_sms'
            })
        
        return plan
    
    def generate_personalized_message(self, template_type: str, lead: Dict) -> str:
        """
        Generate personalized message for lead
        
        Args:
            template_type: Type of message template
            lead: Lead information
            
        Returns:
            Personalized message string
        """
        base_message = self.engagement_templates.get(template_type, "")
        name = lead.get('name', 'Valued Client')
        
        return f"Dear {name},\n\n{base_message}\n\nBest regards,\nYour Property Brokerage Team"
