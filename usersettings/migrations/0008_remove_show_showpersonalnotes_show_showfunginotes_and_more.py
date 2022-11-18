# Generated by Django 4.1.3 on 2022-11-16 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersettings', '0007_rename_personalnotes_show_showpersonalnotes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='show',
            name='ShowPersonalNotes',
        ),
        migrations.AddField(
            model_name='show',
            name='ShowFungiNotes',
            field=models.BooleanField(default=True, verbose_name=' _Fungi Notes'),
        ),
        migrations.AddField(
            model_name='showsearchfields',
            name='FungiNotes',
            field=models.BooleanField(default=False, verbose_name=' _Fungi Notes'),
        ),
        migrations.AlterField(
            model_name='showsearchfields',
            name='EnvironmentNotes',
            field=models.BooleanField(default=False, verbose_name=' _Environmental Notes'),
        ),
        migrations.AlterField(
            model_name='showsearchfields',
            name='MonthFoundNotes',
            field=models.BooleanField(default=False, verbose_name=' _Month Found Notes'),
        ),
        migrations.AlterField(
            model_name='showsearchfields',
            name='WhereFoundNotes',
            field=models.BooleanField(default=False, verbose_name=' _Where Found Notes'),
        ),
    ]