# Generated by Django 3.0.8 on 2021-08-29 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='medicamentos',
            field=models.ManyToManyField(blank=True, to='medicos.Receta'),
        ),
    ]