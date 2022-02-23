from django.contrib import admin # pylint:disable=W0611
from front.models import (Comment, Expert, ExpertsGeographicDiv, GeographicDiv, Hierarchy, Kingdom, Publication,
ReferenceLink, SynonymLink, TaxonAuthorLkp, TaxonomicUnit, TaxonUnitType, TuCommentLink)

# Register your models here.
from simple_history.admin import SimpleHistoryAdmin
from simple_history.models import HistoricalRecords
from front.models import Reference


admin.site.register(Comment)
admin.site.register(Expert)
admin.site.register(ExpertsGeographicDiv)
admin.site.register(GeographicDiv)
admin.site.register(Hierarchy)
admin.site.register(Kingdom)
admin.site.register(Publication)
admin.site.register(ReferenceLink)
admin.site.register(SynonymLink)
admin.site.register(TaxonAuthorLkp)
admin.site.register(TaxonomicUnit)
admin.site.register(TaxonUnitType)
admin.site.register(TuCommentLink)

# Django-simple-history history tracking for a third-party model
from simple_history import register
register(Reference)

class RefAdmin(SimpleHistoryAdmin):

    def changed_fields_with_values(self, obj):
        fields = ""
        if obj.prev_record:
            delta = obj.diff_against(obj.prev_record)

            for change in delta.changes:
                fields += str("{} changed from {} to {}.\n".format(change.field.capitalize(), change.old, change.new))
            return fields
        return None

    search_fields = ('authors', 'title', 'journal')
    history_list_display = ['changed_fields_with_values']
    history = HistoricalRecords()




admin.site.register(Reference, RefAdmin)
