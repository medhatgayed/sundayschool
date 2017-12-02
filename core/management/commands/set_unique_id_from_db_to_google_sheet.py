from __future__ import unicode_literals

from django.core.management.base import BaseCommand, CommandError
from core.models import Child
from django.conf import settings

import pygsheets


class Command(BaseCommand):
    help = "Match and set children and parents unique id from db to google sheet."

    def add_arguments(self, parser):
        parser.add_argument(
            '--save',
            action='store_true',
            dest='save',
            default=False,
            help='Confirm that updates should be saved to the google sheet otherwise will do a dry run.')

        parser.add_argument(
            '--sheet-key',
            action='store',
            dest='sheet_key',
            help='The google sheet key.')

    def handle(self, *args, **options):
        sheet_key = options.get('sheet_key')
        if not sheet_key:
            raise CommandError('Please specify --sheet-key')

        gc = pygsheets.authorize(outh_file=settings.GOOGLE_SHEETS_CLIENT_SECRET_FILE)
        ss = gc.open_by_key(sheet_key)
        ws = ss.sheet1

        for child in Child.objects.all():
            cell = None

            cell_child_name = ws.find(child.name)

            father_mobile = child.child_parents.father_mobile
            if father_mobile:
                cell = ws.find(child.child_parents.father_mobile)

            father_email = child.child_parents.father_email
            if father_email:
                cell = ws.find(child.child_parents.father_email)

            mother_mobile = child.child_parents.mother_mobile
            if mother_mobile:
                cell = ws.find(child.child_parents.mother_mobile)

            mother_email = child.child_parents.mother_email
            if mother_email:
                cell = ws.find(child.child_parents.mother_email)

            cell_child_name = cell_child_name[0] if cell_child_name else None
            cell = cell[0] if cell else None

            if cell_child_name and cell and cell_child_name.row == cell.row:
                child_unique_id_cell = 'M{}'.format(cell.row)
                ws.update_cell(str(child_unique_id_cell), str(child.unique_id))
                self.stdout.write('Set {} unique id to {}'.format(child.name, child.unique_id))

                parents_unique_id_cell = 'N{}'.format(cell.row)
                ws.update_cell(str(parents_unique_id_cell), str(child.child_parents.unique_id))
                self.stdout.write('Set {} parents unique id to {}'.format(child.name, child.child_parents.unique_id))

        if options.get('save'):
            ws.sync()
            self.stdout('Updated cloud.')
        else:
            self.stdout('Dry run complete.')