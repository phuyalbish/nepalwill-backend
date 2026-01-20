from rest_framework import serializers

from contacts.models import  Contact


class ContactSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"
