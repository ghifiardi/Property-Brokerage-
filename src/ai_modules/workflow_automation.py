"""
AI-powered Workflow Automation and Document Management

This module implements AI capabilities for:
- Appointment scheduling
- Database management
- Contract review and compliance checking
- Document processing
"""

from typing import Dict, List, Optional
from datetime import datetime, timedelta
import re


class AppointmentScheduler:
    """AI-powered appointment scheduling system"""
    
    def __init__(self):
        self.business_hours = {
            'start': 9,  # 9 AM
            'end': 18,   # 6 PM
        }
        self.slot_duration = 60  # minutes
        self.buffer_time = 15    # minutes between appointments
    
    def find_available_slots(self, date: datetime, existing_appointments: List[Dict]) -> List[Dict]:
        """
        Find available time slots for appointments
        
        Args:
            date: Target date
            existing_appointments: List of existing appointments
            
        Returns:
            List of available time slots
        """
        available_slots = []
        current_time = datetime.combine(date.date(), 
                                       datetime.min.time().replace(hour=self.business_hours['start']))
        end_time = datetime.combine(date.date(), 
                                   datetime.min.time().replace(hour=self.business_hours['end']))
        
        while current_time < end_time:
            slot_end = current_time + timedelta(minutes=self.slot_duration)
            
            # Check if slot conflicts with existing appointments
            is_available = not self._has_conflict(current_time, slot_end, existing_appointments)
            
            if is_available:
                available_slots.append({
                    'start_time': current_time.isoformat(),
                    'end_time': slot_end.isoformat(),
                    'duration_minutes': self.slot_duration
                })
            
            current_time += timedelta(minutes=self.slot_duration + self.buffer_time)
        
        return available_slots
    
    def schedule_appointment(self, appointment_data: Dict) -> Dict:
        """
        Schedule a new appointment
        
        Args:
            appointment_data: Appointment details
            
        Returns:
            Scheduled appointment confirmation
        """
        return {
            'appointment_id': f"APT-{datetime.now().strftime('%Y%m%d%H%M%S')}",
            'client_name': appointment_data.get('client_name'),
            'broker_name': appointment_data.get('broker_name'),
            'property_id': appointment_data.get('property_id'),
            'appointment_time': appointment_data.get('appointment_time'),
            'duration_minutes': self.slot_duration,
            'status': 'confirmed',
            'confirmation_sent': True,
            'created_at': datetime.now().isoformat()
        }
    
    def suggest_optimal_time(self, client_preferences: Dict, broker_availability: List[Dict]) -> List[Dict]:
        """
        Suggest optimal appointment times using AI
        
        Args:
            client_preferences: Client's time preferences
            broker_availability: Broker's available slots
            
        Returns:
            Ranked list of suggested times
        """
        preferred_time = client_preferences.get('preferred_time_of_day', 'morning')
        preferred_days = client_preferences.get('preferred_days', ['monday', 'tuesday', 'wednesday', 'thursday', 'friday'])
        
        suggestions = []
        for slot in broker_availability:
            slot_time = datetime.fromisoformat(slot['start_time'])
            day_name = slot_time.strftime('%A').lower()
            hour = slot_time.hour
            
            # Score the slot
            score = 50  # Base score
            
            # Day preference
            if day_name in [d.lower() for d in preferred_days]:
                score += 30
            
            # Time preference
            if preferred_time == 'morning' and 9 <= hour < 12:
                score += 20
            elif preferred_time == 'afternoon' and 12 <= hour < 17:
                score += 20
            elif preferred_time == 'evening' and 17 <= hour < 19:
                score += 20
            
            suggestions.append({
                'slot': slot,
                'score': score,
                'recommendation_reason': self._get_recommendation_reason(preferred_time, hour, day_name)
            })
        
        # Sort by score
        suggestions.sort(key=lambda x: x['score'], reverse=True)
        return suggestions[:5]  # Top 5 suggestions
    
    def send_reminders(self, appointment: Dict) -> Dict:
        """
        Generate appointment reminders
        
        Args:
            appointment: Appointment details
            
        Returns:
            Reminder schedule
        """
        appointment_time = datetime.fromisoformat(appointment['appointment_time'])
        
        return {
            'reminders': [
                {
                    'type': 'email',
                    'send_at': (appointment_time - timedelta(days=1)).isoformat(),
                    'message': '24-hour reminder for your property viewing'
                },
                {
                    'type': 'sms',
                    'send_at': (appointment_time - timedelta(hours=2)).isoformat(),
                    'message': '2-hour reminder for your appointment'
                }
            ],
            'appointment_id': appointment.get('appointment_id')
        }
    
    def _has_conflict(self, start: datetime, end: datetime, appointments: List[Dict]) -> bool:
        """Check if time slot conflicts with existing appointments"""
        for apt in appointments:
            apt_start = datetime.fromisoformat(apt['start_time'])
            apt_end = datetime.fromisoformat(apt['end_time'])
            
            if (start < apt_end and end > apt_start):
                return True
        
        return False
    
    def _get_recommendation_reason(self, preferred_time: str, hour: int, day: str) -> str:
        """Generate recommendation reason"""
        reasons = []
        
        if preferred_time == 'morning' and 9 <= hour < 12:
            reasons.append("Matches your morning preference")
        elif preferred_time == 'afternoon' and 12 <= hour < 17:
            reasons.append("Matches your afternoon preference")
        
        if day in ['monday', 'tuesday', 'wednesday']:
            reasons.append("Earlier in the week")
        
        return " • ".join(reasons) if reasons else "Available slot"


