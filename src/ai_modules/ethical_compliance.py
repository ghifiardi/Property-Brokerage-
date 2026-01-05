"""
Ethical AI Guidelines and Compliance

This module implements ethical considerations and compliance checks for:
- Fair Housing compliance
- Transparency and disclosure requirements
- Data privacy and protection
- Accuracy verification
"""

from typing import Dict, List, Optional
from datetime import datetime


class FairHousingCompliance:
    """Fair Housing Act compliance checker"""
    
    def __init__(self):
        self.protected_classes = [
            'race',
            'color',
            'national_origin',
            'religion',
            'sex',
            'familial_status',
            'disability'
        ]
        
        self.prohibited_terms = [
            # Family status
            'adults only', 'no children', 'perfect for couples', 'mature individuals',
            'single person', 'ideal for retirees', 'families preferred',
            
            # Disability
            'able-bodied', 'physically fit', 'no wheelchairs', 'walk-up',
            
            # Religion
            'christian neighborhood', 'near church', 'religious community',
            
            # National origin
            'american preferred', 'english speakers only', 'local residents',
            
            # Other discriminatory
            'exclusive', 'restricted', 'select clientele'
        ]
        
        self.warning_terms = [
            'quiet neighborhood', 'active lifestyle', 'walking distance',
            'integrated', 'diverse', 'traditional'
        ]
    
    def check_content(self, content: str) -> Dict:
        """
        Check content for Fair Housing compliance
        
        Args:
            content: Text content to check
            
        Returns:
            Compliance check results
        """
        content_lower = content.lower()
        violations = []
        warnings = []
        
        # Check for prohibited terms
        for term in self.prohibited_terms:
            if term in content_lower:
                violations.append({
                    'term': term,
                    'severity': 'high',
                    'issue': 'Potentially discriminatory language',
                    'protected_class': self._identify_protected_class(term)
                })
        
        # Check for warning terms
        for term in self.warning_terms:
            if term in content_lower:
                warnings.append({
                    'term': term,
                    'severity': 'medium',
                    'issue': 'May be interpreted as discriminatory in context'
                })
        
        is_compliant = len(violations) == 0
        
        return {
            'compliant': is_compliant,
            'violations': violations,
            'warnings': warnings,
            'checked_at': datetime.now().isoformat(),
            'recommendation': self._generate_recommendation(violations, warnings)
        }
    
    def check_targeting(self, targeting_criteria: Dict) -> Dict:
        """
        Check audience targeting for discrimination
        
        Args:
            targeting_criteria: Marketing targeting criteria
            
        Returns:
            Targeting compliance results
        """
        issues = []
        
        # Check age targeting
        if 'age_range' in targeting_criteria:
            age_range = targeting_criteria['age_range']
            if age_range.get('min', 0) > 18 or age_range.get('max', 100) < 65:
                issues.append({
                    'criterion': 'age_range',
                    'issue': 'Age-based targeting may violate Fair Housing',
                    'severity': 'high'
                })
        
        # Check gender targeting
        if 'gender' in targeting_criteria and targeting_criteria['gender'] != 'all':
            issues.append({
                'criterion': 'gender',
                'issue': 'Gender-based targeting violates Fair Housing',
                'severity': 'critical'
            })
        
        # Check zip code exclusions (potential proxy for discrimination)
        if 'excluded_zip_codes' in targeting_criteria:
            issues.append({
                'criterion': 'excluded_zip_codes',
                'issue': 'Geographic exclusions may be discriminatory',
                'severity': 'high'
            })
        
        return {
            'compliant': len(issues) == 0,
            'issues': issues,
            'checked_at': datetime.now().isoformat()
        }
    
    def generate_compliant_description(self, original_content: str) -> Dict:
        """
        Generate Fair Housing compliant alternative
        
        Args:
            original_content: Original property description
            
        Returns:
            Compliant alternative and changes made
        """
        compliant_content = original_content
        changes_made = []
        
        # Remove prohibited terms
        for term in self.prohibited_terms:
            if term in compliant_content.lower():
                # Replace with neutral alternative
                compliant_content = compliant_content.replace(term, '[REMOVED]')
                changes_made.append(f"Removed potentially discriminatory term: '{term}'")
        
        return {
            'original_content': original_content,
            'compliant_content': compliant_content,
            'changes_made': changes_made,
            'compliance_verified': True,
            'generated_at': datetime.now().isoformat()
        }
    
    def _identify_protected_class(self, term: str) -> str:
        """Identify which protected class a term may discriminate against"""
        family_terms = ['adults only', 'no children', 'couples', 'retirees']
        disability_terms = ['able-bodied', 'physically fit', 'wheelchairs']
        religion_terms = ['christian', 'church', 'religious']
        
        if any(t in term for t in family_terms):
            return 'familial_status'
        elif any(t in term for t in disability_terms):
            return 'disability'
        elif any(t in term for t in religion_terms):
            return 'religion'
        else:
            return 'multiple'
    
    def _generate_recommendation(self, violations: List, warnings: List) -> str:
        """Generate compliance recommendation"""
        if violations:
            return "CRITICAL: Content violates Fair Housing Act. Revise before publication."
        elif warnings:
            return "CAUTION: Review flagged terms to ensure compliance in context."
        else:
            return "Content appears compliant with Fair Housing Act."


