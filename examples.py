"""
Examples and Use Cases
AI-Powered Property Brokerage System

This file contains practical examples and use cases demonstrating
how to use the system in real-world scenarios.
"""

from app import PropertyBrokerageAI
from datetime import datetime

# Initialize the system
system = PropertyBrokerageAI()

print("="*70)
print("AI-POWERED PROPERTY BROKERAGE SYSTEM - EXAMPLES")
print("="*70)

# =============================================================================
# Example 1: Complete Lead Processing Workflow
# =============================================================================

print("\n" + "="*70)
print("EXAMPLE 1: Complete Lead Processing Workflow")
print("="*70)

# New lead comes in from website form
new_lead = {
    'id': 'LEAD-2024-001',
    'name': 'Sarah Johnson',
    'email': 'sarah.johnson@email.com',
    'phone': '+1-555-0123',
    'budget': 750000,
    'urgency': 'high',
    'preferred_location': 'Downtown',
    'bedrooms_min': 3,
    'bathrooms_min': 2,
    'must_have_features': ['garage', 'backyard', 'modern kitchen'],
    'previous_inquiries': 0,
    'type': 'buyer'
}

print("\n1. Processing new lead...")
result = system.process_new_lead(new_lead)

print(f"\nLead Name: {new_lead['name']}")
print(f"Lead Score: {result['lead_analysis']['score']}/100")
print(f"Priority: {result['lead_analysis']['priority']}")
print(f"\nKey Insights:")
for insight in result['lead_analysis']['insights']:
    print(f"  • {insight}")

print(f"\nRecommended Actions:")
for action in result['lead_analysis']['recommended_actions']:
    print(f"  • {action}")

print(f"\n2. Personalized message generated:")
print("-" * 70)
print(result['personalized_message'])
print("-" * 70)

# =============================================================================
# Example 2: Property Listing Workflow
# =============================================================================

print("\n" + "="*70)
print("EXAMPLE 2: Complete Property Listing Workflow")
print("="*70)

# Property owner wants to list their property
property_to_list = {
    'id': 'PROP-2024-001',
    'address': '456 Oak Avenue, Downtown',
    'bedrooms': 4,
    'bathrooms': 3,
    'size_sqft': 2500,
    'price': 725000,
    'location': 'Downtown',
    'type': 'house',
    'age_years': 8,
    'location_score': 9,
    'condition': 'excellent',
    'features': [
        'Two-car garage',
        'Modern kitchen with granite countertops',
        'Hardwood floors throughout',
        'Large backyard with deck',
        'Master suite with walk-in closet',
        'Energy-efficient appliances'
    ]
}

seller_info = {
    'name': 'Michael Brown',
    'email': 'michael.brown@email.com',
    'phone': '+1-555-0456',
    'address': '456 Oak Avenue, Downtown'
}

print("\n1. Creating complete listing package...")
listing = system.list_property(property_to_list, seller_info)

print(f"\nProperty: {property_to_list['address']}")
print(f"Estimated Value: ${listing['valuation']['estimated_value']:,.2f}")
print(f"Value Range: ${listing['valuation']['value_range']['lower']:,.2f} - ${listing['valuation']['value_range']['upper']:,.2f}")
print(f"Price per sqft: ${listing['valuation']['price_per_sqft']:.2f}")

print(f"\nComparable Market Analysis:")
print(f"  Market Average: ${listing['cma_report']['market_statistics']['avg_sold_price']:,.2f}")
print(f"  Suggested List Price: ${listing['cma_report']['pricing_recommendation']['suggested_list_price']:,.2f}")
print(f"  Strategy: {listing['cma_report']['pricing_recommendation']['pricing_strategy']}")

print(f"\n2. Marketing content generated:")
print("-" * 70)
print(listing['marketing']['description'][:500] + "...")
print("-" * 70)

print(f"\n3. Social media posts ready for:")
for platform in listing['marketing']['social_media'].keys():
    print(f"  • {platform.capitalize()}")

print(f"\n4. Transaction workflow created:")
print(f"  Total tasks: {len(listing['workflow']['tasks'])}")
print(f"  Current stage: {listing['workflow']['current_stage']}")

print(f"\n5. Maintenance schedule established:")
print(f"  Annual budget: ${listing['maintenance_schedule']['annual_maintenance_budget']:,.2f}")
print(f"  Scheduled tasks: {len(listing['maintenance_schedule']['tasks'])}")

# =============================================================================
# Example 3: Market Analysis for Investment Decision
# =============================================================================

print("\n" + "="*70)
print("EXAMPLE 3: Market Analysis for Investment Decision")
print("="*70)

print("\nAnalyzing different locations for investment opportunity...")

locations = ['Downtown', 'Suburbs', 'Waterfront']
comparisons = []

