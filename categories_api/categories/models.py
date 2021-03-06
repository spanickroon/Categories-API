"""Module with categories models."""

from django.db import models


class Category(models.Model):
    """
    Category model.

    Has two fields: name -- CharField(255), parent -- FK.
    The parent field is a key to an object of the same type.
    Thanks to this, nesting of categories is implemented.
    """

    name = models.CharField(
        max_length=255,
        unique=True,
        blank=True,
        null=False,
        verbose_name='name'
    )

    parent = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name='parent',
        related_name='children'
    )

    def __str__(self) -> str:
        """Funtion for output info about this category object."""
        return self.name

    class Meta:

        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
