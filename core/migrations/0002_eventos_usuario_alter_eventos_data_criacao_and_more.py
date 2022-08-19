# Generated by Django 4.1 on 2022-08-18 22:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventos',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='eventos',
            name='data_criacao',
            field=models.DateTimeField(auto_now=True, verbose_name='Data de Criação'),
        ),
        migrations.AlterField(
            model_name='eventos',
            name='data_evento',
            field=models.DateTimeField(verbose_name='Data do Evento'),
        ),
    ]