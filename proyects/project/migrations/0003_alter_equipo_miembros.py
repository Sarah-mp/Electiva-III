# Generated by Django 5.1 on 2024-11-16 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("project", "0002_equipo_descripcion_alter_equipo_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="equipo",
            name="miembros",
            field=models.ManyToManyField(to="project.usuario"),
        ),
    ]
