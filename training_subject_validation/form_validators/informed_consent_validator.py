from edc_constants.constants import OTHER
from edc_form_validators import FormValidator


class InformedConsentFormValidator(FormValidator):

    def clean(self):
        self.required_if(
            'M',
            field='gender',
            field_required='man_question'
        )  # Question required for man

        self.required_if(
            'F',
            field='gender',
            field_required='women_question'
        )  # Question required for women
