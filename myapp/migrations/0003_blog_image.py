# Generated by Django 5.0.4 on 2024-05-06 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0002_blog_created_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="blogs/%Y/%m/%d/"),
        ),
    ]
