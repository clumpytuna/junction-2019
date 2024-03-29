from django.db import models


class Category(models.Model):
    """
    A category of ProductCategory.
    """
    id = models.TextField(primary_key=True)
    name = models.TextField(null=False)
    description = models.TextField(null=True, default=None)
