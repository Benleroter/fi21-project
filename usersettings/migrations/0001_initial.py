# Generated by Django 4.1.3 on 2022-11-08 12:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ShowSearchFields',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ExactMatch', models.BooleanField(default=False, verbose_name=' _Exact match')),
                ('CommonName', models.BooleanField(default=False, verbose_name=' _Common name')),
                ('LatinName', models.BooleanField(default=False, verbose_name=' _Latin name')),
                ('Group', models.BooleanField(default=False, verbose_name=' _Group/Type')),
                ('HabitatAssociations', models.BooleanField(default=False, verbose_name=' _Associated Trees')),
                ('HabitatPh', models.BooleanField(default=False, verbose_name=' _Ph')),
                ('HabitatSubstrate', models.BooleanField(default=False, verbose_name=' _Substrate')),
                ('HabitatEnvironment', models.BooleanField(default=False, verbose_name=' _Environment')),
                ('HabitatSoil', models.BooleanField(default=False, verbose_name=' _Soil')),
                ('MonthFound', models.BooleanField(default=False, verbose_name=' _Month found')),
                ('CapColour', models.BooleanField(default=False, verbose_name=' _Colour')),
                ('CapShape', models.BooleanField(default=False, verbose_name=' _Shape')),
                ('CapRim', models.BooleanField(default=False, verbose_name=' _Rim')),
                ('CapTexture', models.BooleanField(default=False, verbose_name=' _Texture')),
                ('CapBruiseColour', models.BooleanField(default=False, verbose_name=' _Bruise colour')),
                ('CapCutColour', models.BooleanField(default=False, verbose_name=' _Cut colour')),
                ('CapWidth', models.BooleanField(default=False, verbose_name=' _width')),
                ('StipeColour', models.BooleanField(default=False, verbose_name=' _Colour')),
                ('StipeBruiseColour', models.BooleanField(default=False, verbose_name=' _Bruise colour')),
                ('StipeCutColour', models.BooleanField(default=False, verbose_name=' _Cut colour')),
                ('StipeLength', models.BooleanField(default=False, verbose_name=' _length')),
                ('StipeThickness', models.BooleanField(default=False, verbose_name=' _thickness')),
                ('StipeShape', models.BooleanField(default=False, verbose_name=' _Shape')),
                ('StipeReticulationPresent', models.BooleanField(default=False, verbose_name=' _Reticulation present')),
                ('StipeReticulation', models.BooleanField(default=False, verbose_name=' _Reticulation')),
                ('StipeBase', models.BooleanField(default=False, verbose_name=' _Base')),
                ('StipeTexture', models.BooleanField(default=False, verbose_name=' _Texture')),
                ('StipeRing', models.BooleanField(default=False, verbose_name=' _Ring')),
                ('PoresPresent', models.BooleanField(default=False, verbose_name=' _Pores Present')),
                ('PoreColour', models.BooleanField(default=False, verbose_name=' _Pore Colour')),
                ('PoreShape', models.BooleanField(default=False, verbose_name=' _PoreShape')),
                ('PoreBruiseColour', models.BooleanField(default=False, verbose_name=' _Pore Bruise colour')),
                ('TubeColour', models.BooleanField(default=False, verbose_name=' _Tube Colour')),
                ('TubeShape', models.BooleanField(default=False, verbose_name=' _Tube Shape')),
                ('TubeBruiseColour', models.BooleanField(default=False, verbose_name=' _Tube Bruise colour')),
                ('PoreMilk', models.BooleanField(default=False, verbose_name=' _Milk')),
                ('GillsPresent', models.BooleanField(default=False, verbose_name=' _Present')),
                ('GillsColour', models.BooleanField(default=False, verbose_name=' _Colour')),
                ('GillsBruiseColour', models.BooleanField(default=False, verbose_name=' _Bruise colour')),
                ('GillsCutColour', models.BooleanField(default=False, verbose_name=' _Cut colour')),
                ('GillsAttachment', models.BooleanField(default=False, verbose_name=' _Attachment')),
                ('GillsArrangement', models.BooleanField(default=False, verbose_name=' _Arrangement')),
                ('GillsMilk', models.BooleanField(default=False, verbose_name=' _Milk')),
                ('FleshCapColour', models.BooleanField(default=False, verbose_name=' _Flesh colour')),
                ('FleshCapBruiseColour', models.BooleanField(default=False, verbose_name=' _Flesh bruise colour')),
                ('FleshCapCutColour', models.BooleanField(default=False, verbose_name=' _Flesh cut colour')),
                ('FleshStipeColour', models.BooleanField(default=False, verbose_name=' _Fesh colour')),
                ('FleshStipeBruiseColour', models.BooleanField(default=False, verbose_name=' _Flesh bruise colour')),
                ('FleshStipeCutColour', models.BooleanField(default=False, verbose_name=' _Flesh cut colour')),
                ('SporeColour', models.BooleanField(default=False, verbose_name=' _Colour')),
                ('OtherCommonNames', models.BooleanField(default=False, verbose_name=' _alt. common names')),
                ('LatinSynonyms', models.BooleanField(default=False, verbose_name=' _alt. latin names')),
                ('Kingdom', models.BooleanField(default=False, verbose_name=' _Tax. Kingdom')),
                ('Phyum', models.BooleanField(default=False, verbose_name=' _Tax. Phyum')),
                ('SubPhyum', models.BooleanField(default=False, verbose_name=' _Tax. SubPhyum')),
                ('Class', models.BooleanField(default=False, verbose_name=' _Tax. Class')),
                ('SubClass', models.BooleanField(default=False, verbose_name=' _Tax. SubClass')),
                ('Order', models.BooleanField(default=False, verbose_name=' _Tax, Order')),
                ('Family', models.BooleanField(default=False, verbose_name=' _Tax. Family')),
                ('Genus', models.BooleanField(default=False, verbose_name=' _Tax. Genus')),
                ('PoisonType', models.BooleanField(default=False, verbose_name=' _Poision type')),
                ('CulinaryRating', models.BooleanField(default=False, verbose_name=' _Culinary rating')),
                ('Odour', models.BooleanField(default=False, verbose_name=' _Odour')),
                ('Taste', models.BooleanField(default=False, verbose_name=' _Taste')),
                ('StatusStatusData', models.BooleanField(default=False, verbose_name=' _ Status')),
                ('StatusWhereFound', models.BooleanField(default=False, verbose_name=' _Where found (geographically')),
                ('StatusRecordedInUK', models.BooleanField(default=False, verbose_name=' _In UK')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ShowSearchFields',
                'verbose_name_plural': 'ShowSearchFields',
                'db_table': 'ShowSearchFields',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ShowAll', models.BooleanField(default=False, verbose_name=' _show all')),
                ('ShowOtherCommonNames', models.BooleanField(default=False, verbose_name=' _Common name')),
                ('ShowLatinNames', models.BooleanField(default=False, verbose_name=' _Latin name')),
                ('ShowGroup', models.BooleanField(default=False, verbose_name=' _Group/Type')),
                ('ShowLatinSynonyms', models.BooleanField(default=False, verbose_name=' _Other Latin names')),
                ('ShowClassification', models.BooleanField(default=False, verbose_name=' _Classification')),
                ('ShowPoresAndTubes', models.BooleanField(default=False, verbose_name=' _Pores & Tubes')),
                ('ShowGills', models.BooleanField(default=False, verbose_name=' _Gills')),
                ('ShowSpores', models.BooleanField(default=False, verbose_name=' _Spores')),
                ('ShowFlesh', models.BooleanField(default=False, verbose_name=' _Flesh')),
                ('ShowHabitat', models.BooleanField(default=False, verbose_name=' _Habitat')),
                ('ShowCuisine', models.BooleanField(default=False, verbose_name=' _Cuisine')),
                ('ShowFruitingBody', models.BooleanField(default=False, verbose_name=' _FruitingBody')),
                ('ShowStipe', models.BooleanField(default=False, verbose_name=' _Stipe/Stem')),
                ('ShowSeasons', models.BooleanField(default=False, verbose_name=' _Seasons')),
                ('ShowSimilarFungi', models.BooleanField(default=False, verbose_name=' _Similar Fungi')),
                ('ShowStatus', models.BooleanField(default=False, verbose_name=' _Status')),
                ('ShowFungiComments', models.BooleanField(default=False, verbose_name=' _Comments')),
                ('ShowOnlyUKOccurences', models.BooleanField(default=False, verbose_name=' _UK Species Only')),
                ('ShowMacromycetes', models.BooleanField(default=False, verbose_name=' _Macromycetes (Large fungi) Only')),
                ('ShowSourcesList', models.BooleanField(default=True, verbose_name=' _Source lIST')),
                ('DetailSources', models.BooleanField(default=True, verbose_name=' _Detail Sources')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Show',
                'managed': True,
            },
        ),
    ]
