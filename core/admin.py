from django.contrib import admin

from core.models import *


class SundaySchoolClassAdmin(admin.ModelAdmin):
    pass

admin.site.register(SundaySchoolClass, SundaySchoolClassAdmin)


class ServantAttendanceInline(admin.TabularInline):
    model = ServantAttendance


class ServantAdmin(admin.ModelAdmin):
    list_display = ['name', 'sunday_school_class', 'uid', 'is_active']
    inlines = [ServantAttendanceInline,]

admin.site.register(Servant, ServantAdmin)


class ServantAttendanceAdmin(admin.ModelAdmin):
    pass

admin.site.register(ServantAttendance, ServantAttendanceAdmin)


class ChildAdmin(admin.ModelAdmin):
    search_fields = ['name',]
    list_display = ['name', 'dob', 'school_year', 'sunday_school_class', 'is_active']
    list_filter = ['school_year', 'sunday_school_class']

admin.site.register(Child, ChildAdmin)


class ChildInline(admin.TabularInline):
    model = Child


class ChildParentsAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'father_name', 'father_mobile', 'father_email',
                    'mother_name', 'mother_mobile', 'mother_email', 'phone', 'is_active']
    inlines = [ChildInline,]
    search_fields = ['father_name', 'mother_name', 'child__name',]

admin.site.register(ChildParents, ChildParentsAdmin)