from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from datetime import datetime
from django.conf import settings
from core.models import Servant, ServantAttendance

class Command(BaseCommand):
    help = "Bulk import servants attendance."

    def handle(self, *args, **options):
        servants = Servant.objects.all()
        for servant in servants:
            self.stdout.write('Importing attendance for {0}\n'.format(servant.name))

            for date_str in sorted(settings.SERVANTS_ATTENDANCE):
                attended_mass = False
                attended_meeting = False
                attended_sunday_school = False

                uids = settings.SERVANTS_ATTENDANCE[date_str]['mass']
                if servant.uid in uids:
                    attended_mass = True

                uids = settings.SERVANTS_ATTENDANCE[date_str]['meeting']
                if servant.uid in uids:
                    attended_meeting = True

                uids = settings.SERVANTS_ATTENDANCE[date_str]['ss']
                if servant.uid in uids:
                    attended_sunday_school = True

                ServantAttendance.objects.create(servant=servant,
                                                 date=date_str,
                                                 attended_mass=attended_mass,
                                                 attended_meeting=attended_meeting,
                                                 attended_sunday_school=attended_sunday_school)

        self.stdout.write('Successfully imported servants attendance.\n')
