# Generated by Django 5.2.4 on 2025-08-01 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relationship_app', '0002_library_librarian'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='librarian',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='library',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
