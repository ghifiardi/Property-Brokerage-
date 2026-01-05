"""
AI-Powered Property Brokerage System
Module 5: Personalized Client Experience

This module provides AI capabilities for:
- Client preference profiling
- Personalized property recommendations
- Chatbot and virtual assistant
- Sentiment analysis and feedback processing
- Client journey optimization
"""

from typing import List, Dict, Optional, Tuple
from datetime import datetime, timedelta
import json


class ClientProfileManager:
    """AI-powered client profiling and preference management"""
    
    def __init__(self):
        self.client_profiles = {}
    
    def create_client_profile(self, client_data: Dict) -> Dict:
        """
        Create a comprehensive client profile
        
        Args:
            client_data: Basic client information
            
        Returns:
            Complete client profile
        """
        profile = {
            'client_id': client_data.get('id', f"CLI-{datetime.now().timestamp()}"),
            'personal_info': {
                'name': client_data.get('name', ''),
                'email': client_data.get('email', ''),
                'phone': client_data.get('phone', ''),
                'type': client_data.get('type', 'buyer')  # buyer, seller, investor
            },
            'preferences': {
                'budget_min': client_data.get('budget_min', 0),
                'budget_max': client_data.get('budget_max', 0),
                'preferred_locations': client_data.get('preferred_locations', []),
                'property_type': client_data.get('property_type', 'any'),
                'bedrooms_min': client_data.get('bedrooms_min', 0),
                'bathrooms_min': client_data.get('bathrooms_min', 0),
                'must_have_features': client_data.get('must_have_features', []),
                'nice_to_have_features': client_data.get('nice_to_have_features', [])
            },
            'behavior': {
                'communication_preference': client_data.get('communication_preference', 'email'),
                'availability': client_data.get('availability', 'weekends'),
                'response_time_avg_hours': 24,
                'engagement_score': 50
            },
            'history': {
                'properties_viewed': [],
                'properties_saved': [],
                'searches_performed': [],
                'interactions': []
            },
            'ai_insights': {
                'buying_probability': 'medium',
                'urgency_level': 'medium',
                'price_sensitivity': 'medium',
                'decision_style': 'analytical'
            },
            'created_at': datetime.now().isoformat(),
            'last_updated': datetime.now().isoformat()
        }
        
        # Analyze and enhance profile
        profile = self._enhance_profile_with_ai(profile)
        
        self.client_profiles[profile['client_id']] = profile
        return profile
    
    def _enhance_profile_with_ai(self, profile: Dict) -> Dict:
        """Enhance profile with AI-generated insights"""
        # Analyze budget
        budget_range = profile['preferences']['budget_max'] - profile['preferences']['budget_min']
        if budget_range > 200000:
            profile['ai_insights']['price_sensitivity'] = 'low'
        elif budget_range < 50000:
            profile['ai_insights']['price_sensitivity'] = 'high'
        
        # Analyze preferences
        if len(profile['preferences']['must_have_features']) > 5:
            profile['ai_insights']['decision_style'] = 'detailed'
        
        return profile
    
    def update_profile_from_behavior(self, client_id: str, 
                                    action: str, data: Dict) -> Dict:
        """
        Update client profile based on behavior
        
        Args:
            client_id: Client identifier
            action: Action performed (viewed_property, saved_property, search, inquiry)
            data: Action details
            
        Returns:
            Updated profile
        """
        if client_id not in self.client_profiles:
            return {'error': 'Client not found'}
        
        profile = self.client_profiles[client_id]
        
        # Record action in history
        interaction = {
            'action': action,
            'timestamp': datetime.now().isoformat(),
            'data': data
        }
        profile['history']['interactions'].append(interaction)
        
        # Update based on action type
        if action == 'viewed_property':
            profile['history']['properties_viewed'].append(data.get('property_id'))
            self._update_preferences_from_view(profile, data)
        
        elif action == 'saved_property':
            profile['history']['properties_saved'].append(data.get('property_id'))
            profile['behavior']['engagement_score'] += 5
            self._update_preferences_from_save(profile, data)
        
        elif action == 'search':
            profile['history']['searches_performed'].append(data)
            self._update_preferences_from_search(profile, data)
        
        # Update engagement score
        total_interactions = len(profile['history']['interactions'])
        if total_interactions > 20:
            profile['behavior']['engagement_score'] = min(profile['behavior']['engagement_score'] + 2, 100)
        
        # Update AI insights
        profile = self._recalculate_ai_insights(profile)
        profile['last_updated'] = datetime.now().isoformat()
        
        return profile
    
    def _update_preferences_from_view(self, profile: Dict, data: Dict):
        """Update preferences based on property view"""
        viewed_location = data.get('location')
        if viewed_location and viewed_location not in profile['preferences']['preferred_locations']:
            profile['preferences']['preferred_locations'].append(viewed_location)
    
    def _update_preferences_from_save(self, profile: Dict, data: Dict):
        """Update preferences based on saved property"""
        # Properties saved indicate strong interest
        saved_features = data.get('features', [])
        for feature in saved_features:
            if feature not in profile['preferences']['must_have_features']:
                if feature not in profile['preferences']['nice_to_have_features']:
                    profile['preferences']['nice_to_have_features'].append(feature)
    
    def _update_preferences_from_search(self, profile: Dict, data: Dict):
        """Update preferences based on search patterns"""
        search_location = data.get('location')
        if search_location and search_location not in profile['preferences']['preferred_locations']:
            profile['preferences']['preferred_locations'].append(search_location)
    
    def _recalculate_ai_insights(self, profile: Dict) -> Dict:
        """Recalculate AI insights based on behavior"""
        # Calculate buying probability
        engagement = profile['behavior']['engagement_score']
        saved_count = len(profile['history']['properties_saved'])
        
        if engagement > 70 and saved_count > 3:
            profile['ai_insights']['buying_probability'] = 'high'
        elif engagement > 40 or saved_count > 1:
            profile['ai_insights']['buying_probability'] = 'medium'
        else:
            profile['ai_insights']['buying_probability'] = 'low'
        
        # Calculate urgency
        recent_interactions = [i for i in profile['history']['interactions'] 
                              if (datetime.now() - datetime.fromisoformat(i['timestamp'])).days < 7]
        
        if len(recent_interactions) > 10:
            profile['ai_insights']['urgency_level'] = 'high'
        elif len(recent_interactions) > 5:
            profile['ai_insights']['urgency_level'] = 'medium'
        else:
            profile['ai_insights']['urgency_level'] = 'low'
        
        return profile


