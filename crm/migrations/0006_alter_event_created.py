# Generated by Django 4.2.1 on 2023-05-25 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0005_rename_crated_event_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
    ]
