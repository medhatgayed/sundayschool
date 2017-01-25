from django.core.management.base import BaseCommand, CommandError
from core.models import SundaySchoolClass
from django.core import mail
from django.conf import settings
import csv
from datetime import datetime

class Command(BaseCommand):
    help = "Export a CSV file of children details for each Sunday School class."

    def handle(self, *args, **options):
        for sunday_school_class in SundaySchoolClass.objects.all():
            self.stdout.write('Exporting children details for year {0}\n'.format(sunday_school_class.name))
            csv_file_path = '/tmp/children-details-for-year-{0}.csv'.format(sunday_school_class.name)
            with open(csv_file_path, 'w') as f:
                w = csv.writer(f, quoting=csv.QUOTE_ALL)
                w.writerow(['Child Name',
                            'Child DOB',
                            'School Year',
                            'Sunday School Class',
                            'Home Phone',
                            'Father Name',
                            'Father Mobile',
                            'Father Email',
                            'Mother Name',
                            'Mother Mobile',
                            'Mother Email',
                            'Home Address',])
                children = sunday_school_class.child_set.filter(is_active=True)
                for child in children:
                    child_parents = child.child_parents
                    w.writerow([str(child.name),
                                str(child.dob),
                                str(child.school_year),
                                str(child.sunday_school_class),
                                str(child_parents.phone),
                                str(child_parents.father_name),
                                str(child_parents.father_mobile),
                                str(child_parents.father_email),
                                str(child_parents.mother_name),
                                str(child_parents.mother_mobile),
                                str(child_parents.mother_email),
                                str(child_parents.address),])
