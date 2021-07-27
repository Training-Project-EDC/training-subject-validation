from django import forms
from django.apps import apps as django_apps
from django.core.exceptions import ValidationError
from edc_constants.constants import NO, YES
from edc_form_validators import FormValidator


class SubjectScreeningFormValidator(FormValidator):

    def clean(self):
        self.required_if(
            NO,
            field='is_subject_literate',
            field_required='is_literate_witness_available'
        )
