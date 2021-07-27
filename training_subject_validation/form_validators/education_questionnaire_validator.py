from edc_constants.constants import OTHER
from edc_form_validators import FormValidator


class EducationQuestionnaireFormValidator(FormValidator):

    def clean(self):
        # self.required_if(
        #     OTHER,
        #     field='previous_work',
        #     field_required='previous_work_other'
        # )
        self.validate_other_specify(field='type_of_work')
        self.validate_other_specify(field='previous_work')
