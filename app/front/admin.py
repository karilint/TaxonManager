from django.contrib import admin # pylint:disable=W0611

# Register your models here.
from simple_history.admin import SimpleHistoryAdmin
from refs.models import Ref

admin.site.unregister(Ref)

class RefAdmin(admin.ModelAdmin):
    search_fields = ('authors', 'title', 'journal')
admin.site.register(Ref, SimpleHistoryAdmin)
