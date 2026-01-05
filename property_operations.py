"""
AI-Powered Property Brokerage System
Module 6: Property Operations and Maintenance

This module provides AI capabilities for:
- Predictive maintenance scheduling
- Property condition monitoring
- Maintenance cost estimation
- Vendor management
- Issue detection and resolution
"""

from typing import List, Dict, Optional, Tuple
from datetime import datetime, timedelta
import json


class PropertyMaintenanceManager:
    """AI-powered property maintenance management"""
    
    def __init__(self):
        self.maintenance_schedules = {}
        self.maintenance_history = []
    
    def create_maintenance_schedule(self, property_data: Dict) -> Dict:
        """
        Create predictive maintenance schedule for a property
        
        Args:
            property_data: Property details including age and features
            
        Returns:
            Comprehensive maintenance schedule
        """
        property_id = property_data.get('id', 'unknown')
        property_age = property_data.get('age_years', 0)
        property_type = property_data.get('type', 'residential')
        
        # Generate maintenance tasks based on property characteristics
        schedule = {
            'property_id': property_id,
            'created_at': datetime.now().isoformat(),
            'property_age': property_age,
            'tasks': []
        }
        
        # Standard maintenance tasks
        standard_tasks = [
            {
                'name': 'HVAC System Inspection',
                'frequency': 'quarterly',
                'estimated_cost': 150,
                'priority': 'high',
                'category': 'HVAC',
                'description': 'Inspect and service heating/cooling systems'
            },
            {
                'name': 'Plumbing Inspection',
                'frequency': 'semi-annual',
                'estimated_cost': 200,
                'priority': 'medium',
                'category': 'Plumbing',
                'description': 'Check for leaks, water pressure, and drainage'
            },
            {
                'name': 'Electrical System Check',
                'frequency': 'annual',
                'estimated_cost': 250,
                'priority': 'high',
                'category': 'Electrical',
                'description': 'Inspect electrical panel, outlets, and wiring'
            },
            {
                'name': 'Roof Inspection',
                'frequency': 'annual',
                'estimated_cost': 300,
                'priority': 'high',
                'category': 'Structural',
                'description': 'Inspect roof for damage, leaks, and wear'
            },
            {
                'name': 'Gutter Cleaning',
                'frequency': 'quarterly',
                'estimated_cost': 100,
                'priority': 'medium',
                'category': 'Exterior',
                'description': 'Clean gutters and downspouts'
            },
            {
                'name': 'Water Heater Maintenance',
                'frequency': 'annual',
                'estimated_cost': 150,
                'priority': 'medium',
                'category': 'Plumbing',
                'description': 'Flush water heater and check for issues'
            },
            {
                'name': 'Fire Safety Check',
                'frequency': 'annual',
                'estimated_cost': 100,
                'priority': 'high',
                'category': 'Safety',
                'description': 'Test smoke detectors and fire extinguishers'
            },
            {
                'name': 'Exterior Painting',
                'frequency': 'every_5_years',
                'estimated_cost': 3500,
                'priority': 'medium',
                'category': 'Exterior',
                'description': 'Repaint exterior surfaces'
            }
        ]
        
        # Add age-specific tasks
        if property_age > 15:
            standard_tasks.append({
                'name': 'Foundation Inspection',
                'frequency': 'every_3_years',
                'estimated_cost': 500,
                'priority': 'high',
                'category': 'Structural',
                'description': 'Inspect foundation for cracks and settling'
            })
        
        if property_age > 20:
            standard_tasks.append({
                'name': 'Window Replacement Assessment',
                'frequency': 'every_5_years',
                'estimated_cost': 5000,
                'priority': 'medium',
                'category': 'Structural',
                'description': 'Assess window condition and energy efficiency'
            })
        
        # Calculate next due dates
        for task in standard_tasks:
            task['next_due_date'] = self._calculate_next_due_date(task['frequency'])
            task['status'] = 'scheduled'
            schedule['tasks'].append(task)
        
        # Calculate annual maintenance budget
        schedule['annual_maintenance_budget'] = self._calculate_annual_budget(schedule['tasks'])
        
        self.maintenance_schedules[property_id] = schedule
        return schedule
    
    def _calculate_next_due_date(self, frequency: str) -> str:
        """Calculate next due date based on frequency"""
        now = datetime.now()
        
        frequency_map = {
            'monthly': 30,
            'quarterly': 90,
            'semi-annual': 180,
            'annual': 365,
            'every_3_years': 1095,
            'every_5_years': 1825
        }
        
        days = frequency_map.get(frequency, 365)
        next_date = now + timedelta(days=days)
        
        return next_date.date().isoformat()
    
    def _calculate_annual_budget(self, tasks: List[Dict]) -> float:
        """Calculate estimated annual maintenance budget"""
        annual_cost = 0
        
        frequency_multipliers = {
            'monthly': 12,
            'quarterly': 4,
            'semi-annual': 2,
            'annual': 1,
            'every_3_years': 1/3,
            'every_5_years': 1/5
        }
        
        for task in tasks:
            frequency = task.get('frequency', 'annual')
            cost = task.get('estimated_cost', 0)
            multiplier = frequency_multipliers.get(frequency, 1)
            
            annual_cost += cost * multiplier
        
        return round(annual_cost, 2)
    
    def predict_upcoming_maintenance(self, property_id: str, 
                                    months_ahead: int = 6) -> List[Dict]:
        """
        Predict upcoming maintenance needs
        
        Args:
            property_id: Property identifier
            months_ahead: Number of months to look ahead
            
        Returns:
            List of upcoming maintenance tasks
        """
        if property_id not in self.maintenance_schedules:
            return []
        
        schedule = self.maintenance_schedules[property_id]
        cutoff_date = (datetime.now() + timedelta(days=months_ahead*30)).date()
        
        upcoming_tasks = []
        
        for task in schedule['tasks']:
            due_date = datetime.fromisoformat(task['next_due_date']).date()
            
            if due_date <= cutoff_date:
                days_until_due = (due_date - datetime.now().date()).days
                
                upcoming_tasks.append({
                    'task_name': task['name'],
                    'due_date': task['next_due_date'],
                    'days_until_due': days_until_due,
                    'estimated_cost': task['estimated_cost'],
                    'priority': task['priority'],
                    'category': task['category'],
                    'urgency': 'overdue' if days_until_due < 0 else 'urgent' if days_until_due < 30 else 'upcoming'
                })
        
        # Sort by urgency and due date
        upcoming_tasks.sort(key=lambda x: (x['urgency'] != 'overdue', x['urgency'] != 'urgent', x['days_until_due']))
        
        return upcoming_tasks
    
    def log_maintenance_activity(self, property_id: str, activity: Dict) -> Dict:
        """
        Log completed maintenance activity
        
        Args:
            property_id: Property identifier
            activity: Maintenance activity details
            
        Returns:
            Logged activity with insights
        """
        log_entry = {
            'property_id': property_id,
            'activity_date': datetime.now().isoformat(),
            'task_name': activity.get('task_name', ''),
            'category': activity.get('category', 'general'),
            'actual_cost': activity.get('cost', 0),
            'vendor': activity.get('vendor', 'unknown'),
            'notes': activity.get('notes', ''),
            'status': 'completed'
        }
        
        self.maintenance_history.append(log_entry)
        
        # Update schedule if task exists
        if property_id in self.maintenance_schedules:
            schedule = self.maintenance_schedules[property_id]
            for task in schedule['tasks']:
                if task['name'] == activity.get('task_name'):
                    task['last_completed'] = datetime.now().isoformat()
                    task['next_due_date'] = self._calculate_next_due_date(task['frequency'])
        
        return log_entry
    
    def get_maintenance_analytics(self, property_id: str) -> Dict:
        """
        Get maintenance analytics for a property
        
        Args:
            property_id: Property identifier
            
        Returns:
            Maintenance analytics and insights
        """
        property_history = [
            log for log in self.maintenance_history 
            if log['property_id'] == property_id
        ]
        
        if not property_history:
            return {
                'property_id': property_id,
                'total_maintenance_activities': 0,
                'message': 'No maintenance history available'
            }
        
        # Calculate statistics
        total_cost = sum(log['actual_cost'] for log in property_history)
        avg_cost = total_cost / len(property_history)
        
        # Category breakdown
        category_costs = {}
        for log in property_history:
            category = log['category']
            category_costs[category] = category_costs.get(category, 0) + log['actual_cost']
        
        # Find most expensive category
        most_expensive_category = max(category_costs.items(), key=lambda x: x[1])
        
        return {
            'property_id': property_id,
            'total_maintenance_activities': len(property_history),
            'total_cost': round(total_cost, 2),
            'average_cost_per_activity': round(avg_cost, 2),
            'cost_by_category': category_costs,
            'most_expensive_category': {
                'category': most_expensive_category[0],
                'total_cost': most_expensive_category[1]
            },
            'analysis_period': {
                'from': property_history[0]['activity_date'],
                'to': property_history[-1]['activity_date']
            }
        }


