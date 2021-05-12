from rest_framework import serializers
from .models import Contact, Social


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    social = SocialSerializer(
        read_only=True, many=True, source='links'
    )

    class Meta:
        model = Contact
        fields = '__all__'