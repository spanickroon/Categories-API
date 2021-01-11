"""Module for serialization classes."""

from rest_framework import serializers
from .models import Category
from django.forms.models import model_to_dict


class CategoriesCreateSerializer(serializers.ModelSerializer):
    """The class-serializer that is responsible for creating an object."""

    children = serializers.ListField()

    class Meta:
        """Meta data."""

        model = Category
        fields = ('name', 'children',)

    def create(self, validated_data):
        """
        Method for creating category objects in the database.

        Takes valid data from the request as a parameter.
        """
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
        """
        Recursive subcategory creation method.

        Based on finding children in depth.
        Accepts parent and child as parameters.
        """
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
        """
        Method of displaying information after making a request.

        Accepts a response to a stored object in a method create
        """
        return {'status': 201, 'count_categories': Category.objects.count()}


class CategoriesSerializer(serializers.Serializer):
    """The class-serializer that is responsible for get requests."""

    def to_representation(self, value):
        """
        The method that gives the answer to the get request.

        Accepts a queryset view object.
        """
        model = model_to_dict(value)

        parents = self._search_parents(
            Category.objects.get(id=model.get('parent'))
        ) if model.get('parent') else []

        children = Category.objects.filter(parent=model.get('id'))

        siblings = Category.objects.filter(
            parent=model.get('parent')
            ).exclude(id=model.get('id'))

        return self._forming_json_response(model, parents, children, siblings)

    def _search_parents(self, parent_obj):
        """
        A method that looks for parents and returns a general list.

        Accepts the current parent.
        """
        parent_list = []

        self._recursive_parent_search(parent_obj, parent_list)
        return parent_list

    def _recursive_parent_search(self, parent, parent_list):
        """
        Recursive parent search in height.

        Accepts a parent and parent list to complement.
        """
        parent_list.append(parent)

        if parent.parent:
            self._recursive_parent_search(
                Category.objects.get(id=parent.parent.id), parent_list
            )

    def _forming_json_response(self, model, parents, children, siblings):
        """
        A method that generates a response to a get request as JSON.

        Accepts current model, parent list, child list, and siblings list.
        """
        response = {
            'id': model.get('id'),
            'name': model.get('name'),
            'parents': [
                {
                    'id': parent.id,
                    'name': parent.name
                }
                for parent in parents
            ],
            'children': [
                {
                    'id': child.id,
                    'name': child.name
                }
                for child in children
            ],
            'siblings': [
                {
                    'id': sibling.id,
                    'name': sibling.name
                }
                for sibling in siblings
            ]
        }

        return response
