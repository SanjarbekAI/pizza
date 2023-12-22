from django.contrib import admin
from pages.models import *

@admin.register(MainScrollModel)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ['title', 'discount', 'created_at', 'updated_at']
    search_fields = ['title', 'info']
    list_filter = ['created_at', 'updated_at']



@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at']
    search_fields = ['title']
    list_filter = ['created_at', 'updated_at']


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'created_at', 'updated_at']
    search_fields = ['title', 'info']
    list_filter = ['created_at', 'updated_at']
