"""
AI-Powered Property Brokerage System
Module 2: Market Analysis and Property Valuation

This module provides AI capabilities for:
- Automated market trend analysis
- Property valuation using machine learning
- Comparative market analysis (CMA)
- Investment opportunity identification
"""

from typing import List, Dict, Optional, Tuple
from datetime import datetime, timedelta
import json


class MarketAnalyzer:
    """AI-powered market analysis and trend prediction"""
    
    def __init__(self):
        self.market_data = {}
        self.historical_prices = []
    
    def analyze_market_trends(self, location: str, property_type: str, 
                             time_period_days: int = 90) -> Dict:
        """
        Analyze market trends for a specific location and property type
        
        Args:
            location: Geographic location to analyze
            property_type: Type of property (residential, commercial, etc.)
            time_period_days: Number of days to analyze
            
        Returns:
            Market analysis report
        """
        # Simulate market analysis (in production, this would use real data)
        trend_direction = "upward"  # Could be: upward, downward, stable
        avg_price_change = 5.2  # Percentage change
        demand_level = "high"  # Could be: low, medium, high
        
        analysis = {
            'location': location,
            'property_type': property_type,
            'analysis_period_days': time_period_days,
            'trend_direction': trend_direction,
            'avg_price_change_percent': avg_price_change,
            'demand_level': demand_level,
            'market_temperature': self._calculate_market_temperature(avg_price_change, demand_level),
            'key_insights': self._generate_market_insights(location, trend_direction, avg_price_change),
            'forecast': self._generate_short_term_forecast(avg_price_change),
            'analyzed_at': datetime.now().isoformat()
        }
        
        return analysis
    
    def _calculate_market_temperature(self, price_change: float, demand: str) -> str:
        """Calculate market temperature (hot, warm, cold)"""
        if price_change > 5 and demand == "high":
            return "HOT - Seller's market"
        elif price_change < -5 and demand == "low":
            return "COLD - Buyer's market"
        else:
            return "WARM - Balanced market"
    
    def _generate_market_insights(self, location: str, trend: str, change: float) -> List[str]:
        """Generate actionable market insights"""
        insights = []
        
        if trend == "upward":
            insights.append(f"Property values in {location} are increasing at {change}% per quarter")
            insights.append("Strong buyer demand indicates good investment opportunity")
            insights.append("Recommend acting quickly for buyers to secure current prices")
        elif trend == "downward":
            insights.append(f"Property values in {location} are decreasing at {abs(change)}% per quarter")
            insights.append("Opportunity for buyers to negotiate better prices")
            insights.append("Sellers should consider strategic pricing")
        else:
            insights.append(f"Property market in {location} is stable")
            insights.append("Good time for both buyers and sellers")
        
        return insights
    
    def _generate_short_term_forecast(self, current_change: float) -> Dict:
        """Generate 6-month market forecast"""
        return {
            'next_3_months': {
                'expected_change_percent': current_change * 0.8,
                'confidence': 'medium'
            },
            'next_6_months': {
                'expected_change_percent': current_change * 1.2,
                'confidence': 'low'
            }
        }
    
    def compare_locations(self, locations: List[str], property_type: str) -> List[Dict]:
        """
        Compare multiple locations for market performance
        
        Args:
            locations: List of locations to compare
            property_type: Type of property
            
        Returns:
            Comparative analysis of locations
        """
        comparisons = []
        
        for location in locations:
            analysis = self.analyze_market_trends(location, property_type)
            comparisons.append({
                'location': location,
                'market_score': self._calculate_market_score(analysis),
                'trend_direction': analysis['trend_direction'],
                'avg_price_change': analysis['avg_price_change_percent'],
                'recommendation': self._get_location_recommendation(analysis)
            })
        
        # Sort by market score
        comparisons.sort(key=lambda x: x['market_score'], reverse=True)
        return comparisons
    
    def _calculate_market_score(self, analysis: Dict) -> float:
        """Calculate overall market score (0-100)"""
        score = 50  # Base score
        
        # Adjust based on trend
        if analysis['trend_direction'] == 'upward':
            score += 20
        elif analysis['trend_direction'] == 'downward':
            score -= 10
        
        # Adjust based on demand
        if analysis['demand_level'] == 'high':
            score += 15
        elif analysis['demand_level'] == 'low':
            score -= 10
        
        # Adjust based on price change
        score += min(analysis['avg_price_change_percent'], 15)
        
        return min(max(score, 0), 100)
    
    def _get_location_recommendation(self, analysis: Dict) -> str:
        """Generate recommendation for a location"""
        temp = analysis['market_temperature']
        
        if "HOT" in temp:
            return "Excellent for sellers, buyers should act fast"
        elif "COLD" in temp:
            return "Great opportunity for buyers, sellers should price strategically"
        else:
            return "Balanced market, good for both buyers and sellers"


