"""
Unit tests for Ethical Compliance modules
"""

import pytest
from src.ai_modules.ethical_compliance import (
    FairHousingCompliance,
    TransparencyManager,
    DataPrivacyManager,
    AccuracyVerificationSystem
)


class TestFairHousingCompliance:
    """Test Fair Housing Compliance"""
    
    def setup_method(self):
        """Setup test fixtures"""
        self.compliance = FairHousingCompliance()
    
    def test_compliant_content(self):
        """Test content that is Fair Housing compliant"""
        content = "Beautiful 3-bedroom house with updated kitchen and spacious living room"
        result = self.compliance.check_content(content)
        
        assert result['compliant'] is True
        assert len(result['violations']) == 0
    
    def test_non_compliant_content(self):
        """Test content with Fair Housing violations"""
        content = "Perfect for adults only, no children allowed in this quiet building"
        result = self.compliance.check_content(content)
        
        assert result['compliant'] is False
        assert len(result['violations']) > 0
    
    def test_warning_content(self):
        """Test content with warning terms"""
        content = "Quiet neighborhood with active lifestyle community"
        result = self.compliance.check_content(content)
        
        assert len(result['warnings']) > 0
    
    def test_check_targeting_age_discrimination(self):
        """Test age-based targeting detection"""
        targeting = {
            'age_range': {'min': 25, 'max': 40}
        }
        result = self.compliance.check_targeting(targeting)
        
        assert result['compliant'] is False
        assert len(result['issues']) > 0
    
    def test_check_targeting_gender_discrimination(self):
        """Test gender-based targeting detection"""
        targeting = {
            'gender': 'male'
        }
        result = self.compliance.check_targeting(targeting)
        
        assert result['compliant'] is False
        assert any('gender' in issue['criterion'] for issue in result['issues'])
    
    def test_generate_compliant_description(self):
        """Test generating compliant alternative"""
        original = "Perfect for families with no children"
        result = self.compliance.generate_compliant_description(original)
        
        assert len(result['changes_made']) > 0
        assert result['compliance_verified'] is True


class TestTransparencyManager:
    """Test Transparency Manager"""
    
    def setup_method(self):
        """Setup test fixtures"""
        self.transparency = TransparencyManager()
    
    def test_add_disclosure(self):
        """Test adding disclosure to content"""
        content = "This is a property description"
        disclosed = self.transparency.add_disclosure(content, 'ai_generated_content')
        
        assert content in disclosed
        assert 'AI' in disclosed or 'ai' in disclosed.lower()
    
    def test_verify_disclosure_present(self):
        """Test disclosure verification"""
        content_with_disclosure = "Property description [This content was generated with AI assistance]"
        result = self.transparency.verify_disclosure_present(content_with_disclosure)
        
        assert result['properly_disclosed'] is True
        assert len(result['present_disclosures']) > 0
    
    def test_create_disclosure_log(self):
        """Test disclosure log creation"""
        log = self.transparency.create_disclosure_log(
            'content_generation',
            {'type': 'property_description'}
        )
        
        assert 'log_id' in log
        assert 'timestamp' in log
        assert log['disclosure_provided'] is True


class TestDataPrivacyManager:
    """Test Data Privacy Manager"""
    
    def setup_method(self):
        """Setup test fixtures"""
        self.privacy = DataPrivacyManager()
    
    def test_check_consent(self):
        """Test consent checking"""
        result = self.privacy.check_consent('CLIENT001', 'marketing')
        
        assert 'client_id' in result
        assert 'consent_given' in result
        assert 'can_proceed' in result
    
    def test_anonymize_data(self):
        """Test data anonymization"""
        data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'phone': '555-1234',
            'address': '123 Main St'
        }
        
        result = self.privacy.anonymize_data(data, ['email', 'phone'])
        
        assert result['anonymized_data']['email'] != data['email']
        assert result['anonymized_data']['phone'] != data['phone']
        assert '***' in result['anonymized_data']['email']
    
    def test_check_data_retention(self):
        """Test data retention check"""
        result = self.privacy.check_data_retention('lead_data', 400)
        
        assert result['should_retain'] is False
        assert result['action'] == 'delete'
        
        result2 = self.privacy.check_data_retention('lead_data', 100)
        assert result2['should_retain'] is True
        assert result2['action'] == 'retain'
    
    def test_encrypt_sensitive_data(self):
        """Test sensitive data encryption marking"""
        data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'ssn': '123-45-6789'
        }
        
        result = self.privacy.encrypt_sensitive_data(data)
        
        assert result['encryption_enabled'] is True
        assert len(result['fields_encrypted']) > 0
        assert 'encryption_method' in result


class TestAccuracyVerificationSystem:
    """Test Accuracy Verification System"""
    
    def setup_method(self):
        """Setup test fixtures"""
        self.verifier = AccuracyVerificationSystem()
    
    def test_verify_ai_output(self):
        """Test AI output verification"""
        output = {
            'estimated_value': 500000,
            'confidence': 0.85
        }
        
        result = self.verifier.verify_ai_output(output, 'valuation')
        
        assert 'verification_level' in result
        assert 'checks_passed' in result
        assert 'total_checks' in result
        assert result['verification_level'] == 'expert_validation'
    
    def test_flag_for_review(self):
        """Test flagging content for review"""
        content = {'id': 'PROP001', 'description': 'Property details'}
        flag = self.verifier.flag_for_review(content, 'Unusual valuation detected')
        
        assert 'flag_id' in flag
        assert flag['status'] == 'pending_review'
        assert 'reason' in flag
    
    def test_validate_sources(self):
        """Test source validation"""
        sources = [
            {'name': 'MLS Database', 'age_days': 30},
            {'name': 'Public Records', 'age_days': 500}
        ]
        
        result = self.verifier.validate_sources(sources)
        
        assert result['total_sources'] == 2
        assert 'validated_sources' in result


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
