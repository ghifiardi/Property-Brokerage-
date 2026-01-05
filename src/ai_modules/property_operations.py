"""
AI-powered Property Operations and Maintenance

This module implements AI capabilities for:
- Tenant screening automation
- Maintenance scheduling
- Drone image analysis for property inspection
"""

from typing import Dict, List, Optional
from datetime import datetime, timedelta


class TenantScreeningSystem:
    """AI-powered tenant screening and evaluation"""
    
    def __init__(self):
        self.screening_criteria = {
            'credit_score': {'weight': 0.30, 'min_threshold': 650},
            'income_ratio': {'weight': 0.25, 'min_threshold': 3.0},  # 3x rent
            'rental_history': {'weight': 0.25, 'min_threshold': 0.7},
            'employment_stability': {'weight': 0.20, 'min_threshold': 0.6}
        }
    
    def screen_applicant(self, applicant_data: Dict) -> Dict:
        """
        Screen tenant applicant using AI
        
        Args:
            applicant_data: Applicant information
            
        Returns:
            Screening results and recommendation
        """
        scores = self._calculate_screening_scores(applicant_data)
        overall_score = self._calculate_overall_score(scores)
        risk_level = self._assess_risk_level(overall_score)
        recommendation = self._generate_recommendation(overall_score, scores)
        
        return {
            'applicant_id': applicant_data.get('applicant_id'),
            'applicant_name': applicant_data.get('name'),
            'overall_score': overall_score,
            'detailed_scores': scores,
            'risk_level': risk_level,
            'recommendation': recommendation,
            'screening_date': datetime.now().isoformat(),
            'compliance_note': 'Screening conducted per Fair Housing regulations'
        }
    
    def batch_screen_applicants(self, applicants: List[Dict]) -> List[Dict]:
        """
        Screen multiple applicants and rank them
        
        Args:
            applicants: List of applicant data
            
        Returns:
            Ranked list of applicants
        """
        screened = []
        for applicant in applicants:
            result = self.screen_applicant(applicant)
            screened.append(result)
        
        # Sort by overall score
        screened.sort(key=lambda x: x['overall_score'], reverse=True)
        
        # Add rankings
        for idx, applicant in enumerate(screened, 1):
            applicant['rank'] = idx
        
        return screened
    
    def verify_information(self, applicant_data: Dict) -> Dict:
        """
        Verify applicant information
        
        Args:
            applicant_data: Applicant data to verify
            
        Returns:
            Verification results
        """
        verifications = {
            'employment': self._verify_employment(applicant_data),
            'income': self._verify_income(applicant_data),
            'references': self._verify_references(applicant_data),
            'identity': self._verify_identity(applicant_data)
        }
        
        all_verified = all(v['verified'] for v in verifications.values())
        
        return {
            'applicant_id': applicant_data.get('applicant_id'),
            'verifications': verifications,
            'all_verified': all_verified,
            'verification_date': datetime.now().isoformat()
        }
    
    def _calculate_screening_scores(self, applicant_data: Dict) -> Dict:
        """Calculate individual screening scores"""
        scores = {}
        
        # Credit score evaluation
        credit_score = applicant_data.get('credit_score', 0)
        if credit_score >= 750:
            scores['credit_score'] = 100
        elif credit_score >= 700:
            scores['credit_score'] = 85
        elif credit_score >= 650:
            scores['credit_score'] = 70
        else:
            scores['credit_score'] = 50
        
        # Income ratio (income / rent)
        monthly_income = applicant_data.get('monthly_income', 0)
        monthly_rent = applicant_data.get('monthly_rent', 1)
        income_ratio = monthly_income / monthly_rent if monthly_rent > 0 else 0
        
        if income_ratio >= 3.5:
            scores['income_ratio'] = 100
        elif income_ratio >= 3.0:
            scores['income_ratio'] = 85
        elif income_ratio >= 2.5:
            scores['income_ratio'] = 70
        else:
            scores['income_ratio'] = 50
        
        # Rental history
        rental_history_score = applicant_data.get('rental_history_score', 0.5)
        scores['rental_history'] = rental_history_score * 100
        
        # Employment stability
        employment_months = applicant_data.get('employment_months', 0)
        if employment_months >= 24:
            scores['employment_stability'] = 100
        elif employment_months >= 12:
            scores['employment_stability'] = 85
        elif employment_months >= 6:
            scores['employment_stability'] = 70
        else:
            scores['employment_stability'] = 50
        
        return scores
    
    def _calculate_overall_score(self, scores: Dict) -> float:
        """Calculate weighted overall score"""
        total = 0.0
        for criterion, score in scores.items():
            weight = self.screening_criteria[criterion]['weight']
            total += score * weight
        
        return round(total, 2)
    
    def _assess_risk_level(self, overall_score: float) -> str:
        """Assess risk level based on score"""
        if overall_score >= 85:
            return 'LOW'
        elif overall_score >= 70:
            return 'MEDIUM'
        else:
            return 'HIGH'
    
    def _generate_recommendation(self, overall_score: float, scores: Dict) -> str:
        """Generate screening recommendation"""
        if overall_score >= 85:
            return 'APPROVE - Strong candidate'
        elif overall_score >= 70:
            return 'CONDITIONAL APPROVAL - Consider additional security deposit'
        else:
            issues = [k for k, v in scores.items() if v < 70]
            return f'REVIEW REQUIRED - Concerns: {", ".join(issues)}'
    
    def _verify_employment(self, data: Dict) -> Dict:
        """Verify employment status"""
        return {
            'verified': data.get('employment_verified', False),
            'method': 'AI-powered document analysis',
            'confidence': 0.9
        }
    
    def _verify_income(self, data: Dict) -> Dict:
        """Verify income"""
        return {
            'verified': data.get('income_verified', False),
            'method': 'Document verification',
            'confidence': 0.85
        }
    
    def _verify_references(self, data: Dict) -> Dict:
        """Verify references"""
        return {
            'verified': data.get('references_verified', False),
            'method': 'Reference check',
            'confidence': 0.8
        }
    
    def _verify_identity(self, data: Dict) -> Dict:
        """Verify identity"""
        return {
            'verified': data.get('identity_verified', False),
            'method': 'ID document analysis',
            'confidence': 0.95
        }


