"""
AI-powered Market Analysis and Property Valuation

This module implements AI capabilities for:
- Historical data processing
- Automated property valuation (AVM)
- Market trend prediction
"""

import numpy as np
from typing import Dict, List, Optional
from datetime import datetime, timedelta


class AutomatedValuationModel:
    """Automated Valuation Model (AVM) for property pricing"""
    
    def __init__(self):
        self.features = [
            'square_footage',
            'bedrooms',
            'bathrooms',
            'age',
            'location_score',
            'condition_score'
        ]
        # Simplified coefficients for demonstration
        self.coefficients = {
            'square_footage': 150,  # $ per sq ft
            'bedrooms': 15000,
            'bathrooms': 10000,
            'age': -2000,  # negative impact
            'location_score': 50000,
            'condition_score': 30000
        }
        self.base_value = 100000
    
    def estimate_value(self, property_data: Dict) -> Dict:
        """
        Estimate property value using AI model
        
        Args:
            property_data: Dictionary with property features
            
        Returns:
            Dictionary with valuation results
        """
        # Calculate base valuation
        estimated_value = self.base_value
        
        for feature, coefficient in self.coefficients.items():
            value = property_data.get(feature, 0)
            estimated_value += value * coefficient
        
        # Calculate confidence interval
        confidence = self._calculate_confidence(property_data)
        margin = estimated_value * 0.1  # 10% margin
        
        return {
            'estimated_value': round(estimated_value, 2),
            'lower_bound': round(estimated_value - margin, 2),
            'upper_bound': round(estimated_value + margin, 2),
            'confidence_score': confidence,
            'valuation_date': datetime.now().isoformat(),
            'model_version': '1.0'
        }
    
    def analyze_comparables(self, target_property: Dict, comparables: List[Dict]) -> Dict:
        """
        Analyze comparable properties for valuation
        
        Args:
            target_property: Target property to value
            comparables: List of comparable properties
            
        Returns:
            Analysis results with adjusted valuation
        """
        if not comparables:
            return {'error': 'No comparable properties provided'}
        
        # Calculate average price per square foot from comparables
        comp_prices_per_sqft = []
        for comp in comparables:
            price = comp.get('sale_price', 0)
            sqft = comp.get('square_footage', 1)
            if sqft > 0:
                comp_prices_per_sqft.append(price / sqft)
        
        if not comp_prices_per_sqft:
            return {'error': 'Invalid comparable data'}
        
        avg_price_per_sqft = np.mean(comp_prices_per_sqft)
        target_sqft = target_property.get('square_footage', 0)
        
        comparable_value = avg_price_per_sqft * target_sqft
        
        # Apply adjustments for differences
        adjustments = self._calculate_adjustments(target_property, comparables)
        adjusted_value = comparable_value + adjustments['total_adjustment']
        
        return {
            'comparable_value': round(comparable_value, 2),
            'adjustments': adjustments,
            'adjusted_value': round(adjusted_value, 2),
            'number_of_comparables': len(comparables),
            'avg_price_per_sqft': round(avg_price_per_sqft, 2),
            'analysis_date': datetime.now().isoformat()
        }
    
    def _calculate_confidence(self, property_data: Dict) -> float:
        """Calculate confidence score for valuation"""
        confidence = 0.8  # Base confidence
        
        # Reduce confidence for missing data
        missing_features = sum(1 for f in self.features if f not in property_data)
        confidence -= (missing_features * 0.1)
        
        # Increase confidence for recent data
        data_age = property_data.get('data_age_days', 30)
        if data_age < 30:
            confidence += 0.1
        elif data_age > 90:
            confidence -= 0.1
        
        return max(0.5, min(1.0, confidence))
    
    def _calculate_adjustments(self, target: Dict, comparables: List[Dict]) -> Dict:
        """Calculate adjustments based on property differences"""
        adjustments = {
            'bedroom_adjustment': 0,
            'bathroom_adjustment': 0,
            'condition_adjustment': 0,
            'location_adjustment': 0
        }
        
        # Average comparable features
        avg_bedrooms = np.mean([c.get('bedrooms', 0) for c in comparables])
        avg_bathrooms = np.mean([c.get('bathrooms', 0) for c in comparables])
        avg_condition = np.mean([c.get('condition_score', 5) for c in comparables])
        
        # Calculate adjustments
        bedroom_diff = target.get('bedrooms', 0) - avg_bedrooms
        adjustments['bedroom_adjustment'] = bedroom_diff * 15000
        
        bathroom_diff = target.get('bathrooms', 0) - avg_bathrooms
        adjustments['bathroom_adjustment'] = bathroom_diff * 10000
        
        condition_diff = target.get('condition_score', 5) - avg_condition
        adjustments['condition_adjustment'] = condition_diff * 20000
        
        adjustments['total_adjustment'] = sum(adjustments.values())
        
        return adjustments


