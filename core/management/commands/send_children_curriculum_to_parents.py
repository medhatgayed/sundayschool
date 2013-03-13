from django.core.management.base import BaseCommand, CommandError
from core.models import Child
from django.core import mail

class Command(BaseCommand):
    args = 'child-id child-id ..." or "all"'
    help = "Sends the curriculum to each child's parents"

    def handle(self, *args, **options):
        connection = mail.get_connection()
        connection.open()
        
        if args[0] == 'all':
            children = Child.objects.all()
        else:
            children = []
            for child_id in args:
                try:
                    child = Child.objects.get(pk=int(child_id))
                    children.append(child)
                except Child.DoesNotExist:
                    raise CommandError('Child "%s" does not exist' % child_id)
        
        for child in children:
            parents_emails = child.get_parents_emails()
            if parents_emails and not child.curriculum_sent:
                subject = 'Sunday School Curriculum for {0}'.format(child.get_first_name())
                body = """
Dear {0},

Peace and Grace,

Please find attached the Sunday School Curriculum for {1}.

God bless,
Sunday School Servants""".format(child.get_parents_names(), child.get_first_name())
                
                email = mail.EmailMessage(subject,
                                          body,
                                          'medhat.gayed@gmail.com',
                                          parents_emails,
                                          connection=connection)
                
                email.attach_file('/home/medhat/Documents/service/SundaySchoolCurriculum/{0}.pdf'.format(child.book))
                email.attach_file('/home/medhat/Documents/service/SundaySchoolSchedule/{0}-schedule.pdf'.format(child.book))
                email.send()
                
                child.curriculum_sent = True
                child.save()
                self.stdout.write('Successfully sent email to parents of "%s"\n' % child.name)
            else:
                self.stdout.write('No email sent for parents of "%s"\n' % child.name)
        
        connection.close()
