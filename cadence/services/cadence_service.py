from cadence.models import Cadence
from croniter import croniter

class InvalidPeriodError(SyntaxError):
    pass

class PeriodDoesNotExist(ValueError):
    pass

class InvalidCronStringError(ValueError):
    pass

class CadenceService():
    def get_all_cadences(self):
        return Cadence.objects.all()

    def get_cadence_by_period(self, period) -> Cadence:
        try:
            return Cadence.objects.get(period=period)
        except Cadence.DoesNotExist:
            raise PeriodDoesNotExist(f"Period does not exist: {period}")

    def create_cadence(self, period, cron_string) -> Cadence:
        '''
        Returns Cadence instance, if created.
        Otherwise raises an exception.
        '''
        # period must be unique
        try:
            Cadence.objects.get(period=period.lower())
            raise InvalidPeriodError(f"Period must be unique: {period.lower()}")
        except Cadence.DoesNotExist:
            pass

        # cron_string must be valid
        try:
            croniter(cron_string)
            return Cadence.objects.create(period=period.lower(), cron_string=cron_string)
        except croniter.CroniterError:
            raise InvalidCronStringError(f"Invalid cron string: {cron_string}")