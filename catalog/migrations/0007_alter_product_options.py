# Generated by Django 4.2.4 on 2023-09-09 23:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_category_c_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('id',), 'verbose_name': 'товар', 'verbose_name_plural': 'товары'},
        ),
    ]