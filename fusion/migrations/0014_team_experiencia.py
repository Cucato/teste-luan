# Generated by Django 4.1 on 2022-09-02 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fusion', '0013_alter_phone_telefone'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='experiencia',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]