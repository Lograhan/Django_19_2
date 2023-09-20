from django.db import models


class Category(models.Model):
    c_name = models.CharField(max_length=50, verbose_name='наименование')
    c_description = models.TextField(verbose_name='описание')
    c_image = models.ImageField(upload_to='category/', verbose_name='изображение категории', null=True, blank=True)

    def __str__(self):
        return f'{self.id} {self.c_name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('id',)


class Product(models.Model):
    p_name = models.CharField(max_length=50, verbose_name='Наименование')
    p_description = models.TextField(verbose_name='Описание')
    p_image = models.ImageField(upload_to='product_im/', verbose_name='Превью', null=True, blank=True)
    p_category = models.ForeignKey("Category", on_delete=models.CASCADE, verbose_name='Категория')
    p_price = models.FloatField(verbose_name='Цена')
    p_date_creation = models.DateTimeField(auto_now=True)
    p_date_change = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} ({self.p_name}) - {self.p_price}, {self.p_category}'

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('p_name',)


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    num_version = models.FloatField(verbose_name='номер версии')
    name = models.CharField(max_length=50, verbose_name='имя версии')
    is_active = models.BooleanField(default=True, verbose_name='активная версия')

    def __str__(self):
        return f'{self.product} ({self.name} - {self.num_version})'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
