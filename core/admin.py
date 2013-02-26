from django.contrib import admin

from core.models import *

class ServantAttendanceInline(admin.TabularInline):
    model = ServantAttendance


class ServantAdmin(admin.ModelAdmin):
    inlines = [ServantAttendanceInline,]

admin.site.register(Servant, ServantAdmin)


class ServantAttendanceAdmin(admin.ModelAdmin):
    pass

admin.site.register(ServantAttendance, ServantAttendanceAdmin)


class ChildAdmin(admin.ModelAdmin):
    pass

admin.site.register(Child, ChildAdmin)
