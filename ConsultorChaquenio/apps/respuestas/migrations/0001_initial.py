# Generated by Django 3.0 on 2021-09-01 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('preguntas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuestas', models.TextField(verbose_name='Escriba su respuesta:')),
                ('respuesta_correcta', models.BooleanField(default=False, verbose_name='Marca esta casilla cuando cargues la respuesta correcta.')),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='preguntas.Pregunta')),
            ],
        ),
    ]