class PropertyRecommendationEngine:
    """AI-powered personalized property recommendations"""
    
    def __init__(self):
        self.recommendation_history = {}
    
    def recommend_properties(self, client_profile: Dict, 
                           available_properties: List[Dict], 
                           max_recommendations: int = 10) -> List[Dict]:
        """
        Generate personalized property recommendations
        
        Args:
            client_profile: Client profile with preferences
            available_properties: List of available properties
            max_recommendations: Maximum number of recommendations
            
        Returns:
            Ranked list of recommended properties
        """
        recommendations = []
        
        for prop in available_properties:
            match_score = self._calculate_match_score(client_profile, prop)
            
            if match_score > 30:  # Minimum threshold
                recommendations.append({
                    'property': prop,
                    'match_score': match_score,
                    'match_reasons': self._get_match_reasons(client_profile, prop),
                    'recommended_at': datetime.now().isoformat()
                })
        
        # Sort by match score
        recommendations.sort(key=lambda x: x['match_score'], reverse=True)
        
        # Return top N recommendations
        return recommendations[:max_recommendations]
    
    def _calculate_match_score(self, profile: Dict, property: Dict) -> float:
        """Calculate how well a property matches client preferences"""
        score = 0.0
        preferences = profile.get('preferences', {})
        
        # Price match (30 points)
        price = property.get('price', 0)
        budget_min = preferences.get('budget_min', 0)
        budget_max = preferences.get('budget_max', float('inf'))
        
        if budget_min <= price <= budget_max:
            score += 30
        elif price < budget_min:
            diff_percent = (budget_min - price) / budget_min * 100
            score += max(0, 30 - diff_percent)
        else:
            diff_percent = (price - budget_max) / budget_max * 100
            score += max(0, 30 - diff_percent)
        
        # Location match (25 points)
        prop_location = property.get('location', '')
        preferred_locations = preferences.get('preferred_locations', [])
        
        if prop_location in preferred_locations:
            score += 25
        elif preferred_locations:
            # Partial match for nearby locations
            score += 10
        
        # Bedrooms match (15 points)
        prop_bedrooms = property.get('bedrooms', 0)
        min_bedrooms = preferences.get('bedrooms_min', 0)
        
        if prop_bedrooms >= min_bedrooms:
            score += 15
        elif prop_bedrooms == min_bedrooms - 1:
            score += 7
        
        # Bathrooms match (10 points)
        prop_bathrooms = property.get('bathrooms', 0)
        min_bathrooms = preferences.get('bathrooms_min', 0)
        
        if prop_bathrooms >= min_bathrooms:
            score += 10
        
        # Features match (20 points)
        prop_features = set(property.get('features', []))
        must_have = set(preferences.get('must_have_features', []))
        nice_to_have = set(preferences.get('nice_to_have_features', []))
        
        # Must-have features
        must_have_matches = len(must_have.intersection(prop_features))
        if must_have:
            score += (must_have_matches / len(must_have)) * 15
        
        # Nice-to-have features
        nice_to_have_matches = len(nice_to_have.intersection(prop_features))
        if nice_to_have:
            score += (nice_to_have_matches / len(nice_to_have)) * 5
        
        return round(score, 2)
    
    def _get_match_reasons(self, profile: Dict, property: Dict) -> List[str]:
        """Generate human-readable match reasons"""
        reasons = []
        preferences = profile.get('preferences', {})
        
        # Price reason
        price = property.get('price', 0)
        if preferences.get('budget_min', 0) <= price <= preferences.get('budget_max', float('inf')):
            reasons.append(f"Within your budget of ${preferences['budget_min']:,}-${preferences['budget_max']:,}")
        
        # Location reason
        if property.get('location') in preferences.get('preferred_locations', []):
            reasons.append(f"In your preferred location: {property['location']}")
        
        # Bedrooms reason
        if property.get('bedrooms', 0) >= preferences.get('bedrooms_min', 0):
            reasons.append(f"Has {property['bedrooms']} bedrooms as requested")
        
        # Features reason
        prop_features = set(property.get('features', []))
        must_have = set(preferences.get('must_have_features', []))
        matching_features = must_have.intersection(prop_features)
        
        if matching_features:
            reasons.append(f"Includes desired features: {', '.join(list(matching_features)[:3])}")
        
        return reasons