class PropertyConditionMonitor:
    """AI-powered property condition monitoring and issue detection"""
    
    def __init__(self):
        self.condition_reports = {}
        self.issue_alerts = []
    
    def assess_property_condition(self, property_id: str, 
                                 inspection_data: Dict) -> Dict:
        """
        Assess overall property condition
        
        Args:
            property_id: Property identifier
            inspection_data: Inspection findings
            
        Returns:
            Condition assessment report
        """
        # Extract inspection data
        structural_score = inspection_data.get('structural_integrity', 8)  # 1-10 scale
        systems_score = inspection_data.get('systems_functionality', 7)
        exterior_score = inspection_data.get('exterior_condition', 8)
        interior_score = inspection_data.get('interior_condition', 7)
        
        # Calculate overall condition score
        overall_score = (structural_score + systems_score + exterior_score + interior_score) / 4
        
        # Determine condition grade
        condition_grade = self._calculate_condition_grade(overall_score)
        
        # Identify issues
        issues = self._identify_issues(inspection_data)
        
        # Generate recommendations
        recommendations = self._generate_maintenance_recommendations(overall_score, issues)
        
        assessment = {
            'property_id': property_id,
            'assessment_date': datetime.now().isoformat(),
            'overall_condition_score': round(overall_score, 2),
            'condition_grade': condition_grade,
            'component_scores': {
                'structural_integrity': structural_score,
                'systems_functionality': systems_score,
                'exterior_condition': exterior_score,
                'interior_condition': interior_score
            },
            'identified_issues': issues,
            'recommendations': recommendations,
            'estimated_repair_costs': self._estimate_repair_costs(issues)
        }
        
        self.condition_reports[property_id] = assessment
        
        # Create alerts for critical issues
        critical_issues = [i for i in issues if i['severity'] == 'critical']
        if critical_issues:
            self._create_issue_alerts(property_id, critical_issues)
        
        return assessment
    
    def _calculate_condition_grade(self, score: float) -> str:
        """Calculate condition grade from score"""
        if score >= 9:
            return "Excellent"
        elif score >= 7:
            return "Good"
        elif score >= 5:
            return "Fair"
        elif score >= 3:
            return "Poor"
        else:
            return "Critical"
    
    def _identify_issues(self, inspection_data: Dict) -> List[Dict]:
        """Identify issues from inspection data"""
        issues = []
        
        # Check for specific issues reported
        reported_issues = inspection_data.get('reported_issues', [])
        
        for issue in reported_issues:
            issues.append({
                'description': issue.get('description', 'Unknown issue'),
                'category': issue.get('category', 'general'),
                'severity': issue.get('severity', 'medium'),
                'detected_date': datetime.now().isoformat()
            })
        
        # Check component scores for potential issues
        if inspection_data.get('structural_integrity', 10) < 5:
            issues.append({
                'description': 'Structural integrity concerns detected',
                'category': 'structural',
                'severity': 'critical',
                'detected_date': datetime.now().isoformat()
            })
        
        if inspection_data.get('systems_functionality', 10) < 5:
            issues.append({
                'description': 'Building systems require attention',
                'category': 'systems',
                'severity': 'high',
                'detected_date': datetime.now().isoformat()
            })
        
        return issues
    
    def _generate_maintenance_recommendations(self, score: float, 
                                            issues: List[Dict]) -> List[str]:
        """Generate maintenance recommendations"""
        recommendations = []
        
        if score < 5:
            recommendations.append("Immediate professional inspection recommended")
            recommendations.append("Address all critical issues within 30 days")
        elif score < 7:
            recommendations.append("Schedule comprehensive maintenance review")
            recommendations.append("Address identified issues within 90 days")
        else:
            recommendations.append("Continue regular maintenance schedule")
            recommendations.append("Monitor condition quarterly")
        
        # Add issue-specific recommendations
        critical_issues = [i for i in issues if i['severity'] == 'critical']
        if critical_issues:
            recommendations.append(f"URGENT: Address {len(critical_issues)} critical issue(s) immediately")
        
        high_issues = [i for i in issues if i['severity'] == 'high']
        if high_issues:
            recommendations.append(f"Address {len(high_issues)} high-priority issue(s) within 60 days")
        
        return recommendations
    
    def _estimate_repair_costs(self, issues: List[Dict]) -> Dict:
        """Estimate repair costs for identified issues"""
        severity_costs = {
            'critical': 5000,
            'high': 2000,
            'medium': 500,
            'low': 200
        }
        
        total_estimate = 0
        cost_breakdown = []
        
        for issue in issues:
            severity = issue.get('severity', 'medium')
            estimated_cost = severity_costs.get(severity, 500)
            
            total_estimate += estimated_cost
            cost_breakdown.append({
                'issue': issue['description'],
                'severity': severity,
                'estimated_cost': estimated_cost
            })
        
        return {
            'total_estimated_cost': total_estimate,
            'cost_range': {
                'minimum': round(total_estimate * 0.7, 2),
                'maximum': round(total_estimate * 1.3, 2)
            },
            'breakdown': cost_breakdown
        }
    
    def _create_issue_alerts(self, property_id: str, issues: List[Dict]):
        """Create alerts for critical issues"""
        for issue in issues:
            alert = {
                'property_id': property_id,
                'alert_type': 'critical_issue',
                'issue': issue,
                'created_at': datetime.now().isoformat(),
                'status': 'open',
                'priority': 'urgent'
            }
            self.issue_alerts.append(alert)
    
    def get_property_health_score(self, property_id: str) -> Dict:
        """
        Calculate overall property health score
        
        Args:
            property_id: Property identifier
            
        Returns:
            Property health score and metrics
        """
        if property_id not in self.condition_reports:
            return {
                'property_id': property_id,
                'message': 'No condition assessment available'
            }
        
        report = self.condition_reports[property_id]
        condition_score = report['overall_condition_score']
        
        # Calculate health score (0-100)
        health_score = condition_score * 10
        
        # Adjust for issues
        issues = report['identified_issues']
        critical_count = sum(1 for i in issues if i['severity'] == 'critical')
        high_count = sum(1 for i in issues if i['severity'] == 'high')
        
        health_score -= (critical_count * 15)
        health_score -= (high_count * 5)
        health_score = max(0, min(100, health_score))
        
        return {
            'property_id': property_id,
            'health_score': round(health_score, 2),
            'health_grade': self._get_health_grade(health_score),
            'condition_score': condition_score,
            'total_issues': len(issues),
            'critical_issues': critical_count,
            'high_priority_issues': high_count,
            'maintenance_urgency': 'immediate' if critical_count > 0 else 'high' if high_count > 0 else 'normal'
        }
    
    def _get_health_grade(self, score: float) -> str:
        """Get health grade from score"""
        if score >= 90:
            return "A - Excellent Health"
        elif score >= 75:
            return "B - Good Health"
        elif score >= 60:
            return "C - Fair Health"
        elif score >= 40:
            return "D - Poor Health"
        else:
            return "F - Critical Health"


