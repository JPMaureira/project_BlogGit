# Generated by Django 4.2.9 on 2024-01-24 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_Blog', '0004_alter_usuariopersonalizado_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuariopersonalizado',
            name='avatar',
            field=models.ImageField(null=True, upload_to='avatars/'),
        ),
    ]
