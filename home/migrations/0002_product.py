# Generated by Django 4.2.5 on 2023-09-27 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('image1', models.ImageField(upload_to='Product')),
                ('image2', models.ImageField(upload_to='Product')),
            ],
        ),
    ]
