from django.contrib import admin # pylint:disable=W0611

# Register your models here.
from simple_history.admin import SimpleHistoryAdmin
from refs.models import Ref

admin.site.unregister(Ref)

class RefAdmin(SimpleHistoryAdmin):

    def changed_fields_with_values(self, obj):
        fields = ""
        if obj.prev_record:
            delta = obj.diff_against(obj.prev_record)

            for change in delta.changes:
                fields += str("{} changed from {} to {}.\n".format(change.field.capitalize(), change.old, change.new))
            return fields
        return None

    search_fields = ('title', 'journal')
    history_list_display = ['changed_fields_with_values']


# admin.site.register(Ref, SimpleHistoryAdmin)
admin.site.register(Ref, RefAdmin)
