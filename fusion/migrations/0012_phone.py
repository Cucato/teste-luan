# Generated by Django 4.1 on 2022-08-31 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fusion', '0011_empresa_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100, null=True)),
                ('telefone', models.DecimalField(blank=True, decimal_places=0, max_digits=11, null=True)),
            ],
            options={
                'verbose_name': 'Telefone',
                'verbose_name_plural': 'Telefones',
            },
        ),
    ]
