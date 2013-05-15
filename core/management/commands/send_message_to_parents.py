from django.core.management.base import BaseCommand, CommandError
from core.models import Child
from django.core import mail
from django.conf import settings

class Command(BaseCommand):
    args = 'child-id child-id ..." or "all"'
    help = "Sends a message to each child's parents."

    def handle(self, *args, **options):
        email_id = 'reschoir20130502'
        
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
            if parents_emails and not email_id in child.sent_emails:
                subject = 'Sunday School Resurrection Choir'
                body = """
Dear {0},

Peace and Grace,

Sunday School will be presenting a choir for the Glorious Feast of Resurrection on Sunday 5th May 2013 at 12pm.

Please bring {1} at 11:45am so that the servants will have enough time to organize the kids for the choir.

Happy Glorious Feast of Resurrection.

Sunday School Servants
St. Mark's Coptic Orthodox Church, Auckland.""".format(parents_names, child.get_first_name())
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
                
                child.sent_emails += email_id + ','
                child.save()
                
                self.stdout.write('Successfully sent email to parents of "%s"\n' % child.name)
            else:
                self.stdout.write('No email sent for parents of "%s"\n' % child.name)
                
        connection.close()
