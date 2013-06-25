from django.core.management.base import BaseCommand, CommandError
from core.models import Child
from django.core import mail
from django.conf import settings
from datetime import datetime
from core.messages import BIRTHDAY

class Command(BaseCommand):
    args = 'child-id child-id ..." or "all"'
    help = "Sends a message to each child's parents."

    def handle(self, *args, **options):
        email_id = 'birthday20130630'
        
        connection = mail.get_connection()
        connection.open()
        
        if args[0] == 'all':
            children = Child.objects.all()
        elif args[0] == 'birthday':
            children = Child.objects.filter(dob__month=datetime.now().month)
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
            if parents_emails and not email_id in child.sent_emails:
                subject = 'Birthday for {0}'.format(child.get_first_name())
                body = BIRTHDAY.format(parents_names, child.get_first_name())
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
                
                if not settings.DEBUG:
                    child.sent_emails += email_id + ','
                    child.save()
                
                self.stdout.write('Successfully sent email to parents of "%s"\n' % child.name)
            else:
                self.stdout.write('No email sent for parents of "%s"\n' % child.name)
                
        connection.close()
