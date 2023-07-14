from rest_framework import serializers
from .models import bookCategory

class bookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = bookCategory
        fields = ("id", "category")