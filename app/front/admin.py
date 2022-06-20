from django.contrib import admin # pylint:disable=W0611
from front.models import (Comment, Expert, ExpertsGeographicDiv, GeographicDiv, Hierarchy, Kingdom, Publication,
Reference, ReferenceLink, SynonymLink, TaxonAuthorLkp, TaxonomicUnit, TaxonUnitType, TuCommentLink)
from simple_history.admin import SimpleHistoryAdmin

admin.site.register(Comment, SimpleHistoryAdmin)
admin.site.register(Expert, SimpleHistoryAdmin)
admin.site.register(ExpertsGeographicDiv, SimpleHistoryAdmin)
admin.site.register(GeographicDiv, SimpleHistoryAdmin)
admin.site.register(Hierarchy, SimpleHistoryAdmin)
admin.site.register(Kingdom, SimpleHistoryAdmin)
admin.site.register(Publication, SimpleHistoryAdmin)
admin.site.register(Reference, SimpleHistoryAdmin)
admin.site.register(ReferenceLink, SimpleHistoryAdmin)
admin.site.register(SynonymLink, SimpleHistoryAdmin)
admin.site.register(TaxonAuthorLkp, SimpleHistoryAdmin)
admin.site.register(TaxonomicUnit, SimpleHistoryAdmin)
admin.site.register(TaxonUnitType, SimpleHistoryAdmin)
admin.site.register(TuCommentLink, SimpleHistoryAdmin)
