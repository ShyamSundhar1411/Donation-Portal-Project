# Generated by Django 4.1.4 on 2023-05-11 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_rename_donor_r_donorrequest_donor'),
    ]

    operations = [
        migrations.AddField(
            model_name='donorrequest',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
