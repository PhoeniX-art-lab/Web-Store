from django.contrib import admin

from .models import Store, Category


class StoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'time_create', 'is_published')
    list_display_links = ('id', 'product_name')
    search_fields = ('product_name', 'product_content')
    list_editable = ('is_published',)
    list_filter = ('product_name', 'time_create', 'is_published')
    prepopulated_fields = {"slug": ("product_name",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', )
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Store, StoreAdmin)
admin.site.register(Category, CategoryAdmin)
