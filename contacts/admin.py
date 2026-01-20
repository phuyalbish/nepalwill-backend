from django.contrib import admin

from contacts.form import (ContactAdminForm)
from contacts.models import  Contact
from core.mixins import DeleteLinkMixin



class ContactAdmin(DeleteLinkMixin, admin.ModelAdmin):
    form = ContactAdminForm
    list_display = ("name", "modified_at", "delete_link")
    list_filter = ["is_reviewed"]


admin.site.register(Contact, ContactAdmin)

