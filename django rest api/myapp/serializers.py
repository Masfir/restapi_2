from rest_framework import serializers
from myapp.models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'title', 'email']
    