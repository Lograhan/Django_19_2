# Generated by Django 4.2.4 on 2023-08-16 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=50, verbose_name='наименование')),
                ('c_description', models.TextField(verbose_name='описание')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=50, verbose_name='имя')),
                ('p_description', models.TextField(verbose_name='описание')),
                ('p_image', models.ImageField(upload_to='product_im/', verbose_name='превью')),
                ('p_price', models.FloatField(verbose_name='цена')),
                ('p_date_creation', models.DateTimeField(auto_now=True)),
                ('p_date_change', models.DateTimeField(auto_now_add=True)),
                ('p_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category', verbose_name='категория')),
            ],
        ),
    ]
