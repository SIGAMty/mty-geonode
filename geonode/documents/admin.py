#########################################################################
#
# Copyright (C) 2016 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

from django.contrib import admin

from modeltranslation.admin import TabbedTranslationAdmin

from geonode.documents.models import Document, DocumentStaff
from geonode.base.admin import ResourceBaseAdminForm
from geonode.base.admin import metadata_batch_edit


class DocumentAdminForm(ResourceBaseAdminForm):
    class Meta(ResourceBaseAdminForm.Meta):
        model = Document
        # exclude = ['keywords']
        fields = "__all__"
        # exclude = (
        #     'resource',
        # )


class DocumentAdmin(TabbedTranslationAdmin):
    list_display = ("id", "title", "date", "category", "group", "is_approved", "is_published", "metadata_completeness")
    list_display_links = ("id",)
    list_editable = ("title", "category", "group", "is_approved", "is_published")
    list_filter = (
        "date",
        "date_type",
        "restriction_code_type",
        "category",
        "group",
        "is_approved",
        "is_published",
    )
    search_fields = (
        "title",
        "abstract",
        "purpose",
        "is_approved",
        "is_published",
    )
    date_hierarchy = "date"
    form = DocumentAdminForm
    actions = [metadata_batch_edit]

    def delete_queryset(self, request, queryset):
        """
        We need to invoke the 'ResourceBase.delete' method even when deleting
        through the admin batch action
        """
        for obj in queryset:
            from geonode.resource.manager import resource_manager

            resource_manager.delete(obj.uuid, instance=obj)


@admin.register(DocumentStaff)
class DocumentStaffAdmin(DocumentAdmin):
    def get_queryset(self, request):
        """
        Filter documents by user groups
        """
        qs = Document.objects.all()
        if request.user.is_superuser:
            return qs
        elif request.user.is_staff:
            return qs.filter(owner=request.user)
        else:
            return qs.none()

admin.site.register(Document, DocumentAdmin)