class VirtualAssistant:
    """AI-powered chatbot and virtual assistant"""
    
    def __init__(self):
        self.conversation_history = {}
        self.intents = {}
    
    def process_message(self, client_id: str, message: str, 
                       context: Dict = None) -> Dict:
        """
        Process client message and generate response
        
        Args:
            client_id: Client identifier
            message: User message
            context: Additional context
            
        Returns:
            Response with intent and actions
        """
        # Initialize conversation history for client
        if client_id not in self.conversation_history:
            self.conversation_history[client_id] = []
        
        # Detect intent
        intent = self._detect_intent(message)
        
        # Generate response based on intent
        response = self._generate_response(intent, message, context)
        
        # Store conversation
        self.conversation_history[client_id].append({
            'timestamp': datetime.now().isoformat(),
            'message': message,
            'intent': intent,
            'response': response['text']
        })
        
        return response
    
    def _detect_intent(self, message: str) -> str:
        """Detect user intent from message"""
        message_lower = message.lower()
        
        # Property search intent
        if any(word in message_lower for word in ['looking for', 'search', 'find', 'need', 'want']):
            if any(word in message_lower for word in ['house', 'home', 'property', 'apartment']):
                return 'property_search'
        
        # Pricing inquiry
        if any(word in message_lower for word in ['price', 'cost', 'expensive', 'afford', 'budget']):
            return 'pricing_inquiry'
        
        # Viewing request
        if any(word in message_lower for word in ['view', 'visit', 'see', 'tour', 'showing']):
            return 'viewing_request'
        
        # Property details
        if any(word in message_lower for word in ['details', 'information', 'tell me', 'about']):
            return 'property_details'
        
        # General inquiry
        if any(word in message_lower for word in ['how', 'what', 'when', 'where', 'why']):
            return 'general_inquiry'
        
        # Greeting
        if any(word in message_lower for word in ['hello', 'hi', 'hey', 'good morning', 'good afternoon']):
            return 'greeting'
        
        return 'unknown'
    
    def _generate_response(self, intent: str, message: str, 
                          context: Dict = None) -> Dict:
        """Generate appropriate response based on intent"""
        responses = {
            'greeting': {
                'text': "Hello! I'm your AI property assistant. How can I help you today? I can help you search for properties, schedule viewings, answer questions about listings, or provide market information.",
                'actions': ['show_search_options'],
                'quick_replies': ['Search properties', 'Schedule viewing', 'Market information']
            },
            'property_search': {
                'text': "I'd be happy to help you find the perfect property! Could you tell me more about what you're looking for? For example:\n• Your budget range\n• Preferred location\n• Number of bedrooms and bathrooms\n• Any specific features you need",
                'actions': ['initiate_search_wizard'],
                'quick_replies': ['Set budget', 'Choose location', 'Specify features']
            },
            'pricing_inquiry': {
                'text': "I can help you understand property pricing. Properties in our listings range from affordable options to luxury estates. What's your budget range? I can show you what's available and help you understand market values.",
                'actions': ['show_price_ranges'],
                'quick_replies': ['Under $300k', '$300k-$500k', '$500k-$1M', 'Over $1M']
            },
            'viewing_request': {
                'text': "Great! I can help you schedule a property viewing. Which property would you like to see? Please provide the property ID or address, and I'll check availability and schedule a convenient time for you.",
                'actions': ['initiate_viewing_scheduler'],
                'quick_replies': ['Morning slots', 'Afternoon slots', 'Weekend viewing']
            },
            'property_details': {
                'text': "I'd be happy to provide detailed information about any property. Please share the property ID or address, and I'll give you comprehensive details including photos, features, pricing, and neighborhood information.",
                'actions': ['fetch_property_details'],
                'quick_replies': ['View photos', 'Check features', 'See location']
            },
            'general_inquiry': {
                'text': "I'm here to help! I can assist with:\n• Finding properties that match your needs\n• Scheduling property viewings\n• Providing market insights\n• Answering questions about listings\n• Guiding you through the buying/selling process\n\nWhat would you like to know more about?",
                'actions': ['show_help_menu'],
                'quick_replies': ['Buying process', 'Selling process', 'Market trends']
            },
            'unknown': {
                'text': "I want to make sure I understand your question correctly. Could you please rephrase or tell me if you're interested in:\n• Searching for properties\n• Scheduling a viewing\n• Getting property information\n• Learning about the market",
                'actions': ['request_clarification'],
                'quick_replies': ['Search properties', 'Schedule viewing', 'Get info']
            }
        }
        
        response = responses.get(intent, responses['unknown'])
        response['intent'] = intent
        response['timestamp'] = datetime.now().isoformat()
        
        return response
    
    def get_conversation_summary(self, client_id: str) -> Dict:
        """
        Get conversation summary for a client
        
        Args:
            client_id: Client identifier
            
        Returns:
            Conversation summary with insights
        """
        if client_id not in self.conversation_history:
            return {'error': 'No conversation history found'}
        
        history = self.conversation_history[client_id]
        
        # Analyze intents
        intent_counts = {}
        for conv in history:
            intent = conv['intent']
            intent_counts[intent] = intent_counts.get(intent, 0) + 1
        
        # Identify main interests
        main_intent = max(intent_counts.items(), key=lambda x: x[1])[0] if intent_counts else 'unknown'
        
        return {
            'client_id': client_id,
            'total_messages': len(history),
            'intent_distribution': intent_counts,
            'main_interest': main_intent,
            'first_interaction': history[0]['timestamp'] if history else None,
            'last_interaction': history[-1]['timestamp'] if history else None,
            'engagement_level': 'high' if len(history) > 10 else 'medium' if len(history) > 5 else 'low'
        }


