# Generated by Django 4.1.3 on 2022-11-15 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fungi', '0020_delete_testtable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalnotes',
            name='EnvironmentNotes',
            field=models.CharField(blank=True, default='NoData', max_length=2048, null=True, verbose_name='Environment Notes'),
        ),
        migrations.AlterField(
            model_name='personalnotes',
            name='Fungi',
            field=models.ForeignKey(max_length=255, on_delete=django.db.models.deletion.CASCADE, related_name='fungi_personal_notes', to='fungi.fungi'),
        ),
        migrations.CreateModel(
            name='FungiNotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Note', models.CharField(blank=True, default='NoData', max_length=255, null=True)),
                ('Fungi', models.ForeignKey(max_length=255, on_delete=django.db.models.deletion.CASCADE, related_name='fungi_notes', to='fungi.fungi')),
            ],
        ),
    ]
