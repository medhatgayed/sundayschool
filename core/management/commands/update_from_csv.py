import csv

from django.core.management.base import BaseCommand, CommandError
from core.models import Child, ChildParents, SundaySchoolClass


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
                child_parents = None
                sunday_school_class = SundaySchoolClass.objects.get(name=row['Sunday School Class'])
                try:
                    child = Child.objects.get(name=row['Child Name'])
                    child.dob = row['Child DOB']
                    child.school_year = row['School Year']
                    child.sunday_school_class = sunday_school_class

                    child_parents = child.child_parents
                    child_parents.phone = row['Home Phone']
                    child_parents.father_name = row['Father Name']
                    child_parents.father_mobile = row['Father Mobile']
                    child_parents.father_email = row['Father Email']
                    child_parents.mother_name = row['Mother Name']
                    child_parents.mother_mobile = row['Mother Mobile']
                    child_parents.mother_email = row['Mother Email']
                    child_parents.address = row['Home Address']

                    self.stdout.write('Updating parents: {}'.format(child_parents.get_parents_names()))
                    self.stdout.write('Updating child: {} {}'.format(child.name, child.dob))
                    self.stdout.write('')
                except Child.DoesNotExist:
                    child = Child()
                    child.name = row['Child Name']
                    child.dob = row['Child DOB']
                    child.school_year = row['School Year']
                    child.sunday_school_class = sunday_school_class

                    try:
                        # It is possible that the child is being added to existing parents
                        child_parents = ChildParents.objects.get(
                            phone=row['Home Phone'],
                            father_name=row['Father Name'],
                            father_mobile=row['Father Mobile'],
                            father_email=row['Father Email'],
                            mother_name=row['Mother Name'],
                            mother_mobile=row['Mother Mobile'],
                            mother_email=row['Mother Email'],
                            address=row['Home Address'])
                    except ChildParents.DoesNotExist:
                        child_parents = ChildParents()
                    finally:
                        child_parents.phone = row['Home Phone']
                        child_parents.father_name = row['Father Name']
                        child_parents.father_mobile = row['Father Mobile']
                        child_parents.father_email = row['Father Email']
                        child_parents.mother_name = row['Mother Name']
                        child_parents.mother_mobile = row['Mother Mobile']
                        child_parents.mother_email = row['Mother Email']
                        child_parents.address = row['Home Address']
                        child.child_parents = child_parents

                        if child_parents.id:
                            self.stdout.write('Found parents: {}'.format(child_parents.get_parents_names()))
                        else:
                            self.stdout.write('Adding parents: {}'.format(child_parents.get_parents_names()))

                    self.stdout.write(("Adding child: {} {}".format(child.name, child.dob)))
                finally:
                    if child and child_parents and options.get('save'):
                        child.save()
                        child_parents.save()
