# Generated by Django 4.1 on 2022-08-29 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fusion', '0006_alter_speech_imagem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='speech',
            name='imagem',
        ),
        migrations.AddField(
            model_name='team',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='team/'),
        ),
    ]