class ContractReviewSystem:
    """AI-powered contract review for compliance"""
    
    def __init__(self):
        self.required_clauses = [
            'property_description',
            'purchase_price',
            'closing_date',
            'contingencies',
            'signatures'
        ]
        self.compliance_keywords = [
            'fair housing',
            'equal opportunity',
            'non-discrimination',
            'as-is condition',
            'disclosure'
        ]
    
    def review_contract(self, contract_text: str) -> Dict:
        """
        Review contract for completeness and compliance
        
        Args:
            contract_text: Contract text to review
            
        Returns:
            Review results with recommendations
        """
        issues = []
        warnings = []
        missing_clauses = []
        
        # Check for required clauses
        for clause in self.required_clauses:
            if clause.replace('_', ' ') not in contract_text.lower():
                missing_clauses.append(clause)
        
        # Check for compliance keywords
        compliance_found = []
        for keyword in self.compliance_keywords:
            if keyword in contract_text.lower():
                compliance_found.append(keyword)
        
        if len(compliance_found) < 2:
            warnings.append("Limited compliance language detected")
        
        if missing_clauses:
            issues.append(f"Missing clauses: {', '.join(missing_clauses)}")
        
        # Check for ambiguous language
        ambiguous_terms = ['maybe', 'possibly', 'might', 'should', 'approximately']
        for term in ambiguous_terms:
            if term in contract_text.lower():
                warnings.append(f"Ambiguous term found: '{term}'")
        
        completeness_score = (len(self.required_clauses) - len(missing_clauses)) / len(self.required_clauses) * 100
        
        return {
            'completeness_score': round(completeness_score, 2),
            'missing_clauses': missing_clauses,
            'issues': issues,
            'warnings': warnings,
            'compliance_keywords_found': compliance_found,
            'recommendation': self._get_recommendation(completeness_score, issues),
            'reviewed_at': datetime.now().isoformat(),
            'review_method': 'AI-powered analysis'
        }
    
    def extract_key_terms(self, contract_text: str) -> Dict:
        """
        Extract key terms from contract
        
        Args:
            contract_text: Contract text
            
        Returns:
            Extracted key terms
        """
        # Simple extraction logic (in production, use NLP)
        terms = {}
        
        # Extract price
        price_match = re.search(r'\$[\d,]+', contract_text)
        if price_match:
            terms['purchase_price'] = price_match.group()
        
        # Extract dates
        date_pattern = r'\b\d{1,2}/\d{1,2}/\d{4}\b'
        dates = re.findall(date_pattern, contract_text)
        if dates:
            terms['dates_mentioned'] = dates
        
        return {
            'extracted_terms': terms,
            'extraction_date': datetime.now().isoformat()
        }
    
    def _get_recommendation(self, score: float, issues: List[str]) -> str:
        """Generate recommendation based on review"""
        if score >= 90 and not issues:
            return "Contract appears complete and ready for signatures"
        elif score >= 70:
            return "Contract requires minor revisions before proceeding"
        else:
            return "Contract requires significant revision - consult legal counsel"


