# Generated by Django 4.0.5 on 2022-06-27 00:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parroquia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('tipo_parroquia', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Barrio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('viviendas', models.IntegerField(verbose_name='numero de viviendas')),
                ('parques', models.IntegerField(choices=[(1, 'Un Parque'), (2, 'Dos Parques'), (3, 'Tres Parques'), (4, 'Cuatro Parques'), (5, 'Cinco Parques'), (6, 'Seis Parques')], verbose_name='numero de parques')),
                ('edificios', models.IntegerField(verbose_name='numero de edificios')),
                ('parroquia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='barrios', to='ordenamiento.parroquia')),
            ],
        ),
    ]
