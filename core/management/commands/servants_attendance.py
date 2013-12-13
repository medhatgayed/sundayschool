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
            for date_str, uids in settings.SERVANTS_ATTENDANCE:
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



