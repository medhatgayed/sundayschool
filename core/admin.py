from django.contrib import admin

from core.models import *

class ServantYearInline(admin.TabularInline):
    model = ServantYear


class ServantAttendanceInline(admin.TabularInline):
    model = ServantAttendance


class ServantAdmin(admin.ModelAdmin):
    inlines = [ServantYearInline, ServantAttendanceInline,]

admin.site.register(Servant, ServantAdmin)


class ServantYearAdmin(admin.ModelAdmin):
    pass

admin.site.register(ServantYear, ServantYearAdmin)


class ServantAttendanceAdmin(admin.ModelAdmin):
    pass

admin.site.register(ServantAttendance, ServantAttendanceAdmin)


class ChildYearInline(admin.TabularInline):
    model = ChildYear


class ChildAdmin(admin.ModelAdmin):
    inlines = [ChildYearInline,]

admin.site.register(Child, ChildAdmin)


class ChildYearAdmin(admin.ModelAdmin):
    pass

admin.site.register(ChildYear, ChildYearAdmin)
