# Generated by Django 3.0.3 on 2020-02-25 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='catgories',
            new_name='categories',
        ),
    ]