for location in locations:
    analysis = system.analyze_market(location, 'residential')
    comparisons.append({
        'location': location,
        'analysis': analysis
    })
    
    print(f"\n{location}:")
    print(f"  Market Temperature: {analysis['market_temperature']}")
    print(f"  Trend: {analysis['trend_direction']}")
    print(f"  Price Change: {analysis['avg_price_change_percent']}%")
    print(f"  Demand: {analysis['demand_level']}")

print("\nKey Insights for Best Investment Location:")
best_location = comparisons[0]
for insight in best_location['analysis']['key_insights']:
    print(f"  • {insight}")

# =============================================================================
# Example 4: Client Property Matching
# =============================================================================

print("\n" + "="*70)
print("EXAMPLE 4: AI-Powered Property Matching for Client")
print("="*70)

# Available properties in the system
available_properties = [
    {
        'id': 'PROP-001',
        'price': 725000,
        'location': 'Downtown',
        'bedrooms': 4,
        'bathrooms': 3,
        'size_sqft': 2500,
        'features': ['garage', 'backyard', 'modern kitchen', 'hardwood floors']
    },
    {
        'id': 'PROP-002',
        'price': 680000,
        'location': 'Downtown',
        'bedrooms': 3,
        'bathrooms': 2,
        'size_sqft': 2000,
        'features': ['garage', 'modern kitchen', 'renovated bathroom']
    },
    {
        'id': 'PROP-003',
        'price': 950000,
        'location': 'Waterfront',
        'bedrooms': 4,
        'bathrooms': 3,
        'size_sqft': 3000,
        'features': ['pool', 'ocean view', 'modern kitchen', 'luxury finishes']
    },
    {
        'id': 'PROP-004',
        'price': 650000,
        'location': 'Suburbs',
        'bedrooms': 3,
        'bathrooms': 2,
        'size_sqft': 1800,
        'features': ['garage', 'backyard', 'family room']
    }
]

# First, create a client profile if not exists
if 'CLIENT-001' not in system.client_profile_manager.client_profiles:
    system.client_profile_manager.create_client_profile(new_lead)

print("\nFinding best property matches for Sarah Johnson...")
recommendations = system.find_properties_for_client('CLIENT-001', available_properties)

print(f"\nTotal Recommendations: {recommendations['total_recommendations']}")
print(f"\nClient Insights:")
print(f"  Buying Probability: {recommendations['client_insights']['buying_probability']}")
print(f"  Urgency Level: {recommendations['client_insights']['urgency_level']}")

print(f"\nTop 3 Property Matches:")
for i, rec in enumerate(recommendations['recommendations'][:3], 1):
    prop = rec['property']
    print(f"\n{i}. Property {prop['id']} - Match Score: {rec['match_score']:.1f}/100")
    print(f"   Price: ${prop['price']:,}")
    print(f"   Location: {prop['location']}")
    print(f"   Specs: {prop['bedrooms']}BR / {prop['bathrooms']}BA / {prop['size_sqft']} sqft")
    print(f"   Why it matches:")
    for reason in rec['match_reasons']:
        print(f"     • {reason}")

# =============================================================================
# Example 5: Virtual Assistant Conversation
# =============================================================================

print("\n" + "="*70)
print("EXAMPLE 5: AI Virtual Assistant Conversation")
print("="*70)

conversation = [
    "Hi, I'm looking for a house in Downtown",
    "What's the price range for properties there?",
    "Can I schedule a viewing for next week?",
    "Tell me more about property PROP-001"
]

print("\nSimulating client conversation with AI assistant:\n")

for message in conversation:
    print(f"Client: {message}")
    response = system.chat_with_client('CLIENT-001', message)
    print(f"Assistant: {response['text'][:200]}...")
    print(f"[Intent: {response['intent']}]\n")

# =============================================================================
# Example 6: Property Maintenance Planning
# =============================================================================

print("\n" + "="*70)
print("EXAMPLE 6: Predictive Property Maintenance")
print("="*70)

# Property that needs maintenance planning
property_for_maintenance = {
    'id': 'PROP-MAINT-001',
    'age_years': 12,
    'type': 'residential',
    'size_sqft': 2200
}

print("\nCreating maintenance schedule for 12-year-old property...")
schedule = system.maintenance_manager.create_maintenance_schedule(property_for_maintenance)

print(f"\nProperty: {schedule['property_id']}")
print(f"Annual Maintenance Budget: ${schedule['annual_maintenance_budget']:,.2f}")
print(f"Total Scheduled Tasks: {len(schedule['tasks'])}")

print(f"\nUpcoming High-Priority Maintenance Tasks:")
high_priority = [task for task in schedule['tasks'] if task['priority'] == 'high']
for task in high_priority[:5]:
    print(f"\n  • {task['name']}")
    print(f"    Category: {task['category']}")
    print(f"    Frequency: {task['frequency']}")
    print(f"    Estimated Cost: ${task['estimated_cost']}")
    print(f"    Next Due: {task['next_due_date']}")

# Check upcoming maintenance
print("\n" + "-"*70)
print("Maintenance Due in Next 6 Months:")
print("-"*70)

