# Generated by Django 5.1.4 on 2025-01-15 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_certificate_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='certificate',
            old_name='centre_no',
            new_name='centre_no1',
        ),
        migrations.AddField(
            model_name='certificate',
            name='centre_no2',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
