# Generated by Django 4.1.4 on 2022-12-30 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0002_imagen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='marca',
            old_name='nobre',
            new_name='nombre',
        ),
    ]
