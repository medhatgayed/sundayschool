from django.core.management.base import BaseCommand
from core.models import Child, SundaySchoolClass

class Command(BaseCommand):
    help = "Move children that are in year 2 or above up one year."

    def handle(self, *args, **options):
        class_0 = SundaySchoolClass.objects.get(name='0')
        class_1_and_2 = SundaySchoolClass.objects.get(name='1&2')
        class_3_and_4 = SundaySchoolClass.objects.get(name='3&4')
        class_5_and_6 = SundaySchoolClass.objects.get(name='5&6')

        map = {0: class_0,
               1: class_1_and_2,
               2: class_1_and_2,
               3: class_3_and_4,
               4: class_3_and_4,
               5: class_5_and_6,
               6: class_5_and_6}

        for child in Child.objects.filter(school_year__gte=2):
            child.school_year += 1
            if child.school_year > 6:
                child.is_active = False
                self.stdout.write('De-activated %s because moved up to year %s.\n' % (child, child.school_year))
                continue
            child.sunday_school_class = map[child.school_year]
            child.save()
            self.stdout.write('Successfully moved %s to year %s and ss class %s.\n' % (child, child.school_year, child.sunday_school_class))
