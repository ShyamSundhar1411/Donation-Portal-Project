# Generated by Django 4.1.4 on 2023-05-07 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_donorrequest_donorapproval'),
    ]

    operations = [
        migrations.AddField(
            model_name='donorrequest',
            name='requirements',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='donorapproval',
            name='date_approved',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='donorrequest',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
