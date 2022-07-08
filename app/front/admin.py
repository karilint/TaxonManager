from django.contrib import admin # pylint:disable=W0611
from front.models import (Comment, Expert, GeographicDiv, Hierarchy, Kingdom, Publication,
Reference, ReferenceLink, SynonymLink, TaxonAuthorLkp, TaxonomicUnit, TaxonUnitType, TuCommentLink)
from simple_history.admin import SimpleHistoryAdmin

class CommentAdmin(SimpleHistoryAdmin):
    readonly_fields = ('created_by', 'modified_by', 'created_at', 'updated_at')
class ExpertAdmin(SimpleHistoryAdmin):
    readonly_fields = ('created_by', 'modified_by', 'created_at', 'updated_at')
# class ExpertsGeographicDivAdmin(SimpleHistoryAdmin):
#     readonly_fields = ('created_by', 'modified_by', 'created_at', 'updated_at')
class GeographicDivAdmin(SimpleHistoryAdmin):
    readonly_fields = ('created_by', 'modified_by', 'created_at', 'updated_at')
class HierarchyAdmin(SimpleHistoryAdmin):
    readonly_fields = ('created_by', 'modified_by', 'created_at', 'updated_at')
class KingdomAdmin(SimpleHistoryAdmin):
    readonly_fields = ('created_by', 'modified_by', 'created_at', 'updated_at')
class PublicationAdmin(SimpleHistoryAdmin):
    readonly_fields = ('created_by', 'modified_by', 'created_at', 'updated_at')
class ReferenceAdmin(SimpleHistoryAdmin):
    readonly_fields = ('created_by', 'modified_by', 'created_at', 'updated_at')
class ReferenceLinkAdmin(SimpleHistoryAdmin):
    readonly_fields = ('created_by', 'modified_by', 'created_at', 'updated_at')
class SynonymLinkAdmin(SimpleHistoryAdmin):
    readonly_fields = ('created_by', 'modified_by', 'created_at', 'updated_at')
class TaxonAuthorLkpAdmin(SimpleHistoryAdmin):
    readonly_fields = ('created_by', 'modified_by', 'created_at', 'updated_at')
class TaxonomicUnitAdmin(SimpleHistoryAdmin):
    readonly_fields = ('created_by', 'modified_by', 'created_at', 'updated_at')
class TaxonUnitTypeAdmin(SimpleHistoryAdmin):
    readonly_fields = ('created_by', 'modified_by', 'created_at', 'updated_at')
class TuCommentLinkAdmin(SimpleHistoryAdmin):
    readonly_fields = ('created_by', 'modified_by', 'created_at', 'updated_at')

admin.site.register(Comment, CommentAdmin)
admin.site.register(Expert, ExpertAdmin)
# admin.site.register(ExpertsGeographicDiv, ExpertsGeographicDivAdmin)
admin.site.register(GeographicDiv, GeographicDivAdmin)
admin.site.register(Hierarchy, HierarchyAdmin)
admin.site.register(Kingdom, KingdomAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Reference, ReferenceAdmin)
admin.site.register(ReferenceLink, ReferenceLinkAdmin)
admin.site.register(SynonymLink, SynonymLinkAdmin)
admin.site.register(TaxonAuthorLkp, TaxonAuthorLkpAdmin)
admin.site.register(TaxonomicUnit, TaxonomicUnitAdmin)
admin.site.register(TaxonUnitType, TaxonUnitTypeAdmin)
admin.site.register(TuCommentLink, TuCommentLinkAdmin)
