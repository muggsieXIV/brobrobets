# Generated by Django 3.1.6 on 2021-08-13 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0004_auto_20210813_1826'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=255)),
                ('header', models.CharField(max_length=255)),
                ('blog', models.TextField()),
                ('author', models.TextField()),
                ('url', models.URLField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('title', 'header', 'blog', 'author', 'url', 'created_at', 'updated_at'),
            },
        ),
    ]
