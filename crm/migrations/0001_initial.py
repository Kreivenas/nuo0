# Generated by Django 4.2.1 on 2023-05-25 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('adress', models.CharField(max_length=1024)),
                ('phone', models.CharField(max_length=15)),
                ('country', models.CharField(choices=[('LT', 'Lithuania'), ('UK', 'United Kingdom'), ('PL', 'Poland')], max_length=2)),
            ],
        ),
    ]
