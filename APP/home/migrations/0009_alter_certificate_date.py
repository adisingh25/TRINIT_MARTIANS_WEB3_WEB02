# Generated by Django 4.0.4 on 2023-02-11 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_certificate_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='date',
            field=models.DateTimeField(),
        ),
    ]