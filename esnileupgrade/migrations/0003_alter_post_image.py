# Generated by Django 4.2 on 2023-04-09 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esnileupgrade', '0002_category_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog_images/'),
        ),
    ]
