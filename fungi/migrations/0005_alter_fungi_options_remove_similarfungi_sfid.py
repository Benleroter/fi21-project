# Generated by Django 4.1.3 on 2022-11-10 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fungi', '0004_similarfungi_similarfunginame2_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fungi',
            options={'managed': True, 'ordering': ['id'], 'verbose_name': 'Fungi', 'verbose_name_plural': 'Fungi'},
        ),
        migrations.RemoveField(
            model_name='similarfungi',
            name='SFid',
        ),
    ]
