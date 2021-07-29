import os

from django.core.exceptions import ValidationError
import django
from django.test import TestCase
from edc_constants.constants import NO, OTHER, YES

from ..form_validators.education_questionnaire_validator import EducationQuestionnaireFormValidator


class EducationQuestionValidatorTests(TestCase):

    def test_type_of_work_required(self):
        data = {
            'working_status': YES
        }
        form = EducationQuestionnaireFormValidator(cleaned_data=data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('type_of_work', form._errors)

    def test_type_of_work_other_required(self):
        data = {
            'type_of_work': OTHER
        }
        form = EducationQuestionnaireFormValidator(cleaned_data=data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('type_of_work_other', form._errors)

    def test_previous_work_other_required(self):
        data = {
            'previous_work': OTHER
        }
        form = EducationQuestionnaireFormValidator(cleaned_data=data)
        self.assertRaises(ValidationError, form.validate)
        self.assertIn('previous_work_other', form._errors)
