from django.contrib import admin # pylint:disable=W0611
from front.models import (Comment, Expert, ExpertsGeographicDiv, GeographicDiv, Hierarchy, Kingdom, Publication,
ReferenceLink, SynonymLink, TaxonAuthorLkp, TaxonomicUnit, TaxonUnitType, TuCommentLink)

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