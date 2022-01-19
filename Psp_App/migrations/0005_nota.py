# Generated by Django 3.2.7 on 2021-11-06 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Psp_App', '0004_pacientes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id_nota', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('usuario', models.CharField(max_length=60)),
                ('profesional_en_gestion', models.CharField(max_length=60)),
                ('fecha_proxima_gestion', models.DateTimeField()),
                ('fecha_ultima_gestion', models.DateTimeField()),
                ('estado_en_eps', models.CharField(max_length=10)),
                ('estado_tratamiento', models.CharField(max_length=15)),
                ('nota', models.CharField(max_length=500)),
                ('diagnostico', models.CharField(max_length=10)),
                ('tratamiento', models.CharField(max_length=50)),
            ],
        ),
    ]
