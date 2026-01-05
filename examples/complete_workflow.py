"""
Example: Complete Property Brokerage AI Workflow

This example demonstrates a complete workflow using all AI modules:
1. Lead comes in through website
2. AI scores and prioritizes the lead
3. Chatbot engages with client
4. Property recommendations are generated
5. Content is created for marketing
6. Valuation is performed
7. All with ethical compliance checks
"""

from datetime import datetime
from src.ai_modules import (
    LeadScoringSystem,
    AIchatbot,
    PropertyRecommendationSystem,
    PropertyDescriptionGenerator,
    AutomatedValuationModel,
    FairHousingCompliance,
    TransparencyManager,
    SocialMediaContentGenerator
)


def main():
    print("=" * 80)
    print("AI-POWERED PROPERTY BROKERAGE WORKFLOW DEMO")
    print("=" * 80)
    print()
    
    # Initialize all systems
    lead_scorer = LeadScoringSystem()
    chatbot = AIchatbot()
    recommender = PropertyRecommendationSystem()
    content_gen = PropertyDescriptionGenerator()
    avm = AutomatedValuationModel()
    compliance = FairHousingCompliance()
    transparency = TransparencyManager()
    social_media = SocialMediaContentGenerator()
    
    # Step 1: New Lead Arrives
    print("STEP 1: NEW LEAD ARRIVES")
    print("-" * 40)
    lead_data = {
        'name': 'John Doe',
        'email': 'john@example.com',
        'page_views': 12,
        'time_on_site': 35,  # minutes
        'property_inquiries': 4,
        'contact_attempts': 2,
        'budget_match': 0.85,
        'timeline_weeks': 8
    }
    
    # Score the lead
    score = lead_scorer.score_lead(lead_data)
    analysis = lead_scorer.analyze_behavior(lead_data)
    
    print(f"Lead: {lead_data['name']}")
    print(f"Lead Score: {score}/100")
    print(f"Engagement Level: {analysis['engagement_level']}")
    print(f"Intent Score: {analysis['intent_score']}")
    print(f"Readiness: {analysis['readiness_score']}")
    print()
    
    # Step 2: AI Chatbot Engagement
    print("STEP 2: AI CHATBOT ENGAGEMENT")
    print("-" * 40)
    client_message = "Hi! I'm looking for a 3-bedroom house in downtown area with a budget around $500,000"
    bot_response = chatbot.get_response(client_message)
    print(f"Client: {client_message}")
    print(f"Bot: {bot_response}")
    print()
    
    # Step 3: Property Recommendations
    print("STEP 3: PROPERTY RECOMMENDATIONS")
    print("-" * 40)
    
    client_profile = {
        'client_id': 'CL001',
        'preferences': {
            'preferred_locations': ['downtown', 'midtown'],
            'price_range': {'min': 450000, 'max': 550000},
            'preferred_property_types': ['house', 'townhouse'],
            'must_have_amenities': ['garage', 'backyard'],
            'size_range': {'min': 1800, 'max': 2500}
        }
    }
    
    available_properties = [
        {
            'id': 'P001',
            'location': 'downtown',
            'price': 485000,
            'type': 'house',
            'square_footage': 2000,
            'bedrooms': 3,
            'bathrooms': 2,
            'amenities': ['garage', 'backyard', 'deck']
        },
        {
            'id': 'P002',
            'location': 'suburb',
            'price': 520000,
            'type': 'house',
            'square_footage': 2200,
            'bedrooms': 4,
            'bathrooms': 2.5,
            'amenities': ['garage', 'pool']
        }
    ]
    
    recommendations = recommender.recommend_properties(client_profile, available_properties, top_n=2)
    
    print(f"Top Recommendations for {lead_data['name']}:")
    for idx, rec in enumerate(recommendations, 1):
        prop = rec['property']
        print(f"\n{idx}. Property {prop['id']} - Match Score: {rec['match_score']:.2f}")
        print(f"   Location: {prop['location']} | Price: ${prop['price']:,}")
        print(f"   {prop['bedrooms']}BR / {prop['bathrooms']}BA | {prop['square_footage']} sqft")
        print(f"   Reasons: {', '.join(rec['match_reasons'])}")
    print()
    
    # Step 4: Property Valuation
    print("STEP 4: AUTOMATED PROPERTY VALUATION")
    print("-" * 40)
    
    property_to_value = {
        'square_footage': 2000,
        'bedrooms': 3,
        'bathrooms': 2,
        'age': 8,
        'location_score': 0.85,
        'condition_score': 0.9
    }
    
    valuation = avm.estimate_value(property_to_value)
    print(f"Property Valuation Results:")
    print(f"Estimated Value: ${valuation['estimated_value']:,.2f}")
    print(f"Range: ${valuation['lower_bound']:,.2f} - ${valuation['upper_bound']:,.2f}")
    print(f"Confidence Score: {valuation['confidence_score']:.2f}")
    print()
    
    # Step 5: Content Generation
    print("STEP 5: MARKETING CONTENT GENERATION")
    print("-" * 40)
    
    property_for_marketing = {
        'type': 'house',
        'bedrooms': 3,
        'bathrooms': 2,
        'square_footage': 2000,
        'location': 'downtown',
        'price': 485000,
        'features': ['Updated kitchen', 'Hardwood floors', 'Attached garage', 'Private backyard', 'Near schools']
    }
    
    # Generate description
    description = content_gen.generate_description(property_for_marketing, style='professional')
    print("Property Description:")
    print(description['description'])
    print()
    
    # Generate headline
    headline = content_gen.generate_headline(property_for_marketing)
    print(f"Headline: {headline}")
    print()
    
    # Step 6: Fair Housing Compliance Check
    print("STEP 6: FAIR HOUSING COMPLIANCE CHECK")
    print("-" * 40)
    
    compliance_result = compliance.check_content(description['description'])
    print(f"Compliance Status: {'✓ COMPLIANT' if compliance_result['compliant'] else '✗ NON-COMPLIANT'}")
    
    if compliance_result['violations']:
        print("Violations Found:")
        for violation in compliance_result['violations']:
            print(f"  - {violation['term']}: {violation['issue']}")
    
    if compliance_result['warnings']:
        print("Warnings:")
        for warning in compliance_result['warnings']:
            print(f"  - {warning['term']}: {warning['issue']}")
    
    print(f"Recommendation: {compliance_result['recommendation']}")
    print()
    
    # Step 7: Add Transparency Disclosures
    print("STEP 7: TRANSPARENCY DISCLOSURES")
    print("-" * 40)
    
    description_with_disclosure = transparency.add_disclosure(
        description['description'],
        'ai_generated_content'
    )
    
    print("Description with Disclosure:")
    print(description_with_disclosure)
    print()
    
    # Step 8: Social Media Campaign
    print("STEP 8: SOCIAL MEDIA CAMPAIGN GENERATION")
    print("-" * 40)
    
    social_posts = social_media.generate_campaign(property_for_marketing)
    
    for post in social_posts:
        print(f"\n{post['platform'].upper()}:")
        print(post['post_text'])
        print()
    
    # Summary
    print("=" * 80)
    print("WORKFLOW COMPLETE")
    print("=" * 80)
    print(f"✓ Lead scored and prioritized: {score}/100")
    print(f"✓ Client engaged via chatbot")
    print(f"✓ {len(recommendations)} properties recommended")
    print(f"✓ Property valued at ${valuation['estimated_value']:,.2f}")
    print(f"✓ Marketing content generated")
    print(f"✓ Fair Housing compliance verified")
    print(f"✓ Transparency disclosures added")
    print(f"✓ Social media campaign created for {len(social_posts)} platforms")
    print()
    print("All AI systems working in harmony to support the broker!")
    print("=" * 80)


if __name__ == "__main__":
    main()
