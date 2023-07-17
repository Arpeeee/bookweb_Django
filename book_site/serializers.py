from rest_framework import serializers
from .models import bookCategory, review, images

class bookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = bookCategory
        fields = ("id", "category")

class reviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = review
        field = ["id","categorys", "main_title", "book_title", "content", "sour", "sweet", "bitter",
                 "spicy", "salt", "created_time", "updated_time", "writer", "post_imgs", "slug"]