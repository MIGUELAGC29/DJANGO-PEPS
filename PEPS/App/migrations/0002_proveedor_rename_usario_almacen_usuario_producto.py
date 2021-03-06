# Generated by Django 4.0.3 on 2022-03-24 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nombre')),
                ('apellido_pat', models.CharField(blank=True, max_length=100, null=True, verbose_name='Apellido Paterno')),
                ('apellido_mat', models.CharField(blank=True, max_length=100, null=True, verbose_name='Apellido Materno')),
                ('empresa', models.CharField(blank=True, max_length=100, null=True, verbose_name='Empresa')),
                ('telefono', models.CharField(blank=True, max_length=100, null=True, verbose_name='Telefono')),
            ],
        ),
        migrations.RenameField(
            model_name='almacen',
            old_name='usario',
            new_name='usuario',
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nombre')),
                ('precio', models.PositiveIntegerField(blank=True, default=1, verbose_name='Precio')),
                ('costo', models.PositiveIntegerField(blank=True, default=1, verbose_name='Costo')),
                ('unidades', models.PositiveIntegerField(blank=True, default=1, verbose_name='Costo')),
                ('descripcion', models.CharField(blank=True, max_length=200, null=True, verbose_name='Descripcion')),
                ('Almacen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.almacen')),
                ('Proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.proveedor')),
            ],
        ),
    ]
