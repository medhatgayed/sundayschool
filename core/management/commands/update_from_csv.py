from django.core.management.base import BaseCommand, CommandError
from core.models import Child, ChildParents

class Command(BaseCommand):
    help = "Update children details from a CSV file."

    def add_arguments(self, parser):
        parser.add_argument('--save',
            action='store_true',
            dest='save',
            default=False,
            help='Confirm that updates should be saved to the db otherwise
                will do a dry run.')

    def handle(self, *args, **options):
        pass