class SentimentAnalyzer:
    """AI-powered sentiment analysis for client feedback"""
    
    def __init__(self):
        self.feedback_history = []
    
    def analyze_feedback(self, feedback_text: str, source: str = 'general') -> Dict:
        """
        Analyze client feedback sentiment
        
        Args:
            feedback_text: Feedback text to analyze
            source: Source of feedback (review, survey, message, etc.)
            
        Returns:
            Sentiment analysis results
        """
        # Simple keyword-based sentiment analysis
        positive_keywords = [
            'great', 'excellent', 'amazing', 'wonderful', 'fantastic', 'love',
            'perfect', 'best', 'helpful', 'professional', 'satisfied', 'happy'
        ]
        
        negative_keywords = [
            'bad', 'terrible', 'awful', 'poor', 'disappointed', 'unhappy',
            'worst', 'unprofessional', 'frustrated', 'angry', 'horrible'
        ]
        
        neutral_keywords = [
            'okay', 'fine', 'average', 'normal', 'standard', 'acceptable'
        ]
        
        text_lower = feedback_text.lower()
        
        # Count sentiment indicators
        positive_count = sum(1 for word in positive_keywords if word in text_lower)
        negative_count = sum(1 for word in negative_keywords if word in text_lower)
        neutral_count = sum(1 for word in neutral_keywords if text_lower)
        
        # Determine overall sentiment
        if positive_count > negative_count and positive_count > neutral_count:
            sentiment = 'positive'
            confidence = min(0.95, 0.6 + (positive_count * 0.1))
        elif negative_count > positive_count and negative_count > neutral_count:
            sentiment = 'negative'
            confidence = min(0.95, 0.6 + (negative_count * 0.1))
        elif neutral_count > 0:
            sentiment = 'neutral'
            confidence = 0.7
        else:
            sentiment = 'neutral'
            confidence = 0.5
        
        # Extract key topics (simplified)
        topics = []
        if 'property' in text_lower or 'house' in text_lower:
            topics.append('property_quality')
        if 'agent' in text_lower or 'broker' in text_lower or 'service' in text_lower:
            topics.append('service_quality')
        if 'price' in text_lower or 'cost' in text_lower:
            topics.append('pricing')
        if 'process' in text_lower or 'transaction' in text_lower:
            topics.append('transaction_process')
        
        analysis = {
            'feedback_text': feedback_text,
            'sentiment': sentiment,
            'confidence': round(confidence, 2),
            'sentiment_score': self._calculate_sentiment_score(sentiment, confidence),
            'topics': topics,
            'source': source,
            'analyzed_at': datetime.now().isoformat(),
            'action_required': sentiment == 'negative',
            'priority': 'high' if sentiment == 'negative' else 'medium' if sentiment == 'neutral' else 'low'
        }
        
        self.feedback_history.append(analysis)
        return analysis
    
    def _calculate_sentiment_score(self, sentiment: str, confidence: float) -> float:
        """Calculate numerical sentiment score (-1 to 1)"""
        base_scores = {
            'positive': 1.0,
            'neutral': 0.0,
            'negative': -1.0
        }
        
        return base_scores.get(sentiment, 0.0) * confidence
    
    def get_sentiment_trends(self, time_period_days: int = 30) -> Dict:
        """
        Analyze sentiment trends over time
        
        Args:
            time_period_days: Time period to analyze
            
        Returns:
            Sentiment trend analysis
        """
        cutoff_date = datetime.now() - timedelta(days=time_period_days)
        
        recent_feedback = [
            f for f in self.feedback_history
            if datetime.fromisoformat(f['analyzed_at']) > cutoff_date
        ]
        
        if not recent_feedback:
            return {'error': 'No feedback in specified time period'}
        
        # Calculate statistics
        sentiment_counts = {'positive': 0, 'neutral': 0, 'negative': 0}
        total_score = 0
        
        for feedback in recent_feedback:
            sentiment_counts[feedback['sentiment']] += 1
            total_score += feedback['sentiment_score']
        
        total_feedback = len(recent_feedback)
        avg_score = total_score / total_feedback if total_feedback > 0 else 0
        
        return {
            'time_period_days': time_period_days,
            'total_feedback': total_feedback,
            'sentiment_distribution': {
                'positive': sentiment_counts['positive'],
                'neutral': sentiment_counts['neutral'],
                'negative': sentiment_counts['negative']
            },
            'sentiment_percentages': {
                'positive': round(sentiment_counts['positive'] / total_feedback * 100, 1),
                'neutral': round(sentiment_counts['neutral'] / total_feedback * 100, 1),
                'negative': round(sentiment_counts['negative'] / total_feedback * 100, 1)
            },
            'average_sentiment_score': round(avg_score, 2),
            'overall_trend': 'positive' if avg_score > 0.3 else 'negative' if avg_score < -0.3 else 'neutral'
        }