class VendorManager:
    """Vendor management for property maintenance"""
    
    def __init__(self):
        self.vendors = {}
        self.vendor_ratings = {}
    
    def add_vendor(self, vendor_data: Dict) -> Dict:
        """
        Add a new vendor to the system
        
        Args:
            vendor_data: Vendor information
            
        Returns:
            Vendor profile
        """
        vendor_id = vendor_data.get('id', f"VND-{datetime.now().timestamp()}")
        
        vendor = {
            'vendor_id': vendor_id,
            'name': vendor_data.get('name', ''),
            'category': vendor_data.get('category', 'general'),
            'specialties': vendor_data.get('specialties', []),
            'contact': {
                'phone': vendor_data.get('phone', ''),
                'email': vendor_data.get('email', ''),
                'address': vendor_data.get('address', '')
            },
            'service_areas': vendor_data.get('service_areas', []),
            'pricing': vendor_data.get('pricing', 'competitive'),
            'availability': vendor_data.get('availability', 'unknown'),
            'rating': 5.0,
            'total_jobs': 0,
            'added_at': datetime.now().isoformat()
        }
        
        self.vendors[vendor_id] = vendor
        return vendor
    
    def recommend_vendor(self, job_category: str, location: str) -> List[Dict]:
        """
        Recommend vendors for a specific job
        
        Args:
            job_category: Type of maintenance work
            location: Job location
            
        Returns:
            List of recommended vendors
        """
        suitable_vendors = []
        
        for vendor_id, vendor in self.vendors.items():
            # Check if vendor handles this category
            if (vendor['category'] == job_category or 
                job_category in vendor['specialties']):
                
                # Check if vendor services this location
                if location in vendor['service_areas'] or 'all' in vendor['service_areas']:
                    suitable_vendors.append({
                        'vendor_id': vendor_id,
                        'name': vendor['name'],
                        'rating': vendor['rating'],
                        'total_jobs': vendor['total_jobs'],
                        'pricing': vendor['pricing'],
                        'availability': vendor['availability']
                    })
        
        # Sort by rating and experience
        suitable_vendors.sort(key=lambda x: (x['rating'], x['total_jobs']), reverse=True)
        
        return suitable_vendors
    
    def rate_vendor(self, vendor_id: str, rating: float, review: str = "") -> Dict:
        """
        Rate a vendor after job completion
        
        Args:
            vendor_id: Vendor identifier
            rating: Rating (1-5)
            review: Optional text review
            
        Returns:
            Updated vendor rating
        """
        if vendor_id not in self.vendors:
            return {'error': 'Vendor not found'}
        
        vendor = self.vendors[vendor_id]
        
        # Update rating (weighted average)
        total_jobs = vendor['total_jobs']
        current_rating = vendor['rating']
        
        new_rating = ((current_rating * total_jobs) + rating) / (total_jobs + 1)
        
        vendor['rating'] = round(new_rating, 2)
        vendor['total_jobs'] += 1
        
        # Store rating details
        if vendor_id not in self.vendor_ratings:
            self.vendor_ratings[vendor_id] = []
        
        self.vendor_ratings[vendor_id].append({
            'rating': rating,
            'review': review,
            'date': datetime.now().isoformat()
        })
        
        return {
            'vendor_id': vendor_id,
            'new_rating': vendor['rating'],
            'total_jobs': vendor['total_jobs']
        }