class PropertyValuationEngine:
    """AI-powered property valuation system"""
    
    def __init__(self):
        self.valuation_models = {}
        self.comparable_sales = []
    
    def estimate_property_value(self, property_data: Dict) -> Dict:
        """
        Estimate property value using AI/ML algorithms
        
        Args:
            property_data: Property characteristics and details
            
        Returns:
            Valuation estimate with confidence interval
        """
        # Extract property features
        size = property_data.get('size_sqft', 1000)
        bedrooms = property_data.get('bedrooms', 2)
        bathrooms = property_data.get('bathrooms', 2)
        age = property_data.get('age_years', 10)
        location_score = property_data.get('location_score', 7)  # 1-10 scale
        condition = property_data.get('condition', 'good')  # poor, fair, good, excellent
        
        # Base valuation calculation (simplified model)
        base_price_per_sqft = 150  # Base price
        
        # Adjust for location
        location_multiplier = 1 + (location_score - 5) * 0.1
        
        # Adjust for condition
        condition_multipliers = {
            'poor': 0.8,
            'fair': 0.9,
            'good': 1.0,
            'excellent': 1.15
        }
        condition_multiplier = condition_multipliers.get(condition, 1.0)
        
        # Adjust for age (depreciation)
        age_adjustment = 1 - (age * 0.01)  # 1% per year
        age_adjustment = max(age_adjustment, 0.7)  # Minimum 70% of value
        
        # Calculate estimated value
        estimated_value = (
            base_price_per_sqft * 
            size * 
            location_multiplier * 
            condition_multiplier * 
            age_adjustment
        )
        
        # Add premiums for features
        if bedrooms > 3:
            estimated_value *= 1.05
        if bathrooms > 2:
            estimated_value *= 1.03
        
        # Calculate confidence interval (±10%)
        lower_bound = estimated_value * 0.9
        upper_bound = estimated_value * 1.1
        
        valuation = {
            'property_id': property_data.get('id', 'unknown'),
            'estimated_value': round(estimated_value, 2),
            'value_range': {
                'lower': round(lower_bound, 2),
                'upper': round(upper_bound, 2)
            },
            'price_per_sqft': round(estimated_value / size, 2),
            'confidence_score': 0.85,  # 85% confidence
            'valuation_factors': {
                'size_impact': f"{size} sqft",
                'location_impact': f"{location_score}/10",
                'condition_impact': condition,
                'age_impact': f"{age} years"
            },
            'comparable_properties_analyzed': 15,  # Simulated
            'valuation_date': datetime.now().isoformat()
        }
        
        return valuation
    
    def perform_cma(self, subject_property: Dict, radius_miles: float = 2.0) -> Dict:
        """
        Perform Comparative Market Analysis (CMA)
        
        Args:
            subject_property: Property to analyze
            radius_miles: Search radius for comparable properties
            
        Returns:
            CMA report with comparable properties
        """
        # Get property valuation
        valuation = self.estimate_property_value(subject_property)
        
        # Generate comparable properties (simulated)
        comparable_properties = self._find_comparable_properties(
            subject_property, 
            radius_miles
        )
        
        # Calculate market statistics
        comp_prices = [comp['sold_price'] for comp in comparable_properties]
        avg_price = sum(comp_prices) / len(comp_prices) if comp_prices else 0
        
        cma_report = {
            'subject_property': {
                'id': subject_property.get('id'),
                'estimated_value': valuation['estimated_value'],
                'value_range': valuation['value_range']
            },
            'comparable_properties': comparable_properties,
            'market_statistics': {
                'avg_sold_price': round(avg_price, 2),
                'price_variance': round((valuation['estimated_value'] - avg_price) / avg_price * 100, 2) if avg_price > 0 else 0,
                'days_on_market_avg': 45,  # Simulated
                'properties_analyzed': len(comparable_properties)
            },
            'pricing_recommendation': self._generate_pricing_recommendation(
                valuation['estimated_value'], 
                avg_price
            ),
            'report_date': datetime.now().isoformat()
        }
        
        return cma_report
    
    def _find_comparable_properties(self, subject: Dict, radius: float) -> List[Dict]:
        """Find comparable properties (simulated data)"""
        comparables = []
        base_value = self.estimate_property_value(subject)['estimated_value']
        
        for i in range(5):  # Generate 5 comparable properties
            variance = 0.95 + (i * 0.02)  # ±5% variance
            comp = {
                'id': f'COMP-{i+1}',
                'address': f'Comparable Property {i+1}',
                'distance_miles': round(0.5 + (i * 0.3), 2),
                'size_sqft': subject.get('size_sqft', 1000) * (0.9 + i * 0.05),
                'bedrooms': subject.get('bedrooms', 2),
                'bathrooms': subject.get('bathrooms', 2),
                'sold_price': round(base_value * variance, 2),
                'sold_date': (datetime.now() - timedelta(days=30+i*10)).isoformat(),
                'similarity_score': round(0.85 + (i * 0.02), 2)
            }
            comparables.append(comp)
        
        return comparables
    
    def _generate_pricing_recommendation(self, estimated_value: float, market_avg: float) -> Dict:
        """Generate pricing recommendations"""
        if market_avg > 0:
            diff_percent = ((estimated_value - market_avg) / market_avg) * 100
        else:
            diff_percent = 0
        
        if diff_percent > 5:
            strategy = "Price at premium - property has above-average features"
            suggested_price = estimated_value * 0.98
        elif diff_percent < -5:
            strategy = "Competitive pricing - emphasize value proposition"
            suggested_price = estimated_value * 1.02
        else:
            strategy = "Market-aligned pricing - standard approach"
            suggested_price = estimated_value
        
        return {
            'suggested_list_price': round(suggested_price, 2),
            'pricing_strategy': strategy,
            'market_position': 'above' if diff_percent > 0 else 'below' if diff_percent < 0 else 'aligned',
            'expected_time_to_sell_days': 30 if abs(diff_percent) < 5 else 45
        }
    
    def identify_investment_opportunities(self, properties: List[Dict]) -> List[Dict]:
        """
        Identify best investment opportunities from a list of properties
        
        Args:
            properties: List of properties to evaluate
            
        Returns:
            Ranked list of investment opportunities
        """
        opportunities = []
        
        for prop in properties:
            valuation = self.estimate_property_value(prop)
            asking_price = prop.get('asking_price', valuation['estimated_value'])
            
            # Calculate investment metrics
            value_difference = valuation['estimated_value'] - asking_price
            roi_potential = (value_difference / asking_price * 100) if asking_price > 0 else 0
            
            opportunity_score = self._calculate_investment_score(
                roi_potential,
                prop.get('location_score', 5),
                prop.get('condition', 'good')
            )
            
            opportunities.append({
                'property_id': prop.get('id'),
                'asking_price': asking_price,
                'estimated_value': valuation['estimated_value'],
                'potential_value_gain': round(value_difference, 2),
                'roi_potential_percent': round(roi_potential, 2),
                'investment_score': opportunity_score,
                'recommendation': self._get_investment_recommendation(opportunity_score)
            })
        
        # Sort by investment score
        opportunities.sort(key=lambda x: x['investment_score'], reverse=True)
        return opportunities
    
    def _calculate_investment_score(self, roi: float, location: int, condition: str) -> float:
        """Calculate investment opportunity score (0-100)"""
        score = 50  # Base score
        
        # ROI impact
        score += min(roi, 30)  # Cap at 30 points
        
        # Location impact
        score += (location - 5) * 3
        
        # Condition impact
        condition_bonus = {
            'poor': -10,
            'fair': 0,
            'good': 5,
            'excellent': 10
        }
        score += condition_bonus.get(condition, 0)
        
        return min(max(score, 0), 100)
    
    def _get_investment_recommendation(self, score: float) -> str:
        """Get investment recommendation based on score"""
        if score >= 75:
            return "STRONG BUY - Excellent investment opportunity"
        elif score >= 60:
            return "BUY - Good investment potential"
        elif score >= 45:
            return "CONSIDER - Average investment potential"
        else:
            return "PASS - Below average investment potential"


