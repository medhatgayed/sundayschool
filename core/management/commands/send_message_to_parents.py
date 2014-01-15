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
        email_id = settings.MESSAGE_ID
        message = settings.MESSAGE_NAME
        one_per_parents = settings.MESSAGE_ONE_PER_PARENTS
        is_sample = settings.MESSAGE_IS_SAMPLE
        sample_count = settings.MESSAGE_SAMPLE_COUNT
        is_birthday = False
        
        connection = mail.get_connection()
        connection.open()
        
        if args[0] == 'all':
            children = Child.objects.all()
        elif args[0] == 'birthday':
            is_birthday = True
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
        count = 0
        for child in children:
            parents_emails = child.child_parents.get_parents_emails()
            parents_names = child.child_parents.get_parents_names()
            parents_id = child.child_parents.id
            
            if parents_id in parents_ids and one_per_parents:
                if not is_sample:
                    child.sent_emails += email_id + ','
                    child.save()
                continue
            elif parents_emails and not email_id in child.sent_emails:
                parents_ids.append(parents_id)
                subject = settings.MESSAGE_SUBJECT
                if is_birthday:
                    body = message.format(parents_names, child.get_first_name())
                else:
                    body = message.format(parents_names, child.get_first_name())
                from_email = settings.MESSAGE_FROM_EMAIL
                to_emails = settings.MESSAGE_TO_EMAILS
                
                if not is_sample:
                    to_emails = parents_emails
                
                email = mail.EmailMessage(subject,
                                          body,
                                          from_email,
                                          to_emails,
                                          connection=connection)

                if settings.MESSAGE_SEND_EMAIL:
                    email.attach_file('/home/medhat/Dropbox/service/2013/memo-{0}.pdf'.format(child.school_year))
                    email.send()
                self.stdout.write('Successfully sent email to parents of "%s"\n' % child.name)
                
                if not is_sample:
                    child.sent_emails += email_id + ','
                    child.save()
            else:
                self.stdout.write('No email sent for parents of "%s"\n' % child.name)

            count += 1
            if is_sample and count >= sample_count:
                break
                
        connection.close()
