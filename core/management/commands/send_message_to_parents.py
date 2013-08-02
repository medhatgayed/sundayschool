from django.core.management.base import BaseCommand, CommandError
from core.models import Child
from django.core import mail
from django.conf import settings
from datetime import datetime
from core.messages import *

class Command(BaseCommand):
    args = 'child-id child-id ..." or "all"'
    help = "Sends a message to each child's parents."

    def handle(self, *args, **options):
        email_id = 'trip20130803'
        message = TRIP_PLAN_CHANGE
        one_per_parents = True
        
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
        
        parents_ids = []
        for child in children:
            parents_emails = child.child_parents.get_parents_emails()
            parents_names = child.child_parents.get_parents_names()
            parents_id = child.child_parents.id
            
            if parents_id in parents_ids and one_per_parents:
                if not settings.DEBUG:
                    child.sent_emails += email_id + ','
                    child.save()
                continue
            elif parents_emails and not email_id in child.sent_emails:
                parents_ids.append(parents_id)
                subject = 'Trip plan for tomorrow'
                body = message.format(parents_names)
                from_email = 'medhat.gayed@gmail.com'
                to_emails = ['medhat.gayed@gmail.com',]
                
                if not settings.DEBUG:
                    to_emails = parents_emails
                
                email = mail.EmailMessage(subject,
                                          body,
                                          from_email,
                                          to_emails,
                                          connection=connection)
                email.send()
                self.stdout.write('Successfully sent email to parents of "%s"\n' % child.name)
                
                if not settings.DEBUG:
                    child.sent_emails += email_id + ','
                    child.save()
            else:
                self.stdout.write('No email sent for parents of "%s"\n' % child.name)
                
        connection.close()
