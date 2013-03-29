from django.core.management.base import BaseCommand, CommandError
from fabric.api import local
from django.conf import settings
from datetime import datetime

class Command(BaseCommand):
    help = "Backup the database"

    def handle(self, *args, **options):
        local('pg_dump sundayschool | gzip > {0}sundayschool.{1}.sql.gz'.format(settings.DB_BACKUP_DIR, datetime.now().strftime('%Y%m%d%H%M%S')))