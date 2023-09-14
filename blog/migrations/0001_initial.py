# Generated by Django 4.2.4 on 2023-09-10 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='название')),
                ('slug', models.CharField(max_length=100, verbose_name='slug')),
                ('content', models.TextField(verbose_name='содержимое')),
                ('b_image', models.ImageField(blank=True, null=True, upload_to='blog/', verbose_name='превью')),
                ('p_date_creation', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=True, verbose_name='опубликовано')),
                ('views_count', models.IntegerField(default=0, verbose_name='просмотры')),
            ],
            options={
                'verbose_name': 'статья',
                'verbose_name_plural': 'статьи',
            },
        ),
    ]