# Generated by Django 4.2.5 on 2023-09-19 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0002_alter_personas_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Personas',
            new_name='Persona',
        ),
        migrations.RenameField(
            model_name='persona',
            old_name='apellidos',
            new_name='apellido',
        ),
        migrations.RenameField(
            model_name='persona',
            old_name='nombres',
            new_name='nombre',
        ),
    ]
