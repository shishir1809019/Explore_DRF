# Generated by Django 4.2.2 on 2023-06-08 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_alter_studentdata_id_course'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='credit',
            new_name='marks',
        ),
    ]
