from django.forms.models import model_to_dict
from cadence.services.cadence_service import CadenceService

CadenceDict = {
    'period': str,
    'cron_string': str
}

class CadenceAPI():
    def _format_model_list(self, model_list: list) -> CadenceDict:
        return [model_to_dict(model) for model in model_list]

    def get_all_cadences(self) -> list[CadenceDict]:
        '''Returns list of all cadences'''
        all_cadences = CadenceService().get_all_cadences()
        return self._format_model_list(all_cadences)

    def create_cadence(self, period, cron_string) -> CadenceDict:
        try:
            cadence = CadenceService().create_cadence(period, cron_string)
            return model_to_dict(cadence)
        except Exception as e:
            raise Exception(e) from None
            # https://docs.python.org/3/tutorial/errors.html#exception-chaining

    def get_cadence_by_period(self, period) -> CadenceDict:
        try:
            cadence = CadenceService().get_cadence_by_period(period)
            return model_to_dict(cadence)
        except Exception as e:
            raise Exception(e) from None