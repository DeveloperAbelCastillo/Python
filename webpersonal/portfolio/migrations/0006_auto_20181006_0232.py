# Generated by Django 2.0.2 on 2018-10-06 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20180929_1827'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectPortfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('description', models.TextField(verbose_name='Descripcion')),
                ('startOfEmployment', models.DateField(verbose_name='Inicio de Empleo')),
                ('exitOfEmployment', models.DateField(blank=True, null=True, verbose_name='Salida de Empleo')),
                ('image', models.ImageField(upload_to='projectsportfolio', verbose_name='Imagen')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')),
            ],
            options={
                'verbose_name': 'proyecto',
                'verbose_name_plural': 'proyectos',
                'ordering': ['-created'],
            },
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