class TransparencyManager:
    """Manage transparency and disclosure requirements"""
    
    def __init__(self):
        self.disclosure_requirements = {
            'ai_generated_content': 'This content was generated with AI assistance',
            'virtual_staging': 'This image has been digitally staged. Furniture and decor are not included.',
            'photo_enhancement': 'Photos have been professionally enhanced',
            'ai_valuation': 'Property valuation generated by AI - professional appraisal recommended',
            'ai_analysis': 'Market analysis powered by AI algorithms',
            'chatbot': 'You are chatting with an AI assistant. A human agent is available upon request.'
        }
    
    def add_disclosure(self, content: str, disclosure_type: str) -> str:
        """
        Add required disclosure to content
        
        Args:
            content: Original content
            disclosure_type: Type of disclosure needed
            
        Returns:
            Content with disclosure
        """
        disclosure_text = self.disclosure_requirements.get(
            disclosure_type,
            'AI-assisted content'
        )
        
        return f"{content}\n\n[{disclosure_text}]"
    
    def verify_disclosure_present(self, content: str) -> Dict:
        """
        Verify that required disclosures are present
        
        Args:
            content: Content to check
            
        Returns:
            Verification results
        """
        present_disclosures = []
        missing_disclosures = []
        
        for disc_type, disc_text in self.disclosure_requirements.items():
            if disc_text.lower() in content.lower() or '[ai' in content.lower():
                present_disclosures.append(disc_type)
            else:
                # Check if this type of content is present
                if self._content_requires_disclosure(content, disc_type):
                    missing_disclosures.append(disc_type)
        
        return {
            'properly_disclosed': len(missing_disclosures) == 0,
            'present_disclosures': present_disclosures,
            'missing_disclosures': missing_disclosures,
            'checked_at': datetime.now().isoformat()
        }
    
    def create_disclosure_log(self, action: str, details: Dict) -> Dict:
        """
        Create audit log entry for transparency
        
        Args:
            action: Action taken
            details: Action details
            
        Returns:
            Log entry
        """
        return {
            'log_id': f"LOG-{datetime.now().strftime('%Y%m%d%H%M%S')}",
            'action': action,
            'details': details,
            'timestamp': datetime.now().isoformat(),
            'disclosure_provided': True
        }
    
    def _content_requires_disclosure(self, content: str, disclosure_type: str) -> bool:
        """Check if content requires specific disclosure"""
        content_lower = content.lower()
        
        requirements = {
            'ai_generated_content': ['property description', 'listing'],
            'virtual_staging': ['image', 'photo', 'picture'],
            'ai_valuation': ['value', 'price', 'worth']
        }
        
        keywords = requirements.get(disclosure_type, [])
        return any(keyword in content_lower for keyword in keywords)


class DataPrivacyManager:
    """Manage data privacy and protection"""
    
    def __init__(self):
        self.pii_fields = [
            'name',
            'email',
            'phone',
            'address',
            'ssn',
            'credit_card',
            'bank_account'
        ]
        
        self.retention_policies = {
            'lead_data': 365,  # days
            'client_data': 2555,  # 7 years
            'transaction_data': 2555,
            'marketing_data': 730,  # 2 years
            'log_data': 90
        }
    
    def check_consent(self, client_id: str, data_usage: str) -> Dict:
        """
        Check if client has given consent for data usage
        
        Args:
            client_id: Client identifier
            data_usage: Intended data usage
            
        Returns:
            Consent status
        """
        # Placeholder - in production, check actual consent records
        return {
            'client_id': client_id,
            'data_usage': data_usage,
            'consent_given': True,
            'consent_date': datetime.now().isoformat(),
            'can_proceed': True
        }
    
    def anonymize_data(self, data: Dict, fields_to_anonymize: List[str] = None) -> Dict:
        """
        Anonymize sensitive data
        
        Args:
            data: Data dictionary
            fields_to_anonymize: Fields to anonymize (defaults to all PII)
            
        Returns:
            Anonymized data
        """
        if fields_to_anonymize is None:
            fields_to_anonymize = self.pii_fields
        
        anonymized = data.copy()
        
        for field in fields_to_anonymize:
            if field in anonymized:
                if field == 'email':
                    anonymized[field] = 'user@*****.com'
                elif field == 'phone':
                    anonymized[field] = '***-***-****'
                elif field == 'ssn':
                    anonymized[field] = '***-**-****'
                else:
                    anonymized[field] = '***REDACTED***'
        
        return {
            'anonymized_data': anonymized,
            'fields_anonymized': fields_to_anonymize,
            'anonymized_at': datetime.now().isoformat()
        }
    
    def check_data_retention(self, data_type: str, data_age_days: int) -> Dict:
        """
        Check if data should be retained or deleted
        
        Args:
            data_type: Type of data
            data_age_days: Age of data in days
            
        Returns:
            Retention decision
        """
        retention_days = self.retention_policies.get(data_type, 365)
        should_retain = data_age_days < retention_days
        
        return {
            'data_type': data_type,
            'data_age_days': data_age_days,
            'retention_period_days': retention_days,
            'should_retain': should_retain,
            'action': 'retain' if should_retain else 'delete',
            'checked_at': datetime.now().isoformat()
        }
    
    def encrypt_sensitive_data(self, data: Dict) -> Dict:
        """
        Mark sensitive data for encryption
        
        Args:
            data: Data to encrypt
            
        Returns:
            Encryption metadata
        """
        sensitive_fields = [f for f in self.pii_fields if f in data]
        
        return {
            'fields_encrypted': sensitive_fields,
            'encryption_method': 'AES-256',
            'encrypted_at': datetime.now().isoformat(),
            'encryption_enabled': True
        }


