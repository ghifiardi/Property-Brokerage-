# Quick Start Guide

Get started with AI-Powered Property Brokerage in 5 minutes!

## Prerequisites

- Python 3.8 or higher
- pip package manager

## Installation

```bash
# 1. Clone the repository
git clone https://github.com/ghifiardi/Property-Brokerage-.git
cd Property-Brokerage-

# 2. Install dependencies
pip install -r requirements.txt
```

## Run the Demo

```bash
# Set Python path and run example
PYTHONPATH=. python examples/complete_workflow.py
```

You should see a complete workflow demonstrating:
- Lead scoring and prioritization
- AI chatbot interaction
- Property recommendations
- Automated valuation
- Content generation
- Fair Housing compliance check
- Social media campaign

## Run Tests

```bash
# Run all tests
pytest tests/ -v

# Run specific test module
pytest tests/test_lead_generation.py -v
pytest tests/test_ethical_compliance.py -v

# Run with coverage
pytest --cov=src tests/
```

## Basic Usage Examples

### 1. Score a Lead

```python
from src.ai_modules import LeadScoringSystem

scorer = LeadScoringSystem()
lead = {
    'page_views': 8,
    'time_on_site': 25,
    'property_inquiries': 3,
    'contact_attempts': 1,
    'budget_match': 0.8
}

score = scorer.score_lead(lead)
print(f"Lead Score: {score}/100")
# Output: Lead Score: 76.33/100
```

### 2. Use AI Chatbot

```python
from src.ai_modules import AIchatbot

bot = AIchatbot()
response = bot.get_response("I'm looking for a 3-bedroom house")
print(response)
# Output: AI-generated helpful response
```

### 3. Generate Property Description

```python
from src.ai_modules import PropertyDescriptionGenerator

generator = PropertyDescriptionGenerator()
property_data = {
    'type': 'house',
    'bedrooms': 3,
    'bathrooms': 2,
    'square_footage': 2000,
    'location': 'downtown',
    'features': ['Updated kitchen', 'Hardwood floors', 'Garage']
}

description = generator.generate_description(property_data)
print(description['description'])
```

### 4. Check Fair Housing Compliance

```python
from src.ai_modules import FairHousingCompliance

compliance = FairHousingCompliance()
content = "Beautiful 3-bedroom house with modern amenities"

result = compliance.check_content(content)
print(f"Compliant: {result['compliant']}")
print(f"Recommendation: {result['recommendation']}")
```

### 5. Recommend Properties

```python
from src.ai_modules import PropertyRecommendationSystem

recommender = PropertyRecommendationSystem()

client_profile = {
    'preferences': {
        'preferred_locations': ['downtown'],
        'price_range': {'min': 400000, 'max': 600000},
        'preferred_property_types': ['house'],
        'must_have_amenities': ['garage', 'backyard']
    }
}

properties = [
    {'id': 'P1', 'location': 'downtown', 'price': 485000, 
     'type': 'house', 'amenities': ['garage', 'backyard']},
    # ... more properties
]

recommendations = recommender.recommend_properties(
    client_profile, properties, top_n=5
)

for rec in recommendations:
    print(f"Property {rec['property']['id']}: {rec['match_score']}/100")
    print(f"Reasons: {', '.join(rec['match_reasons'])}")
```

## Configuration

Edit `config.py` to customize:
- AI model paths
- Database connections
- Compliance settings
- Disclosure text
- API rate limits

```python
from config import config

# Use development config
app_config = config['development']

# Or production
app_config = config['production']
```

## Next Steps

1. **Read Documentation**
   - [Ethical Guidelines](docs/ETHICAL_GUIDELINES.md)
   - [Implementation Guide](docs/IMPLEMENTATION_GUIDE.md)

2. **Explore Examples**
   - Check `examples/complete_workflow.py` for full workflow
   - Modify parameters to test different scenarios

3. **Run Tests**
   - Ensure all tests pass in your environment
   - Add tests for custom features

4. **Customize**
   - Adjust lead scoring weights
   - Customize chatbot responses
   - Add your own property features

5. **Integrate**
   - Connect to your CRM
   - Integrate with MLS
   - Add to your website

## Common Issues

### Import Errors
```bash
# Solution: Set PYTHONPATH
export PYTHONPATH=/path/to/Property-Brokerage-:$PYTHONPATH
# or
PYTHONPATH=. python your_script.py
```

### Missing Dependencies
```bash
# Solution: Install all requirements
pip install -r requirements.txt

# Or install specific package
pip install numpy pandas
```

### Test Failures
```bash
# Ensure you're in the project root
cd /path/to/Property-Brokerage-

# Run tests with verbose output
pytest tests/ -v -s
```

## Support

- **Documentation**: Check `docs/` folder
- **Examples**: See `examples/` folder  
- **Issues**: Open issue on GitHub
- **Tests**: Run `pytest tests/` to verify setup

## Important Reminders

⚠️ **Before Production Use:**

1. ✅ Read ethical guidelines thoroughly
2. ✅ Understand Fair Housing requirements
3. ✅ Test all features with real data
4. ✅ Configure proper disclosures
5. ✅ Set up data encryption
6. ✅ Train your team
7. ✅ Consult legal counsel if needed

🎉 **You're Ready!**

Start with one feature, test thoroughly, then gradually expand your AI usage. Remember: AI assists, humans decide!
