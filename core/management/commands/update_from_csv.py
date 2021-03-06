import csv

from django.core.management.base import BaseCommand, CommandError
from django.db.models import Q
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

                # if row is empty ignore it
                row_values = [x for x in row.values() if x]
                if not row_values:
                    self.stdout.write('Empty row: {}'.format(row))
                    continue

                if row['Sunday School Class'] == '':
                    sunday_school_class = None
                else:
                    sunday_school_class = SundaySchoolClass.objects.get(name=row['Sunday School Class'])

                try:
                    child = Child.objects.get(name=row['Child Name'])
                    child.parse_and_set_dob(row['Child DOB'])
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
                    child.parse_and_set_dob(row['Child DOB'])
                    child.school_year = row['School Year']
                    child.sunday_school_class = sunday_school_class

                    try:
                        # It is possible that the child is being added to existing parents
                        query = Q()
                        if row['Home Phone']:
                            query |= Q(phone=row['Home Phone'])
                        if row['Father Mobile']:
                            query |= Q(father_mobile=row['Father Mobile'])
                        if row['Father Email']:
                            query |= Q(father_email=row['Father Email'])
                        if row['Mother Mobile']:
                            query |= Q(mother_mobile=row['Mother Mobile'])
                        if row['Mother Email']:
                            query |= Q(mother_email=row['Mother Email'])
                        if row['Home Address']:
                            query |= Q(address=row['Home Address'])

                        child_parents = ChildParents.objects.get(query)
                    except ChildParents.DoesNotExist:
                        child_parents = ChildParents()
                    except ChildParents.MultipleObjectsReturned:
                        child_parents = ChildParents()

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
