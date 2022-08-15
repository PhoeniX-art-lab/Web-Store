from django.db import models
from django.urls import reverse


class Store(models.Model):
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    product_content = models.TextField()
    product_characteristics = models.TextField(null=True)
    product_image = models.ImageField(upload_to="photos/%Y/%m/%d")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    product_price = models.IntegerField()
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('information', kwargs={'info_slug': self.slug})

    class Meta:
        verbose_name_plural = 'Store'
        ordering = ['id', 'product_name']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def get_absolute_url(self):
        return reverse('categories', kwargs={'cat_slug': self.slug})

    def __str__(self):
        return self.name