# Example usage and demonstration
if __name__ == "__main__":
    # Property Maintenance Management
    print("=== Property Maintenance Management ===")
    maintenance_mgr = PropertyMaintenanceManager()
    
    property_data = {
        'id': 'PROP-001',
        'age_years': 15,
        'type': 'residential'
    }
    
    schedule = maintenance_mgr.create_maintenance_schedule(property_data)
    print(f"Property: {schedule['property_id']}")
    print(f"Annual Maintenance Budget: ${schedule['annual_maintenance_budget']:,.2f}")
    print(f"\nScheduled Tasks: {len(schedule['tasks'])}")
    
    print("\nFirst 5 Maintenance Tasks:")
    for task in schedule['tasks'][:5]:
        print(f"  - {task['name']}")
        print(f"    Priority: {task['priority']}, Cost: ${task['estimated_cost']}")
        print(f"    Next Due: {task['next_due_date']}")
    
    # Upcoming Maintenance
    print("\n=== Upcoming Maintenance (Next 6 Months) ===")
    upcoming = maintenance_mgr.predict_upcoming_maintenance('PROP-001', 6)
    
    for task in upcoming[:3]:
        print(f"\n{task['task_name']}")
        print(f"  Due: {task['due_date']} ({task['days_until_due']} days)")
        print(f"  Cost: ${task['estimated_cost']}")
        print(f"  Urgency: {task['urgency']}")
    
    # Property Condition Monitoring
    print("\n=== Property Condition Assessment ===")
    condition_monitor = PropertyConditionMonitor()
    
    inspection_data = {
        'structural_integrity': 8,
        'systems_functionality': 7,
        'exterior_condition': 8,
        'interior_condition': 7,
        'reported_issues': [
            {
                'description': 'Minor roof leak in guest bedroom',
                'category': 'roofing',
                'severity': 'high'
            }
        ]
    }
    
    assessment = condition_monitor.assess_property_condition('PROP-001', inspection_data)
    print(f"Overall Condition Score: {assessment['overall_condition_score']}/10")
    print(f"Condition Grade: {assessment['condition_grade']}")
    print(f"Identified Issues: {len(assessment['identified_issues'])}")
    
    if assessment['identified_issues']:
        print("\nIssues Found:")
        for issue in assessment['identified_issues']:
            print(f"  - {issue['description']} (Severity: {issue['severity']})")
    
    print(f"\nEstimated Repair Costs: ${assessment['estimated_repair_costs']['total_estimated_cost']:,.2f}")
    
    # Property Health Score
    print("\n=== Property Health Score ===")
    health = condition_monitor.get_property_health_score('PROP-001')
    print(f"Health Score: {health['health_score']}/100")
    print(f"Health Grade: {health['health_grade']}")
    print(f"Maintenance Urgency: {health['maintenance_urgency']}")
    
    # Vendor Management
    print("\n=== Vendor Management ===")
    vendor_mgr = VendorManager()
    
    # Add sample vendors
    vendors_data = [
        {
            'id': 'VND-001',
            'name': 'ABC Roofing Services',
            'category': 'roofing',
            'specialties': ['roof repair', 'roof replacement'],
            'service_areas': ['Downtown', 'Suburbs'],
            'phone': '+1234567890'
        },
        {
            'id': 'VND-002',
            'name': 'Quality HVAC Solutions',
            'category': 'HVAC',
            'specialties': ['HVAC repair', 'AC installation'],
            'service_areas': ['all'],
            'phone': '+1234567891'
        }
    ]
    
    for vendor_data in vendors_data:
        vendor_mgr.add_vendor(vendor_data)
    
    # Get vendor recommendations
    recommendations = vendor_mgr.recommend_vendor('roofing', 'Downtown')
    print(f"Recommended Vendors for Roofing in Downtown:")
    
    for vendor in recommendations:
        print(f"  - {vendor['name']}")
        print(f"    Rating: {vendor['rating']}/5.0")
        print(f"    Jobs Completed: {vendor['total_jobs']}")
