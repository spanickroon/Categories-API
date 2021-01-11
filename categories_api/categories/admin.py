"""This module contain class for work with model objects in admin panel."""

from django.contrib import admin
from .models import Category


@admin.register(Category)
class AuthorAdmin(admin.ModelAdmin):
    """Category class with list of filters and meta data."""

    list_filter = ('id', )

    class Meta:
        """Meta data."""

        app_label = 'Category'
        verbose_name = 'Category'
        base_manager_name = 'Category'
        verbose_name_plural = 'Category'
        db_table = 'StCategoryock'
        default_manager_name = 'Category'

    def save_model(self, request, obj, form, change):
        """Model save method."""
        obj.save()
