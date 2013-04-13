from django.core.management.base import BaseCommand, CommandError
from core.models import SundaySchoolClass
from django.core import mail
from django.conf import settings
import csv
from datetime import datetime

class Command(BaseCommand):
    help = "Sends each class children details to class servants."

    def handle(self, *args, **options):
        email_id = 'cts20130413'
        
        connection = mail.get_connection()
        connection.open()
        
        for sunday_school_class in SundaySchoolClass.objects.all():
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
                children = sunday_school_class.child_set.all()
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
        
            subject = 'Updated class details for year {0}'.format(sunday_school_class.name)
            body = """
     +
Dear Servants,

Peace and Grace,

Please find attached the updated details for your class.

If you have more details that are not in the attached file please email them to me and I will update the data.

God bless,
Sunday School Servants"""
            from_email = 'medhat.gayed@gmail.com'
            to_emails = sunday_school_class.get_servants_emails()
            cc_emails = ['gorgyhanna@yahoo.co.nz','medhat.gayed@gmail.com',]
            if settings.DEBUG:
                to_emails = ['medhat.gayed@gmail.com',]
                cc_emails = ['medhat.gayed@gmail.com',]
            
            email = mail.EmailMessage(subject,
                                      body,
                                      from_email,
                                      to_emails,
                                      cc=cc_emails,
                                      connection=connection)
            email.attach_file(csv_file_path)
            email.send()
            
            self.stdout.write('Successfully sent email to servants of year {0}\n'.format(sunday_school_class.name))
                
        connection.close()
