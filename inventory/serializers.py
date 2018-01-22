from rest_framework import serializers
from . import models


class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Items
        fields = '__all__'
