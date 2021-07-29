import os

from django.core.exceptions import ValidationError
import django
from django.test import TestCase
from ..form_validators.informed_consent_validator import InformedConsentFormValidator


# os.environ['DJANGO_SETTINGS_MODULE'] = 'training_subject_validation.settings'
# django.setup()


class InformedConsentValidatorTests(TestCase):

    def test_man_question_required_invalid(self):
        """
        Test if a question will be required for a particular gender
        """
        data = {
            'gender': 'M',
        }

        form = InformedConsentFormValidator(cleaned_data=data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('man_question', form._errors)

    def test_woman_question_required_invalid(self):
        """
        Test if a question will be required for a particular gender
        """
        data = {
            'gender': 'F',
        }

        form = InformedConsentFormValidator(cleaned_data=data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('women_question', form._errors)