upcoming = system.maintenance_manager.predict_upcoming_maintenance('PROP-MAINT-001', 6)
for task in upcoming[:5]:
    print(f"\n  • {task['task_name']}")
    print(f"    Due in: {task['days_until_due']} days")
    print(f"    Cost: ${task['estimated_cost']}")
    print(f"    Urgency: {task['urgency']}")

# =============================================================================
# Example 7: Marketing Campaign Creation
# =============================================================================

print("\n" + "="*70)
print("EXAMPLE 7: Multi-Channel Marketing Campaign")
print("="*70)

campaign_property = {
    'id': 'PROP-CAMPAIGN-001',
    'address': '789 Maple Street',
    'bedrooms': 3,
    'bathrooms': 2,
    'size_sqft': 1900,
    'price': 585000,
    'location': 'Suburbs',
    'type': 'house'
}

print("\nCreating comprehensive marketing campaign...")
campaign = system.create_marketing_campaign(
    'New Listing Launch',
    campaign_property,
    ['email', 'social_media', 'seo']
)

print(f"\nCampaign: {campaign['name']}")
print(f"Property: {campaign['property_id']}")
print(f"Start Date: {campaign['start_date']}")
print(f"Duration: {campaign['duration_days']} days")
print(f"Status: {campaign['status']}")

print(f"\nMarketing Channels:")
for channel in campaign['channels']:
    print(f"  • {channel.replace('_', ' ').title()}")

if 'email' in campaign['content']:
    print(f"\nEmail Campaign:")
    print(f"  Subject: {campaign['content']['email']['subject']}")
    print(f"  CTA: {campaign['content']['email']['cta_button']}")

if 'social_media' in campaign['content']:
    print(f"\nSocial Media Posts Generated:")
    for platform in campaign['content']['social_media'].keys():
        print(f"  • {platform.capitalize()}")

if 'seo' in campaign['content']:
    print(f"\nSEO Optimization:")
    print(f"  Title: {campaign['content']['seo']['title']}")
    print(f"  Keywords: {', '.join(campaign['content']['seo']['keywords'][:5])}")

# =============================================================================
# Example 8: Property Condition Assessment
# =============================================================================

print("\n" + "="*70)
print("EXAMPLE 8: AI Property Condition Assessment")
print("="*70)

# Inspection data from property inspection
inspection_data = {
    'structural_integrity': 7,
    'systems_functionality': 8,
    'exterior_condition': 7,
    'interior_condition': 8,
    'reported_issues': [
        {
            'description': 'Minor leak in guest bathroom',
            'category': 'plumbing',
            'severity': 'medium'
        },
        {
            'description': 'HVAC system needs servicing',
            'category': 'HVAC',
            'severity': 'low'
        }
    ]
}

print("\nAssessing property condition from inspection data...")
assessment = system.condition_monitor.assess_property_condition(
    'PROP-CONDITION-001',
    inspection_data
)

print(f"\nProperty: {assessment['property_id']}")
print(f"Overall Condition Score: {assessment['overall_condition_score']:.1f}/10")
print(f"Condition Grade: {assessment['condition_grade']}")

print(f"\nComponent Scores:")
for component, score in assessment['component_scores'].items():
    print(f"  • {component.replace('_', ' ').title()}: {score}/10")

print(f"\nIdentified Issues: {len(assessment['identified_issues'])}")
for issue in assessment['identified_issues']:
    print(f"  • {issue['description']} (Severity: {issue['severity']})")

print(f"\nRecommendations:")
for rec in assessment['recommendations']:
    print(f"  • {rec}")

print(f"\nEstimated Repair Costs:")
print(f"  Total: ${assessment['estimated_repair_costs']['total_estimated_cost']:,}")
print(f"  Range: ${assessment['estimated_repair_costs']['cost_range']['minimum']:,} - ${assessment['estimated_repair_costs']['cost_range']['maximum']:,}")

# Get health score
health = system.condition_monitor.get_property_health_score('PROP-CONDITION-001')
print(f"\nProperty Health Score: {health['health_score']:.1f}/100")
print(f"Health Grade: {health['health_grade']}")
print(f"Maintenance Urgency: {health['maintenance_urgency']}")

# =============================================================================
# Summary
# =============================================================================

print("\n" + "="*70)
print("EXAMPLES SUMMARY")
print("="*70)

print("""
These examples demonstrate the key capabilities of the AI-Powered
Property Brokerage System:

1. ✓ Automated lead scoring and personalized communication
2. ✓ Complete property listing workflow with valuation
3. ✓ Market analysis for investment decisions
4. ✓ AI-powered property matching for clients
5. ✓ Virtual assistant for client interactions
6. ✓ Predictive property maintenance planning
7. ✓ Multi-channel marketing campaign creation
8. ✓ Property condition assessment and health scoring

All these features work together to create a comprehensive
AI-powered solution for modern property brokerage operations.
""")

print("="*70)
print("For more information, see API_DOCUMENTATION.md")
print("="*70)
