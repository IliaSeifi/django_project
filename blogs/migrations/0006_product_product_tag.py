# Generated by Django 4.2.6 on 2024-01-04 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_producttag_alter_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_tag',
            field=models.ManyToManyField(to='blogs.producttag', verbose_name='تگ محصول'),
        ),
    ]