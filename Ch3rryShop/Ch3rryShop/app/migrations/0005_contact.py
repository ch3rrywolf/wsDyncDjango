# Generated by Django 5.0.6 on 2024-05-30 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_main_category_category_sub_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('tel', models.CharField(max_length=100)),
                ('localistaion', models.CharField(max_length=100)),
            ],
        ),
    ]