# Generated by Django 5.0.4 on 2024-04-21 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stamp', '0006_alter_patternstamp_image_example'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patternstamp',
            name='forme',
            field=models.CharField(blank=True, choices=[('ROND', 'Rond'), ('ROND', 'Carré')], max_length=255, null=True),
        ),
    ]
