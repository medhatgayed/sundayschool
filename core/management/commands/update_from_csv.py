import csv

from django.core.management.base import BaseCommand, CommandError
from core.models import Child, ChildParents


class Command(BaseCommand):
    help = "Update children details from a CSV file."

    def add_arguments(self, parser):
        parser.add_argument(
            '--save',
            action='store_true',
            dest='save',
            default=False,
            help='Confirm that updates should be saved to the db otherwise will do a dry run.')

        parser.add_argument(
            '--csv-path',
            action='store',
            dest='csv_path',
            help='The path to the csv file to update from.')

    def handle(self, *args, **options):
        csv_path = options.get('csv_path')
        if not csv_path:
            raise CommandError('Please specify --csv-path')

        with open(csv_path) as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                child = None
                try:
                    child = Child.objects.get(name=row['Child Name'])
                    child.dob = row['Child DOB']
                    self.stdout.write(("Updating: {} {}".format(child.name, child.dob)))
                except Child.DoesNotExist:
                    child = Child(
                        name=row['Child Name'],
                        dob=row['Child DOB'])
                    self.stdout.write(("Creating: {} {}".format(child.name, child.dob)))

                if child and options.get('save'):
                    child.save()