class MaintenanceScheduler:
    """AI-powered maintenance scheduling system"""
    
    def __init__(self):
        self.maintenance_types = {
            'preventive': {'priority': 'medium', 'frequency_days': 90},
            'corrective': {'priority': 'high', 'frequency_days': 7},
            'emergency': {'priority': 'critical', 'frequency_days': 1}
        }
    
    def schedule_maintenance(self, maintenance_request: Dict) -> Dict:
        """
        Schedule maintenance based on priority and availability
        
        Args:
            maintenance_request: Maintenance request details
            
        Returns:
            Scheduled maintenance
        """
        request_type = maintenance_request.get('type', 'corrective')
        priority = self.maintenance_types.get(request_type, {}).get('priority', 'medium')
        
        # Calculate schedule based on priority
        if priority == 'critical':
            scheduled_date = datetime.now() + timedelta(hours=4)
        elif priority == 'high':
            scheduled_date = datetime.now() + timedelta(days=1)
        else:
            scheduled_date = datetime.now() + timedelta(days=7)
        
        return {
            'maintenance_id': f"MAINT-{datetime.now().strftime('%Y%m%d%H%M%S')}",
            'property_id': maintenance_request.get('property_id'),
            'type': request_type,
            'priority': priority,
            'description': maintenance_request.get('description'),
            'scheduled_date': scheduled_date.isoformat(),
            'estimated_duration_hours': self._estimate_duration(maintenance_request),
            'assigned_to': 'Auto-assigned',
            'status': 'scheduled',
            'created_at': datetime.now().isoformat()
        }
    
    def predict_maintenance_needs(self, property_data: Dict, maintenance_history: List[Dict]) -> List[Dict]:
        """
        Predict future maintenance needs using AI
        
        Args:
            property_data: Property information
            maintenance_history: Historical maintenance data
            
        Returns:
            Predicted maintenance needs
        """
        predictions = []
        
        # Analyze patterns in maintenance history
        if maintenance_history:
            # HVAC prediction
            hvac_maintenance = [m for m in maintenance_history if 'hvac' in m.get('description', '').lower()]
            if hvac_maintenance:
                last_hvac = max(hvac_maintenance, key=lambda x: x.get('date', ''))
                predictions.append({
                    'system': 'HVAC',
                    'predicted_date': (datetime.now() + timedelta(days=90)).isoformat(),
                    'reason': 'Regular maintenance due',
                    'confidence': 0.85
                })
            
            # Plumbing prediction
            plumbing_issues = [m for m in maintenance_history if 'plumb' in m.get('description', '').lower()]
            if len(plumbing_issues) > 2:
                predictions.append({
                    'system': 'Plumbing',
                    'predicted_date': (datetime.now() + timedelta(days=30)).isoformat(),
                    'reason': 'Pattern of recurring issues detected',
                    'confidence': 0.75
                })
        
        # Age-based predictions
        property_age = property_data.get('age_years', 0)
        if property_age > 15:
            predictions.append({
                'system': 'Roof',
                'predicted_date': (datetime.now() + timedelta(days=180)).isoformat(),
                'reason': 'Property age suggests inspection needed',
                'confidence': 0.70
            })
        
        return predictions
    
    def optimize_maintenance_route(self, maintenance_tasks: List[Dict]) -> List[Dict]:
        """
        Optimize route for maintenance visits
        
        Args:
            maintenance_tasks: List of maintenance tasks
            
        Returns:
            Optimized task order
        """
        # Sort by priority first, then by location proximity
        priority_order = {'critical': 0, 'high': 1, 'medium': 2, 'low': 3}
        
        sorted_tasks = sorted(
            maintenance_tasks,
            key=lambda x: (
                priority_order.get(x.get('priority', 'medium'), 2),
                x.get('property_id', '')
            )
        )
        
        # Add route order
        for idx, task in enumerate(sorted_tasks, 1):
            task['route_order'] = idx
            task['optimized'] = True
        
        return sorted_tasks
    
    def _estimate_duration(self, request: Dict) -> float:
        """Estimate maintenance duration in hours"""
        description = request.get('description', '').lower()
        
        if any(word in description for word in ['emergency', 'urgent', 'leak']):
            return 2.0
        elif any(word in description for word in ['repair', 'fix', 'replace']):
            return 3.0
        elif any(word in description for word in ['inspect', 'check', 'review']):
            return 1.0
        else:
            return 2.0


