from rest_framework import serializers
from .models import Drug, ActiveIng

class DrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drug
        fields = ('name', 'price', 'active_ing')

class ActiveIngSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActiveIng
        fields = ('name', 'dose')