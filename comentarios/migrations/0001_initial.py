# Generated by Django 2.2.14 on 2020-12-07 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_created=True, null=True)),
                ('autor', models.CharField(max_length=200)),
                ('fecha_comentario', models.DateField()),
                ('contenido', models.CharField(max_length=2000)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
