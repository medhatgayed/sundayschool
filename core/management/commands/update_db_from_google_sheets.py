from __future__ import unicode_literals

from django.core.management.base import BaseCommand, CommandError
from django.db.models import Q
from core.models import Child, ChildParents, SundaySchoolClass
from django.conf import settings

import pygsheets


class Command(BaseCommand):
    help = "Update children details from a google sheet to the database."

    def add_arguments(self, parser):
        parser.add_argument(
            '--save',
            action='store_true',
            dest='save',
            default=False,
            help='Confirm that updates should be saved to the db otherwise will do a dry run.')

        parser.add_argument(
            '--sheet-key',
            action='store',
            dest='sheet_key',
            help='The google sheet name.')

    def handle(self, *args, **options):
        sheet_key = options.get('sheet_key')
        if not sheet_key:
            raise CommandError('Please specify --sheet-key')

        gc = pygsheets.authorize(outh_file=settings.GOOGLE_SHEETS_CLIENT_SECRET_FILE)
        ss = gc.open_by_key(sheet_key)
        ws = ss.sheet1

        for x in ws.get_all_records():
            print('')
            for key, value in x.items():
                print('{}: {}'.format(key, value))
