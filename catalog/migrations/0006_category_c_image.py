# Generated by Django 4.2.4 on 2023-08-24 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_product_p_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='c_image',
            field=models.ImageField(blank=True, null=True, upload_to='category/', verbose_name='изображение категории'),
        ),
    ]
