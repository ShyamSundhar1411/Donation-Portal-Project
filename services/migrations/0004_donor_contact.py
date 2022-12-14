# Generated by Django 4.1.4 on 2022-12-14 17:24

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0003_donor_role"),
    ]

    operations = [
        migrations.AddField(
            model_name="donor",
            name="contact",
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True, max_length=128, region=None
            ),
        ),
    ]
