# Generated by Django 3.1.6 on 2021-08-14 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0006_podcast'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='podcast',
            options={'ordering': ('id', 'title', 'description', 'episode', 'video', 'created_at', 'updated_at')},
        ),
    ]