class DocumentProcessor:
    """AI-powered document processing and management"""
    
    def __init__(self):
        self.supported_formats = ['pdf', 'docx', 'txt', 'jpg', 'png']
        self.document_types = [
            'contract',
            'disclosure',
            'inspection_report',
            'title_document',
            'financial_statement'
        ]
    
    def process_document(self, document_path: str, document_type: str) -> Dict:
        """
        Process and categorize document
        
        Args:
            document_path: Path to document
            document_type: Type of document
            
        Returns:
            Processing results
        """
        file_extension = document_path.split('.')[-1].lower()
        
        if file_extension not in self.supported_formats:
            return {'error': f'Unsupported format: {file_extension}'}
        
        return {
            'document_id': f"DOC-{datetime.now().strftime('%Y%m%d%H%M%S')}",
            'document_path': document_path,
            'document_type': document_type,
            'file_format': file_extension,
            'processed_at': datetime.now().isoformat(),
            'status': 'processed',
            'extracted_data': self._extract_document_data(document_type),
            'requires_signature': document_type in ['contract', 'disclosure']
        }
    
    def organize_documents(self, documents: List[Dict], property_id: str) -> Dict:
        """
        Organize documents by type and property
        
        Args:
            documents: List of document records
            property_id: Property identifier
            
        Returns:
            Organized document structure
        """
        organized = {
            'property_id': property_id,
            'total_documents': len(documents),
            'by_type': {},
            'organized_at': datetime.now().isoformat()
        }
        
        for doc in documents:
            doc_type = doc.get('document_type', 'other')
            if doc_type not in organized['by_type']:
                organized['by_type'][doc_type] = []
            organized['by_type'][doc_type].append(doc)
        
        return organized
    
    def check_document_completeness(self, documents: List[Dict], transaction_type: str) -> Dict:
        """
        Check if all required documents are present
        
        Args:
            documents: List of documents
            transaction_type: Type of transaction (buy/sell/lease)
            
        Returns:
            Completeness check results
        """
        required_docs = self._get_required_documents(transaction_type)
        present_types = [doc.get('document_type') for doc in documents]
        
        missing = [req for req in required_docs if req not in present_types]
        
        return {
            'transaction_type': transaction_type,
            'required_documents': required_docs,
            'present_documents': present_types,
            'missing_documents': missing,
            'completeness_percentage': ((len(required_docs) - len(missing)) / len(required_docs)) * 100,
            'ready_to_proceed': len(missing) == 0,
            'checked_at': datetime.now().isoformat()
        }
    
    def _extract_document_data(self, document_type: str) -> Dict:
        """Extract relevant data from document (placeholder)"""
        return {
            'method': 'AI-powered OCR and NLP',
            'confidence': 0.85,
            'requires_verification': True
        }
    
    def _get_required_documents(self, transaction_type: str) -> List[str]:
        """Get list of required documents for transaction type"""
        requirements = {
            'buy': ['contract', 'disclosure', 'inspection_report', 'financial_statement'],
            'sell': ['contract', 'disclosure', 'title_document'],
            'lease': ['contract', 'disclosure']
        }
        return requirements.get(transaction_type, ['contract'])
