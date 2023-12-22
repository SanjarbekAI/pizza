from django.db import models

class MainScrollModel(models.Model):
    image = models.ImageField(upload_to='main-scroll')
    title = models.CharField(max_length=50)
    info = models.CharField(max_length=255)
    discount = models.PositiveSmallIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'scroll'
        verbose_name_plural = 'scrolls'




class CategoryModel(models.Model):
    title = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'



class ProductModel(models.Model):
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products')
    price = models.FloatField()
    info = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'



