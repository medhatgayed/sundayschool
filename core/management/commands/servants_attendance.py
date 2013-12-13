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
                uids = settings.SERVANTS_ATTENDANCE[date_str]
                if servant.uid in uids:
                    attended_mass = True
                    attended_meeting = True
                    attended_sunday_school = True
                else:
                    attended_mass = False
                    attended_meeting = False
                    attended_sunday_school = False

                ServantAttendance.objects.create(servant=servant,
                                                 date=date_str,
                                                 attended_mass=attended_mass,
                                                 attended_meeting=attended_meeting,
                                                 attended_sunday_school=attended_sunday_school)

        self.stdout.write('Successfully imported servants attendance.\n')
