# Generated by Django 4.1.7 on 2023-04-17 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="student", old_name="name", new_name="badge_id",
        ),
        migrations.RenameField(
            model_name="student", old_name="email", new_name="department",
        ),
    ]