# Example usage and demonstration
if __name__ == "__main__":
    # Client Profile Management
    print("=== Client Profile Management ===")
    profile_mgr = ClientProfileManager()
    
    client_data = {
        'id': 'CLIENT-001',
        'name': 'Jane Buyer',
        'email': 'jane@example.com',
        'phone': '+1234567890',
        'type': 'buyer',
        'budget_min': 400000,
        'budget_max': 550000,
        'preferred_locations': ['Downtown', 'Suburbs'],
        'bedrooms_min': 3,
        'bathrooms_min': 2,
        'must_have_features': ['garage', 'backyard', 'modern kitchen']
    }
    
    profile = profile_mgr.create_client_profile(client_data)
    print(f"Created profile for: {profile['personal_info']['name']}")
    print(f"Buying Probability: {profile['ai_insights']['buying_probability']}")
    print(f"Urgency Level: {profile['ai_insights']['urgency_level']}")
    
    # Property Recommendations
    print("\n=== Property Recommendations ===")
    rec_engine = PropertyRecommendationEngine()
    
    sample_properties = [
        {
            'id': 'PROP-001',
            'price': 475000,
            'location': 'Downtown',
            'bedrooms': 3,
            'bathrooms': 2,
            'features': ['garage', 'backyard', 'modern kitchen', 'hardwood floors']
        },
        {
            'id': 'PROP-002',
            'price': 525000,
            'location': 'Waterfront',
            'bedrooms': 4,
            'bathrooms': 3,
            'features': ['pool', 'ocean view', 'modern kitchen']
        }
    ]
    
    recommendations = rec_engine.recommend_properties(profile, sample_properties, 5)
    
    for rec in recommendations:
        print(f"\nProperty: {rec['property']['id']}")
        print(f"Match Score: {rec['match_score']:.1f}/100")
        print(f"Reasons:")
        for reason in rec['match_reasons']:
            print(f"  - {reason}")
    
    # Virtual Assistant
    print("\n=== Virtual Assistant Demo ===")
    assistant = VirtualAssistant()
    
    test_messages = [
        "Hi, I'm looking for a house",
        "What's the price range?",
        "I'd like to schedule a viewing"
    ]
    
    for msg in test_messages:
        print(f"\nUser: {msg}")
        response = assistant.process_message('CLIENT-001', msg)
        print(f"Assistant: {response['text'][:150]}...")
        print(f"Intent: {response['intent']}")
    
    # Sentiment Analysis
    print("\n=== Sentiment Analysis ===")
    sentiment = SentimentAnalyzer()
    
    feedback_samples = [
        "The agent was excellent and helped us find the perfect home!",
        "The process was okay, nothing special",
        "Very disappointed with the service and communication"
    ]
    
    for feedback in feedback_samples:
        analysis = sentiment.analyze_feedback(feedback)
        print(f"\nFeedback: {feedback[:50]}...")
        print(f"Sentiment: {analysis['sentiment']} (confidence: {analysis['confidence']})")
        print(f"Priority: {analysis['priority']}")
