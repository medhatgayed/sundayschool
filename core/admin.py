from django.contrib import admin

from core.models import Contact, Servant, Child, ServantAttendance


class ContactAdmin(admin.ModelAdmin):
    pass

admin.site.register(Contact, ContactAdmin)


class ServantAdmin(admin.ModelAdmin):
    pass

admin.site.register(Servant, ServantAdmin)


class ChildAdmin(admin.ModelAdmin):
    pass

admin.site.register(Child, ChildAdmin)


class ServantAttendanceAdmin(admin.ModelAdmin):
    pass

admin.site.register(ServantAttendance, ServantAttendanceAdmin)
