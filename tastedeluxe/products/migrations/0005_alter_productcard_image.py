# Generated by Django 4.2 on 2023-05-07 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_productcard_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcard',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='product_images/'),
        ),
    ]