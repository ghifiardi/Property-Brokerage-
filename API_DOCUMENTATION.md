# API Documentation

## AI-Powered Property Brokerage System API Reference

This document provides detailed information about the APIs and methods available in the system.

---

## Table of Contents

1. [Lead Generation Module](#lead-generation-module)
2. [Market Analysis Module](#market-analysis-module)
3. [Content Marketing Module](#content-marketing-module)
4. [Workflow Automation Module](#workflow-automation-module)
5. [Client Experience Module](#client-experience-module)
6. [Property Operations Module](#property-operations-module)
7. [Main Application](#main-application)

---

## Lead Generation Module

### LeadGenerator

#### `analyze_lead(lead_data: Dict) -> Dict`
Analyze and score a lead using AI algorithms.

**Parameters:**
- `lead_data`: Dictionary containing lead information
  - `id`: Unique lead identifier
  - `name`: Lead name
  - `email`: Email address
  - `phone`: Phone number
  - `budget`: Budget amount
  - `urgency`: Urgency level ('high', 'medium', 'low')
  - `preferred_location`: Preferred location
  - `previous_inquiries`: Number of previous inquiries

**Returns:**
- Dictionary with:
  - `lead_id`: Lead identifier
  - `score`: Score out of 100
  - `priority`: Priority level ('HIGH', 'MEDIUM', 'LOW')
  - `insights`: List of insights
  - `recommended_actions`: List of recommended actions
  - `analyzed_at`: Analysis timestamp

**Example:**
```python
lead_gen = LeadGenerator()
result = lead_gen.analyze_lead({
    'id': 'LEAD-001',
    'name': 'John Doe',
    'email': 'john@example.com',
    'budget': 500000,
    'urgency': 'high'
})
print(f"Score: {result['score']}/100")
```

#### `generate_personalized_message(lead_data: Dict, message_type: str) -> str`
Generate personalized communication for leads.

**Parameters:**
- `lead_data`: Lead information
- `message_type`: Type of message ('initial', 'follow_up', 'property_match')

**Returns:**
- Personalized message string

**Example:**
```python
message = lead_gen.generate_personalized_message(
    lead_data,
    'initial'
)
```

#### `batch_score_leads(leads: List[Dict]) -> List[Dict]`
Score multiple leads in batch.

**Parameters:**
- `leads`: List of lead dictionaries

**Returns:**
- List of analyzed leads with scores

### LeadNurturingEngine

#### `create_nurture_campaign(campaign_name: str, campaign_config: Dict) -> Dict`
Create an automated nurture campaign.

**Parameters:**
- `campaign_name`: Name of the campaign
- `campaign_config`: Configuration including schedule and content

**Returns:**
- Campaign details dictionary

---

## Market Analysis Module

### MarketAnalyzer

#### `analyze_market_trends(location: str, property_type: str, time_period_days: int = 90) -> Dict`
Analyze market trends for a specific location and property type.

**Parameters:**
- `location`: Geographic location to analyze
- `property_type`: Type of property (residential, commercial, etc.)
- `time_period_days`: Number of days to analyze (default: 90)

**Returns:**
- Market analysis report with:
  - `location`: Location analyzed
  - `trend_direction`: 'upward', 'downward', or 'stable'
  - `avg_price_change_percent`: Price change percentage
  - `demand_level`: 'high', 'medium', or 'low'
  - `market_temperature`: Market temperature description
  - `key_insights`: List of actionable insights
  - `forecast`: Short-term forecast

**Example:**
```python
analyzer = MarketAnalyzer()
analysis = analyzer.analyze_market_trends('Downtown', 'residential')
print(f"Market: {analysis['market_temperature']}")
```

#### `compare_locations(locations: List[str], property_type: str) -> List[Dict]`
Compare multiple locations for market performance.

**Parameters:**
- `locations`: List of locations to compare
- `property_type`: Type of property

**Returns:**
- Comparative analysis of locations sorted by market score

### PropertyValuationEngine

#### `estimate_property_value(property_data: Dict) -> Dict`
Estimate property value using AI/ML algorithms.

**Parameters:**
- `property_data`: Property characteristics
  - `id`: Property ID
  - `size_sqft`: Size in square feet
  - `bedrooms`: Number of bedrooms
  - `bathrooms`: Number of bathrooms
  - `age_years`: Property age in years
  - `location_score`: Location rating (1-10)
  - `condition`: 'poor', 'fair', 'good', or 'excellent'

**Returns:**
- Valuation estimate with:
  - `estimated_value`: Estimated value
  - `value_range`: Lower and upper bounds
  - `price_per_sqft`: Price per square foot
  - `confidence_score`: Confidence level (0-1)
  - `valuation_factors`: Impact factors

**Example:**
```python
valuator = PropertyValuationEngine()
valuation = valuator.estimate_property_value({
    'id': 'PROP-001',
    'size_sqft': 2000,
    'bedrooms': 3,
    'bathrooms': 2,
    'age_years': 10,
    'location_score': 8,
    'condition': 'good'
})
print(f"Value: ${valuation['estimated_value']:,.2f}")
```

#### `perform_cma(subject_property: Dict, radius_miles: float = 2.0) -> Dict`
Perform Comparative Market Analysis.

**Parameters:**
- `subject_property`: Property to analyze
- `radius_miles`: Search radius for comparable properties

**Returns:**
- CMA report with comparable properties and pricing recommendations

---

## Content Marketing Module

### ContentGenerator

#### `generate_property_description(property_data: Dict, style: str = "professional") -> str`
Generate compelling property description.

**Parameters:**
- `property_data`: Property details
- `style`: Writing style ('professional', 'luxury', 'casual', 'urgent')

**Returns:**
- Generated property description string

**Example:**
```python
generator = ContentGenerator()
description = generator.generate_property_description(
    property_data,
    'professional'
)
```

#### `generate_social_media_posts(property_data: Dict, platforms: List[str]) -> Dict[str, str]`
Generate platform-specific social media content.

**Parameters:**
- `property_data`: Property details
- `platforms`: List of platforms ('facebook', 'instagram', 'twitter', 'linkedin')

**Returns:**
- Dictionary of platform-specific posts

#### `generate_email_campaign(campaign_type: str, property_data: Dict = None) -> Dict`
Generate email marketing campaigns.

**Parameters:**
- `campaign_type`: Type of campaign ('new_listing', 'open_house', 'price_reduction', 'newsletter')
- `property_data`: Property details if applicable

**Returns:**
- Email campaign with subject and body

#### `generate_seo_content(property_data: Dict) -> Dict`
Generate SEO-optimized content for property listings.

**Parameters:**
- `property_data`: Property details

**Returns:**
- SEO-optimized content with metadata

### MarketingCampaignManager

#### `create_campaign(campaign_name: str, property_data: Dict, channels: List[str], duration_days: int = 30) -> Dict`
Create a comprehensive marketing campaign.

**Parameters:**
- `campaign_name`: Name of the campaign
- `property_data`: Property details
- `channels`: Marketing channels to use
- `duration_days`: Campaign duration (default: 30)

**Returns:**
- Campaign details and schedule

---

## Workflow Automation Module

### DocumentProcessor

#### `generate_listing_agreement(property_data: Dict, seller_data: Dict) -> Dict`
Generate a listing agreement document.

**Parameters:**
- `property_data`: Property details
- `seller_data`: Seller information

**Returns:**
- Generated listing agreement

#### `generate_purchase_agreement(property_data: Dict, buyer_data: Dict, seller_data: Dict, offer_details: Dict) -> Dict`
Generate a purchase agreement document.

**Parameters:**
- `property_data`: Property details
- `buyer_data`: Buyer information
- `seller_data`: Seller information
- `offer_details`: Offer terms

**Returns:**
- Generated purchase agreement

### WorkflowAutomation

#### `create_transaction_workflow(transaction_id: str, transaction_type: str) -> Dict`
Create an automated workflow for a property transaction.

**Parameters:**
- `transaction_id`: Unique transaction identifier
- `transaction_type`: Type of transaction ('listing', 'purchase', 'lease')

**Returns:**
- Workflow details with tasks

#### `update_task_status(transaction_id: str, task_id: int, new_status: str) -> Dict`
Update task status and trigger automation if needed.

**Parameters:**
- `transaction_id`: Transaction identifier
- `task_id`: Task identifier
- `new_status`: New status ('pending', 'in_progress', 'completed', 'blocked')

**Returns:**
- Updated workflow

### ComplianceChecker

#### `check_document_compliance(document: Dict, jurisdiction: str = "US") -> Dict`
Check document for regulatory compliance.

**Parameters:**
- `document`: Document to check
- `jurisdiction`: Legal jurisdiction (default: "US")

**Returns:**
- Compliance report with score and recommendations

---

## Client Experience Module

### ClientProfileManager

#### `create_client_profile(client_data: Dict) -> Dict`
Create a comprehensive client profile.

**Parameters:**
- `client_data`: Basic client information

**Returns:**
- Complete client profile with AI insights

#### `update_profile_from_behavior(client_id: str, action: str, data: Dict) -> Dict`
Update client profile based on behavior.

**Parameters:**
- `client_id`: Client identifier
- `action`: Action performed ('viewed_property', 'saved_property', 'search', 'inquiry')
- `data`: Action details

**Returns:**
- Updated profile

### PropertyRecommendationEngine

#### `recommend_properties(client_profile: Dict, available_properties: List[Dict], max_recommendations: int = 10) -> List[Dict]`
Generate personalized property recommendations.

**Parameters:**
- `client_profile`: Client profile with preferences
- `available_properties`: List of available properties
- `max_recommendations`: Maximum number of recommendations (default: 10)

**Returns:**
- Ranked list of recommended properties with match scores

### VirtualAssistant

#### `process_message(client_id: str, message: str, context: Dict = None) -> Dict`
Process client message and generate response.

**Parameters:**
- `client_id`: Client identifier
- `message`: User message
- `context`: Additional context (optional)

**Returns:**
- Response with intent and actions

### SentimentAnalyzer

#### `analyze_feedback(feedback_text: str, source: str = 'general') -> Dict`
Analyze client feedback sentiment.

**Parameters:**
- `feedback_text`: Feedback text to analyze
- `source`: Source of feedback ('review', 'survey', 'message', etc.)

**Returns:**
- Sentiment analysis results

---

## Property Operations Module

### PropertyMaintenanceManager

#### `create_maintenance_schedule(property_data: Dict) -> Dict`
Create predictive maintenance schedule for a property.

**Parameters:**
- `property_data`: Property details including age and features

**Returns:**
- Comprehensive maintenance schedule

#### `predict_upcoming_maintenance(property_id: str, months_ahead: int = 6) -> List[Dict]`
Predict upcoming maintenance needs.

**Parameters:**
- `property_id`: Property identifier
- `months_ahead`: Number of months to look ahead (default: 6)

**Returns:**
- List of upcoming maintenance tasks

### PropertyConditionMonitor

#### `assess_property_condition(property_id: str, inspection_data: Dict) -> Dict`
Assess overall property condition.

**Parameters:**
- `property_id`: Property identifier
- `inspection_data`: Inspection findings

**Returns:**
- Condition assessment report

#### `get_property_health_score(property_id: str) -> Dict`
Calculate overall property health score.

**Parameters:**
- `property_id`: Property identifier

**Returns:**
- Property health score and metrics

### VendorManager

#### `add_vendor(vendor_data: Dict) -> Dict`
Add a new vendor to the system.

**Parameters:**
- `vendor_data`: Vendor information

**Returns:**
- Vendor profile

#### `recommend_vendor(job_category: str, location: str) -> List[Dict]`
Recommend vendors for a specific job.

**Parameters:**
- `job_category`: Type of maintenance work
- `location`: Job location

**Returns:**
- List of recommended vendors

---

## Main Application

### PropertyBrokerageAI

#### `__init__()`
Initialize all AI modules.

#### `get_system_status() -> Dict`
Get system status and module information.

**Returns:**
- System status dictionary

#### `process_new_lead(lead_data: Dict) -> Dict`
Process a new lead through the complete pipeline.

**Parameters:**
- `lead_data`: Lead information

**Returns:**
- Complete lead analysis and actions

**Example:**
```python
from app import PropertyBrokerageAI

system = PropertyBrokerageAI()
result = system.process_new_lead({
    'id': 'LEAD-001',
    'name': 'John Doe',
    'email': 'john@example.com',
    'budget': 500000,
    'urgency': 'high'
})
```

#### `list_property(property_data: Dict, seller_data: Dict) -> Dict`
Complete property listing workflow.

**Parameters:**
- `property_data`: Property details
- `seller_data`: Seller information

**Returns:**
- Complete listing package

#### `find_properties_for_client(client_id: str, available_properties: List[Dict]) -> Dict`
Find and recommend properties for a client.

**Parameters:**
- `client_id`: Client identifier
- `available_properties`: List of available properties

**Returns:**
- Personalized property recommendations

#### `chat_with_client(client_id: str, message: str) -> Dict`
Process client chat message.

**Parameters:**
- `client_id`: Client identifier
- `message`: Client message

**Returns:**
- AI assistant response

#### `analyze_market(location: str, property_type: str) -> Dict`
Comprehensive market analysis.

**Parameters:**
- `location`: Market location
- `property_type`: Type of property

**Returns:**
- Complete market analysis

#### `create_marketing_campaign(campaign_name: str, property_data: Dict, channels: List[str]) -> Dict`
Create multi-channel marketing campaign.

**Parameters:**
- `campaign_name`: Campaign name
- `property_data`: Property details
- `channels`: Marketing channels

**Returns:**
- Campaign details

---

## Error Handling

All methods may raise exceptions. Common exceptions include:

- `ValueError`: Invalid input parameters
- `KeyError`: Missing required fields in dictionaries
- `TypeError`: Incorrect data types

It's recommended to wrap API calls in try-except blocks:

```python
try:
    result = system.process_new_lead(lead_data)
except ValueError as e:
    print(f"Invalid input: {e}")
except Exception as e:
    print(f"Error: {e}")
```

---

## Rate Limits

If using external AI services (OpenAI, etc.), be aware of rate limits:

- OpenAI API: Varies by plan
- Ensure proper error handling for rate limit errors

---

## Best Practices

1. **Always validate input data** before passing to API methods
2. **Use type hints** for better code clarity
3. **Handle exceptions** appropriately
4. **Log important operations** for debugging
5. **Cache results** when appropriate to reduce API calls
6. **Test thoroughly** before production deployment

---

## Support

For issues or questions about the API, please:
1. Check this documentation
2. Review the example code in each module
3. Create an issue on GitHub

---

**Last Updated:** 2026-01-05