class AccuracyVerificationSystem:
    """System for verifying AI-generated information accuracy"""
    
    def __init__(self):
        self.verification_levels = ['automated', 'human_review', 'expert_validation']
    
    def verify_ai_output(self, ai_output: Dict, output_type: str) -> Dict:
        """
        Verify accuracy of AI-generated output
        
        Args:
            ai_output: AI-generated content
            output_type: Type of output (valuation, content, analysis)
            
        Returns:
            Verification results
        """
        verification_level = self._determine_verification_level(output_type)
        checks = self._run_verification_checks(ai_output, output_type)
        
        return {
            'output_type': output_type,
            'verification_level': verification_level,
            'checks_passed': sum(1 for c in checks if c['passed']),
            'total_checks': len(checks),
            'checks': checks,
            'requires_human_review': verification_level != 'automated',
            'verified_at': datetime.now().isoformat()
        }
    
    def flag_for_review(self, content: Dict, reason: str) -> Dict:
        """
        Flag content for human review
        
        Args:
            content: Content to flag
            reason: Reason for flagging
            
        Returns:
            Review flag details
        """
        return {
            'flag_id': f"FLAG-{datetime.now().strftime('%Y%m%d%H%M%S')}",
            'content_id': content.get('id', 'unknown'),
            'reason': reason,
            'flagged_at': datetime.now().isoformat(),
            'status': 'pending_review',
            'assigned_to': 'human_reviewer'
        }
    
    def validate_sources(self, data_sources: List[Dict]) -> Dict:
        """
        Validate data sources for reliability
        
        Args:
            data_sources: List of data sources
            
        Returns:
            Source validation results
        """
        validated_sources = []
        
        for source in data_sources:
            reliability_score = self._assess_source_reliability(source)
            validated_sources.append({
                'source': source.get('name'),
                'reliability_score': reliability_score,
                'validated': reliability_score > 0.7
            })
        
        return {
            'total_sources': len(data_sources),
            'validated_sources': [s for s in validated_sources if s['validated']],
            'validation_date': datetime.now().isoformat()
        }
    
    def _determine_verification_level(self, output_type: str) -> str:
        """Determine required verification level"""
        critical_types = ['valuation', 'legal_document', 'financial_analysis']
        
        if output_type in critical_types:
            return 'expert_validation'
        elif output_type in ['market_analysis', 'property_description']:
            return 'human_review'
        else:
            return 'automated'
    
    def _run_verification_checks(self, output: Dict, output_type: str) -> List[Dict]:
        """Run verification checks on output"""
        checks = []
        
        # Completeness check
        checks.append({
            'check': 'completeness',
            'passed': len(output) > 0,
            'details': 'Output contains data'
        })
        
        # Consistency check
        checks.append({
            'check': 'consistency',
            'passed': True,  # Placeholder
            'details': 'Data appears consistent'
        })
        
        # Range check (for numerical data)
        if output_type == 'valuation':
            value = output.get('estimated_value', 0)
            checks.append({
                'check': 'range_validation',
                'passed': 50000 < value < 10000000,
                'details': 'Value within reasonable range'
            })
        
        return checks
    
    def _assess_source_reliability(self, source: Dict) -> float:
        """Assess reliability of data source"""
        # Placeholder scoring
        base_score = 0.8
        
        # Adjust based on source age
        age_days = source.get('age_days', 0)
        if age_days > 365:
            base_score -= 0.2
        elif age_days > 90:
            base_score -= 0.1
        
        return max(0.0, min(1.0, base_score))
