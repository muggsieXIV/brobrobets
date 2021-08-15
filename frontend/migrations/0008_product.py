# Generated by Django 3.1.6 on 2021-08-14 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0007_auto_20210814_2044'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=10)),
                ('image', models.ImageField(upload_to='')),
                ('quantity', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('id', 'name', 'description', 'price', 'image', 'quantity', 'created_at', 'updated_at'),
            },
        ),
    ]
