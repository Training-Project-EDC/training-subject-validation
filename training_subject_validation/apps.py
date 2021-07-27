from datetime import datetime
from dateutil.tz import gettz
from django.apps import AppConfig as DjangoAppConfig
from django.conf import settings
from django.core.management.color import color_style

style = color_style()


class AppConfig(DjangoAppConfig):
    name = 'training_subject_validation'
    verbose_name = 'Training Subject Validation'


if settings.APP_NAME == 'training_subject_validation':
    from edc_protocol.apps import AppConfig as BaseEdcProtocolAppConfigs


    class EdcProtocolAppConfig(BaseEdcProtocolAppConfigs):
        protocol = 'Training'
        protocol_name = 'Training 123'
        protocol_number = '1234'
        protocol_title = ''
        study_open_datetime = datetime(
            2021, 4, 15, 0, 0, 0, tzinfo=gettz('UTC'))
        study_close_datetime = datetime(
            2025, 12, 1, 0, 0, 0, tzinfo=gettz('UTC'))
