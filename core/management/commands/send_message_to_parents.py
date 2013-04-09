from django.core.management.base import BaseCommand, CommandError
from core.models import Child
from django.core import mail
from django.conf import settings

class Command(BaseCommand):
    args = 'child-id child-id ..." or "all"'
    help = "Sends a message to each child's parents."

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
            parents_emails = child.child_parents.get_parents_emails()
            parents_names = child.child_parents.get_parents_names()
            if parents_emails and child.sunday_school_class.name != '0':
                subject = 'Practice Sacrament of Confession for {0}'.format(child.get_first_name())
                body = """
Dear {0},

Peace and Grace,

This is just a reminder that Sunday School is organizing confession sessions
for all Sunday School children on Sunday 14/4/2013.

Please bring {1} to participate and get into the habit of practicing this great and holy sacrament.

God bless,
Sunday School Servants""".format(parents_names, child.get_first_name())
                from_email = 'medhat.gayed@gmail.com'
                to_emails = parents_emails
                if settings.DEBUG:
                    to_emails = ['medhat.gayed@gmail.com',]
                
                email = mail.EmailMessage(subject,
                                          body,
                                          from_email,
                                          to_emails,
                                          connection=connection)
                email.send()
                
                self.stdout.write('Successfully sent email to parents of "%s"\n' % child.name)
            else:
                self.stdout.write('No email sent for parents of "%s"\n' % child.name)
                
        connection.close()
