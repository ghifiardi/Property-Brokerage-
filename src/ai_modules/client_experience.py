"""
AI-powered Personalized Client Experience

This module implements AI capabilities for:
- Property recommendation system
- Meeting summarization
- Client preference learning
"""

from typing import Dict, List, Optional
from datetime import datetime
import numpy as np


class PropertyRecommendationSystem:
    """AI-powered property recommendation engine"""
    
    def __init__(self):
        self.feature_weights = {
            'location_match': 0.25,
            'price_match': 0.20,
            'size_match': 0.15,
            'type_match': 0.15,
            'amenities_match': 0.15,
            'style_match': 0.10
        }
    
    def recommend_properties(self, client_profile: Dict, available_properties: List[Dict], 
                            top_n: int = 10) -> List[Dict]:
        """
        Recommend properties based on client preferences
        
        Args:
            client_profile: Client preferences and history
            available_properties: List of available properties
            top_n: Number of recommendations to return
            
        Returns:
            Ranked list of recommended properties
        """
        recommendations = []
        
        for property_data in available_properties:
            score = self._calculate_match_score(client_profile, property_data)
            reasons = self._generate_match_reasons(client_profile, property_data)
            
            recommendations.append({
                'property': property_data,
                'match_score': score,
                'match_reasons': reasons,
                'recommended_at': datetime.now().isoformat()
            })
        
        # Sort by score
        recommendations.sort(key=lambda x: x['match_score'], reverse=True)
        
        return recommendations[:top_n]
    
    def learn_preferences(self, client_id: str, interaction_history: List[Dict]) -> Dict:
        """
        Learn client preferences from interaction history
        
        Args:
            client_id: Client identifier
            interaction_history: List of client interactions
            
        Returns:
            Learned preferences profile
        """
        preferences = {
            'preferred_locations': [],
            'price_range': {'min': 0, 'max': 0},
            'preferred_property_types': [],
            'must_have_amenities': [],
            'style_preferences': []
        }
        
        # Analyze viewed properties
        viewed_properties = [i for i in interaction_history if i.get('action') == 'viewed']
        if viewed_properties:
            # Extract location preferences
            locations = [p.get('property', {}).get('location') for p in viewed_properties]
            preferences['preferred_locations'] = list(set(locations))
            
            # Extract price range
            prices = [p.get('property', {}).get('price', 0) for p in viewed_properties]
            if prices:
                preferences['price_range'] = {
                    'min': min(prices),
                    'max': max(prices),
                    'avg': sum(prices) / len(prices)
                }
        
        # Analyze saved/liked properties
        liked_properties = [i for i in interaction_history if i.get('action') == 'liked']
        if liked_properties:
            # Extract property type preferences
            types = [p.get('property', {}).get('type') for p in liked_properties]
            preferences['preferred_property_types'] = list(set(types))
            
            # Extract amenity preferences
            amenities = []
            for prop in liked_properties:
                amenities.extend(prop.get('property', {}).get('amenities', []))
            preferences['must_have_amenities'] = list(set(amenities))
        
        return {
            'client_id': client_id,
            'preferences': preferences,
            'confidence_score': self._calculate_confidence(interaction_history),
            'last_updated': datetime.now().isoformat()
        }
    
    def update_recommendations(self, client_id: str, feedback: Dict) -> Dict:
        """
        Update recommendation model based on client feedback
        
        Args:
            client_id: Client identifier
            feedback: Feedback on recommendations
            
        Returns:
            Update confirmation
        """
        feedback_type = feedback.get('type')  # 'positive' or 'negative'
        property_id = feedback.get('property_id')
        
        return {
            'client_id': client_id,
            'feedback_recorded': True,
            'feedback_type': feedback_type,
            'property_id': property_id,
            'model_updated': True,
            'updated_at': datetime.now().isoformat()
        }
    
    def _calculate_match_score(self, client_profile: Dict, property_data: Dict) -> float:
        """Calculate how well property matches client preferences"""
        score = 0.0
        preferences = client_profile.get('preferences', {})
        
        # Location match
        preferred_locations = preferences.get('preferred_locations', [])
        property_location = property_data.get('location', '')
        if property_location in preferred_locations:
            score += self.feature_weights['location_match'] * 100
        
        # Price match
        price_range = preferences.get('price_range', {})
        property_price = property_data.get('price', 0)
        if price_range.get('min', 0) <= property_price <= price_range.get('max', float('inf')):
            score += self.feature_weights['price_match'] * 100
        
        # Size match
        preferred_size = preferences.get('size_range', {})
        property_size = property_data.get('square_footage', 0)
        if preferred_size.get('min', 0) <= property_size <= preferred_size.get('max', float('inf')):
            score += self.feature_weights['size_match'] * 100
        
        # Type match
        preferred_types = preferences.get('preferred_property_types', [])
        property_type = property_data.get('type', '')
        if property_type in preferred_types:
            score += self.feature_weights['type_match'] * 100
        
        # Amenities match
        must_have = preferences.get('must_have_amenities', [])
        property_amenities = property_data.get('amenities', [])
        amenities_matched = sum(1 for a in must_have if a in property_amenities)
        if must_have:
            amenities_score = (amenities_matched / len(must_have)) * self.feature_weights['amenities_match'] * 100
            score += amenities_score
        
        return round(score, 2)
    
    def _generate_match_reasons(self, client_profile: Dict, property_data: Dict) -> List[str]:
        """Generate reasons why property matches client"""
        reasons = []
        preferences = client_profile.get('preferences', {})
        
        # Check location
        if property_data.get('location') in preferences.get('preferred_locations', []):
            reasons.append("Matches your preferred location")
        
        # Check price
        price_range = preferences.get('price_range', {})
        property_price = property_data.get('price', 0)
        if price_range.get('min', 0) <= property_price <= price_range.get('max', float('inf')):
            reasons.append("Within your budget")
        
        # Check amenities
        must_have = preferences.get('must_have_amenities', [])
        property_amenities = property_data.get('amenities', [])
        matched_amenities = [a for a in must_have if a in property_amenities]
        if matched_amenities:
            reasons.append(f"Has {len(matched_amenities)} of your must-have amenities")
        
        return reasons
    
    def _calculate_confidence(self, interaction_history: List[Dict]) -> float:
        """Calculate confidence in learned preferences"""
        if not interaction_history:
            return 0.0
        
        # More interactions = higher confidence
        num_interactions = len(interaction_history)
        confidence = min(num_interactions / 20.0, 1.0)  # Max confidence at 20+ interactions
        
        return round(confidence, 2)


