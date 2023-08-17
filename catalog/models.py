from django.db import models


class Category(models.Model):
    c_name = models.CharField(max_length=50, verbose_name='наименование')
    c_description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.id} {self.c_name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('id',)


class Product(models.Model):
    p_name = models.CharField(max_length=50, verbose_name='имя')
    p_description = models.TextField(verbose_name='описание')
    p_image = models.ImageField(upload_to='product_im/', verbose_name='превью', null=True, blank=True)
    p_category = models.ForeignKey("Category", on_delete=models.CASCADE, verbose_name='категория')
    p_price = models.FloatField(verbose_name='цена')
    p_date_creation = models.DateTimeField(auto_now=True)
    p_date_change = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} ({self.p_name}) - {self.p_price}, {self.p_category}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('p_name',)
