from rest_framework import serializers
from .models import Category
from django.forms.models import model_to_dict


class CategoriesCreateSerializer(serializers.ModelSerializer):

    children = serializers.ListField()

    class Meta:
        model = Category
        fields = ('name', 'children',)

    def create(self, validated_data):
        category, _ = Category.objects.all().update_or_create(
            name=validated_data.get('name', None),
            parent=None,
        )

        self._recursive_creation_categories(
            validated_data.get('name', None),
            validated_data.get('children', None)
        )

        return category

    def _recursive_creation_categories(self, parent, children):
        for child in children:
            category, _ = Category.objects.all().update_or_create(
                name=child.get('name'),
                parent=Category.objects.get(name=parent),
            )

            if child.get('children'):
                self._recursive_creation_categories(
                    child.get('name'),
                    child.get('children')
                )

    def to_representation(self, instance):
        return {}