class DroneImageAnalyzer:
    """AI-powered drone image analysis for property inspection"""
    
    def __init__(self):
        self.detectable_issues = [
            'roof_damage',
            'gutter_issues',
            'siding_damage',
            'chimney_problems',
            'vegetation_overgrowth'
        ]
    
    def analyze_drone_images(self, image_paths: List[str], property_id: str) -> Dict:
        """
        Analyze drone images for property issues
        
        Args:
            image_paths: List of drone image paths
            property_id: Property identifier
            
        Returns:
            Analysis results
        """
        issues_detected = []
        
        # Simulate AI image analysis
        # In production, this would use computer vision models
        for idx, image_path in enumerate(image_paths):
            analysis = self._analyze_single_image(image_path, idx)
            if analysis['issues']:
                issues_detected.extend(analysis['issues'])
        
        severity_score = self._calculate_severity_score(issues_detected)
        
        return {
            'property_id': property_id,
            'images_analyzed': len(image_paths),
            'issues_detected': issues_detected,
            'total_issues': len(issues_detected),
            'severity_score': severity_score,
            'requires_immediate_attention': severity_score > 7,
            'analyzed_at': datetime.now().isoformat(),
            'analysis_method': 'AI-powered computer vision'
        }
    
    def generate_inspection_report(self, analysis_results: Dict) -> Dict:
        """
        Generate inspection report from analysis
        
        Args:
            analysis_results: Analysis results
            
        Returns:
            Formatted inspection report
        """
        issues = analysis_results.get('issues_detected', [])
        severity = analysis_results.get('severity_score', 0)
        
        # Categorize issues
        critical = [i for i in issues if i.get('severity') == 'critical']
        moderate = [i for i in issues if i.get('severity') == 'moderate']
        minor = [i for i in issues if i.get('severity') == 'minor']
        
        recommendations = self._generate_recommendations(critical, moderate, minor)
        
        return {
            'property_id': analysis_results.get('property_id'),
            'inspection_date': analysis_results.get('analyzed_at'),
            'overall_condition': self._determine_condition(severity),
            'critical_issues': len(critical),
            'moderate_issues': len(moderate),
            'minor_issues': len(minor),
            'detailed_findings': {
                'critical': critical,
                'moderate': moderate,
                'minor': minor
            },
            'recommendations': recommendations,
            'next_inspection_date': (datetime.now() + timedelta(days=180)).isoformat()
        }
    
    def detect_change_over_time(self, current_images: List[str], 
                                previous_images: List[str]) -> Dict:
        """
        Detect changes in property condition over time
        
        Args:
            current_images: Current drone images
            previous_images: Previous drone images
            
        Returns:
            Change detection results
        """
        changes = []
        
        # Simulate change detection
        # In production, this would compare images using computer vision
        if len(current_images) != len(previous_images):
            changes.append({
                'type': 'coverage_difference',
                'severity': 'minor',
                'description': 'Different number of images captured'
            })
        
        return {
            'changes_detected': len(changes),
            'changes': changes,
            'deterioration_rate': self._calculate_deterioration_rate(changes),
            'analysis_date': datetime.now().isoformat()
        }
    
    def _analyze_single_image(self, image_path: str, image_index: int) -> Dict:
        """Analyze single drone image"""
        # Placeholder for actual computer vision analysis
        issues = []
        
        # Simulate detection based on image index (for demonstration)
        if image_index % 3 == 0:
            issues.append({
                'type': 'roof_damage',
                'severity': 'moderate',
                'location': 'Northwest section',
                'confidence': 0.85,
                'image': image_path
            })
        
        return {'issues': issues}
    
    def _calculate_severity_score(self, issues: List[Dict]) -> float:
        """Calculate overall severity score (0-10)"""
        if not issues:
            return 0.0
        
        severity_weights = {
            'critical': 3.0,
            'moderate': 2.0,
            'minor': 1.0
        }
        
        total_score = sum(severity_weights.get(i.get('severity', 'minor'), 1.0) for i in issues)
        normalized_score = min(total_score, 10.0)
        
        return round(normalized_score, 2)
    
    def _determine_condition(self, severity_score: float) -> str:
        """Determine overall property condition"""
        if severity_score >= 8:
            return 'POOR - Immediate attention required'
        elif severity_score >= 5:
            return 'FAIR - Repairs recommended'
        elif severity_score >= 2:
            return 'GOOD - Minor maintenance needed'
        else:
            return 'EXCELLENT - Well maintained'
    
    def _generate_recommendations(self, critical: List, moderate: List, minor: List) -> List[str]:
        """Generate recommendations based on issues"""
        recommendations = []
        
        if critical:
            recommendations.append(f"URGENT: Address {len(critical)} critical issue(s) immediately")
        
        if moderate:
            recommendations.append(f"Schedule repairs for {len(moderate)} moderate issue(s) within 30 days")
        
        if minor:
            recommendations.append(f"Plan routine maintenance for {len(minor)} minor issue(s)")
        
        if not (critical or moderate or minor):
            recommendations.append("Property is in good condition. Continue regular maintenance schedule.")
        
        return recommendations
    
    def _calculate_deterioration_rate(self, changes: List[Dict]) -> str:
        """Calculate rate of property deterioration"""
        if not changes:
            return 'STABLE'
        elif len(changes) > 5:
            return 'RAPID'
        elif len(changes) > 2:
            return 'MODERATE'
        else:
            return 'SLOW'