class MarketAnalyzer:
    """AI-powered market analysis and trend prediction"""
    
    def __init__(self):
        self.trend_window = 12  # months
        self.prediction_horizon = 6  # months
    
    def analyze_market_trends(self, historical_data: List[Dict]) -> Dict:
        """
        Analyze market trends from historical data
        
        Args:
            historical_data: List of historical market data points
            
        Returns:
            Market trend analysis
        """
        if not historical_data:
            return {'error': 'No historical data provided'}
        
        # Extract prices and dates
        prices = [d.get('median_price', 0) for d in historical_data]
        
        # Calculate trend metrics
        trend = self._calculate_trend(prices)
        volatility = self._calculate_volatility(prices)
        momentum = self._calculate_momentum(prices)
        
        return {
            'trend': trend,
            'volatility': volatility,
            'momentum': momentum,
            'current_median_price': prices[-1] if prices else 0,
            'price_change_pct': self._calculate_price_change(prices),
            'market_status': self._determine_market_status(trend, momentum),
            'analysis_date': datetime.now().isoformat()
        }
    
    def predict_market_trend(self, historical_data: List[Dict]) -> Dict:
        """
        Predict future market trends
        
        Args:
            historical_data: List of historical market data
            
        Returns:
            Market predictions
        """
        if not historical_data:
            return {'error': 'No historical data provided'}
        
        prices = [d.get('median_price', 0) for d in historical_data]
        
        # Simple linear trend prediction
        predictions = self._generate_predictions(prices)
        
        return {
            'predictions': predictions,
            'prediction_horizon_months': self.prediction_horizon,
            'confidence_level': 0.75,
            'methodology': 'AI-powered time series analysis',
            'prediction_date': datetime.now().isoformat()
        }
    
    def analyze_neighborhood(self, neighborhood_data: Dict) -> Dict:
        """
        Analyze neighborhood market dynamics
        
        Args:
            neighborhood_data: Neighborhood statistics
            
        Returns:
            Neighborhood analysis
        """
        metrics = {
            'avg_days_on_market': neighborhood_data.get('avg_days_on_market', 60),
            'sale_to_list_ratio': neighborhood_data.get('sale_to_list_ratio', 0.98),
            'inventory_level': neighborhood_data.get('inventory_level', 3.0),
            'price_growth_yoy': neighborhood_data.get('price_growth_yoy', 0.05)
        }
        
        market_heat = self._calculate_market_heat(metrics)
        
        return {
            'metrics': metrics,
            'market_heat_index': market_heat,
            'market_type': self._classify_market(metrics),
            'investment_score': self._calculate_investment_score(metrics),
            'analysis_date': datetime.now().isoformat()
        }
    
    def _calculate_trend(self, prices: List[float]) -> str:
        """Calculate price trend direction"""
        if len(prices) < 2:
            return 'INSUFFICIENT_DATA'
        
        recent_avg = np.mean(prices[-3:])
        older_avg = np.mean(prices[:3])
        
        change = (recent_avg - older_avg) / older_avg
        
        if change > 0.05:
            return 'RISING'
        elif change < -0.05:
            return 'FALLING'
        else:
            return 'STABLE'
    
    def _calculate_volatility(self, prices: List[float]) -> float:
        """Calculate price volatility"""
        if len(prices) < 2:
            return 0.0
        return round(np.std(prices) / np.mean(prices), 4)
    
    def _calculate_momentum(self, prices: List[float]) -> str:
        """Calculate market momentum"""
        if len(prices) < 3:
            return 'NEUTRAL'
        
        recent_change = (prices[-1] - prices[-2]) / prices[-2]
        
        if recent_change > 0.02:
            return 'STRONG_POSITIVE'
        elif recent_change > 0:
            return 'POSITIVE'
        elif recent_change < -0.02:
            return 'STRONG_NEGATIVE'
        elif recent_change < 0:
            return 'NEGATIVE'
        else:
            return 'NEUTRAL'
    
    def _calculate_price_change(self, prices: List[float]) -> float:
        """Calculate percentage price change"""
        if len(prices) < 2:
            return 0.0
        return round(((prices[-1] - prices[0]) / prices[0]) * 100, 2)
    
    def _determine_market_status(self, trend: str, momentum: str) -> str:
        """Determine overall market status"""
        if trend == 'RISING' and 'POSITIVE' in momentum:
            return 'SELLERS_MARKET'
        elif trend == 'FALLING' and 'NEGATIVE' in momentum:
            return 'BUYERS_MARKET'
        else:
            return 'BALANCED_MARKET'
    
    def _generate_predictions(self, prices: List[float]) -> List[Dict]:
        """Generate price predictions"""
        if not prices:
            return []
        
        # Simple linear projection
        predictions = []
        last_price = prices[-1]
        trend_rate = (prices[-1] - prices[0]) / len(prices) if len(prices) > 1 else 0
        
        for month in range(1, self.prediction_horizon + 1):
            predicted_price = last_price + (trend_rate * month)
            predictions.append({
                'month': month,
                'predicted_price': round(predicted_price, 2),
                'prediction_date': (datetime.now() + timedelta(days=30*month)).strftime('%Y-%m')
            })
        
        return predictions
    
    def _calculate_market_heat(self, metrics: Dict) -> float:
        """Calculate market heat index (0-100)"""
        heat = 50.0  # Base
        
        # Days on market (lower is hotter)
        days = metrics['avg_days_on_market']
        if days < 30:
            heat += 20
        elif days > 60:
            heat -= 20
        
        # Sale to list ratio (higher is hotter)
        ratio = metrics['sale_to_list_ratio']
        if ratio > 1.0:
            heat += 15
        elif ratio < 0.95:
            heat -= 15
        
        # Inventory (lower is hotter)
        inventory = metrics['inventory_level']
        if inventory < 2.0:
            heat += 15
        elif inventory > 6.0:
            heat -= 15
        
        return max(0, min(100, heat))
    
    def _classify_market(self, metrics: Dict) -> str:
        """Classify market type"""
        heat = self._calculate_market_heat(metrics)
        
        if heat > 70:
            return 'HOT_SELLERS_MARKET'
        elif heat > 55:
            return 'SELLERS_MARKET'
        elif heat > 45:
            return 'BALANCED'
        elif heat > 30:
            return 'BUYERS_MARKET'
        else:
            return 'COLD_BUYERS_MARKET'
    
    def _calculate_investment_score(self, metrics: Dict) -> float:
        """Calculate investment attractiveness score (0-100)"""
        score = 50.0
        
        # Price growth
        growth = metrics['price_growth_yoy']
        score += growth * 100
        
        # Market dynamics
        heat = self._calculate_market_heat(metrics)
        score += (heat - 50) * 0.3
        
        return round(max(0, min(100, score)), 2)
