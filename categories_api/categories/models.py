from django.db import models

# Create your models here.


class Category(models.Model):

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

    def __str__(self):
        return self.name

    class Meta:

        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
