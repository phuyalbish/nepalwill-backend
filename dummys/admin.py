from django.contrib import admin

from core.mixins import DeleteLinkMixin
from dummys.form import (DummyAdminForm)
from dummys.models import (Dummy)

class DummyNameMixin:
    def get_dummy_name(self, obj):
        return obj.dummy.heading if obj.dummy else "No Dummy Assigned"
    get_dummy_name.short_description = "Dummy"



class DummyAdmin(DummyNameMixin, DeleteLinkMixin, admin.ModelAdmin):
    form = DummyAdminForm
    
    list_display = ("name", "is_hidden",)
    list_filter = ("is_hidden",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    # filter_horizontal = ("projects",)

    fieldsets = (
        ("Personal Information", {
            "fields": ("name", "slug", "image",),
        }),
        ("Status", {
            "fields": ("is_hidden",),
            "description": "Private contact info and administrative visibility controls."
        }),
    )

admin.site.register(Dummy, DummyAdmin)