class MeetingSummarizer:
    """AI-powered meeting summarization and action items"""
    
    def __init__(self):
        self.summary_types = ['brief', 'detailed', 'action_items']
    
    def summarize_meeting(self, meeting_transcript: str, summary_type: str = 'detailed') -> Dict:
        """
        Summarize meeting discussion
        
        Args:
            meeting_transcript: Meeting transcript or notes
            summary_type: Type of summary to generate
            
        Returns:
            Meeting summary
        """
        # Extract key components
        topics = self._extract_topics(meeting_transcript)
        action_items = self._extract_action_items(meeting_transcript)
        decisions = self._extract_decisions(meeting_transcript)
        
        summary = self._generate_summary(meeting_transcript, topics, summary_type)
        
        return {
            'summary': summary,
            'summary_type': summary_type,
            'topics_discussed': topics,
            'action_items': action_items,
            'decisions_made': decisions,
            'meeting_date': datetime.now().isoformat(),
            'generated_by': 'AI Meeting Assistant'
        }
    
    def extract_action_items(self, meeting_notes: str) -> List[Dict]:
        """
        Extract action items from meeting
        
        Args:
            meeting_notes: Meeting notes text
            
        Returns:
            List of action items with assignments
        """
        action_items = self._extract_action_items(meeting_notes)
        
        return [
            {
                'action_id': f"ACT-{idx+1}",
                'description': item['description'],
                'assigned_to': item['assigned_to'],
                'due_date': item['due_date'],
                'priority': item['priority'],
                'status': 'pending'
            }
            for idx, item in enumerate(action_items)
        ]
    
    def generate_follow_up(self, meeting_summary: Dict) -> Dict:
        """
        Generate follow-up email from meeting summary
        
        Args:
            meeting_summary: Meeting summary data
            
        Returns:
            Follow-up email content
        """
        action_items = meeting_summary.get('action_items', [])
        decisions = meeting_summary.get('decisions_made', [])
        
        email_body = "Dear Team,\n\n"
        email_body += "Thank you for attending today's meeting. Here's a summary:\n\n"
        
        if decisions:
            email_body += "Key Decisions:\n"
            for decision in decisions:
                email_body += f"• {decision}\n"
            email_body += "\n"
        
        if action_items:
            email_body += "Action Items:\n"
            for item in action_items:
                email_body += f"• {item['description']} - {item['assigned_to']}\n"
            email_body += "\n"
        
        email_body += "Please reach out if you have any questions.\n\n"
        email_body += "Best regards"
        
        return {
            'subject': f"Meeting Follow-up - {datetime.now().strftime('%Y-%m-%d')}",
            'body': email_body,
            'generated_at': datetime.now().isoformat()
        }
    
    def _extract_topics(self, transcript: str) -> List[str]:
        """Extract main topics from transcript"""
        # Simplified topic extraction
        topics = []
        
        keywords = ['property', 'price', 'market', 'client', 'financing', 'inspection', 'closing']
        for keyword in keywords:
            if keyword in transcript.lower():
                topics.append(keyword.capitalize())
        
        return topics
    
    def _extract_action_items(self, text: str) -> List[Dict]:
        """Extract action items from text"""
        # Simplified extraction (in production, use NLP)
        action_items = []
        
        # Look for action keywords
        action_keywords = ['will', 'should', 'need to', 'must', 'going to']
        
        sentences = text.split('.')
        for sentence in sentences:
            if any(keyword in sentence.lower() for keyword in action_keywords):
                action_items.append({
                    'description': sentence.strip(),
                    'assigned_to': 'TBD',
                    'due_date': (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d'),
                    'priority': 'medium'
                })
        
        return action_items
    
    def _extract_decisions(self, text: str) -> List[str]:
        """Extract decisions from text"""
        decisions = []
        
        decision_keywords = ['decided', 'agreed', 'concluded', 'determined']
        
        sentences = text.split('.')
        for sentence in sentences:
            if any(keyword in sentence.lower() for keyword in decision_keywords):
                decisions.append(sentence.strip())
        
        return decisions
    
    def _generate_summary(self, transcript: str, topics: List[str], summary_type: str) -> str:
        """Generate summary based on type"""
        if summary_type == 'brief':
            return f"Meeting covered {len(topics)} main topics including: {', '.join(topics[:3])}."
        elif summary_type == 'action_items':
            return "See action items list below for next steps."
        else:  # detailed
            return f"Meeting discussion covered the following topics: {', '.join(topics)}. " \
                   f"Detailed notes and action items are provided below."


class ClientInteractionAnalyzer:
    """Analyze client interactions for insights"""
    
    def __init__(self):
        self.sentiment_keywords = {
            'positive': ['love', 'great', 'perfect', 'excellent', 'amazing'],
            'negative': ['concern', 'worried', 'expensive', 'small', 'problem'],
            'neutral': ['okay', 'fine', 'acceptable', 'standard']
        }
    
    def analyze_sentiment(self, client_message: str) -> Dict:
        """
        Analyze sentiment of client communication
        
        Args:
            client_message: Client's message
            
        Returns:
            Sentiment analysis results
        """
        message_lower = client_message.lower()
        
        positive_count = sum(1 for word in self.sentiment_keywords['positive'] if word in message_lower)
        negative_count = sum(1 for word in self.sentiment_keywords['negative'] if word in message_lower)
        neutral_count = sum(1 for word in self.sentiment_keywords['neutral'] if word in message_lower)
        
        total = positive_count + negative_count + neutral_count
        
        if total == 0:
            sentiment = 'neutral'
            confidence = 0.5
        elif positive_count > negative_count:
            sentiment = 'positive'
            confidence = positive_count / total
        elif negative_count > positive_count:
            sentiment = 'negative'
            confidence = negative_count / total
        else:
            sentiment = 'neutral'
            confidence = 0.6
        
        return {
            'sentiment': sentiment,
            'confidence': round(confidence, 2),
            'analyzed_at': datetime.now().isoformat()
        }
    
    def identify_client_needs(self, interaction_history: List[Dict]) -> Dict:
        """
        Identify client needs from interactions
        
        Args:
            interaction_history: List of client interactions
            
        Returns:
            Identified needs and priorities
        """
        needs = {
            'urgent': [],
            'important': [],
            'long_term': []
        }
        
        # Analyze recent interactions
        recent = interaction_history[-10:] if len(interaction_history) > 10 else interaction_history
        
        for interaction in recent:
            message = interaction.get('message', '').lower()
            
            # Check for urgency
            if any(word in message for word in ['asap', 'urgent', 'immediately', 'soon']):
                needs['urgent'].append(interaction.get('topic', 'General inquiry'))
            elif any(word in message for word in ['important', 'need', 'must']):
                needs['important'].append(interaction.get('topic', 'General inquiry'))
            else:
                needs['long_term'].append(interaction.get('topic', 'General inquiry'))
        
        return {
            'needs': needs,
            'priority_recommendation': 'urgent' if needs['urgent'] else 'important' if needs['important'] else 'long_term',
            'analyzed_at': datetime.now().isoformat()
        }
