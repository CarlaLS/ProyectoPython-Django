# Generated by Django 4.0.4 on 2022-05-11 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppAcademico', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Carrera',
        ),
        migrations.DeleteModel(
            name='Estudiante',
        ),
        migrations.DeleteModel(
            name='Matricula',
        ),
    ]