# Example usage and demonstration
if __name__ == "__main__":
    # Market Analysis
    print("=== Market Analysis ===")
    market_analyzer = MarketAnalyzer()
    
    analysis = market_analyzer.analyze_market_trends("Downtown", "residential", 90)
    print(f"\nLocation: {analysis['location']}")
    print(f"Market Temperature: {analysis['market_temperature']}")
    print(f"Trend: {analysis['trend_direction']} ({analysis['avg_price_change_percent']}%)")
    print(f"\nKey Insights:")
    for insight in analysis['key_insights']:
        print(f"  - {insight}")
    
    # Location Comparison
    print("\n=== Location Comparison ===")
    locations = ["Downtown", "Suburbs", "Waterfront"]
    comparison = market_analyzer.compare_locations(locations, "residential")
    for loc in comparison:
        print(f"\n{loc['location']}: Score {loc['market_score']:.1f}/100")
        print(f"  Recommendation: {loc['recommendation']}")
    
    # Property Valuation
    print("\n=== Property Valuation ===")
    valuation_engine = PropertyValuationEngine()
    
    sample_property = {
        'id': 'PROP-001',
        'size_sqft': 2000,
        'bedrooms': 3,
        'bathrooms': 2,
        'age_years': 5,
        'location_score': 8,
        'condition': 'good'
    }
    
    valuation = valuation_engine.estimate_property_value(sample_property)
    print(f"\nProperty ID: {valuation['property_id']}")
    print(f"Estimated Value: ${valuation['estimated_value']:,.2f}")
    print(f"Value Range: ${valuation['value_range']['lower']:,.2f} - ${valuation['value_range']['upper']:,.2f}")
    print(f"Price per sqft: ${valuation['price_per_sqft']:.2f}")
    print(f"Confidence: {valuation['confidence_score']*100}%")
    
    # CMA Report
    print("\n=== Comparative Market Analysis ===")
    cma = valuation_engine.perform_cma(sample_property)
    print(f"Subject Property Value: ${cma['subject_property']['estimated_value']:,.2f}")
    print(f"Market Average: ${cma['market_statistics']['avg_sold_price']:,.2f}")
    print(f"Comparable Properties Analyzed: {cma['market_statistics']['properties_analyzed']}")
    print(f"\nPricing Recommendation:")
    print(f"  Suggested List Price: ${cma['pricing_recommendation']['suggested_list_price']:,.2f}")
    print(f"  Strategy: {cma['pricing_recommendation']['pricing_strategy']}")
