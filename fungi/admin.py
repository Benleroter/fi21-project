from django.contrib import admin
from fungi.models import Fungi

from fungi.models import (
    OtherCommonNames,
    LatinSynonyms,
    FungiComments,
    FruitingBody,
    Stipe,
    PoresAndTubes,
    Gills,
    Spores,
    Picture,
    Habitat,
    Cuisine,
    Flesh,
    Classification,
    Seasons,
    NetLinks,
    SimilarFungi,
    Status,
    DetailSources,
    Glossary,
    FungiNotes,
    #FungiNotes2,
)


# @admin.register(FungiNotes2)
# class FungiNotes2Admin(admin.ModelAdmin):
#     list_display = ("FungNoteiId", "User","Note")

@admin.register(FungiNotes)
class FungiNotesAdmin(admin.ModelAdmin):
    list_display = ("Fungi", "Note")


@admin.register(Fungi)
class FungiAdmin(admin.ModelAdmin):
    list_per_page = 500
    list_display = ("CommonName", "LatinName", "id")
    search_fields = ("CommonName__icontains",)


@admin.register(DetailSources)
class DetailSourcesAdmin(admin.ModelAdmin):
    list_per_page = 500
    list_display = ("Fungi", "Source", "Detail")
    search_fields = ("Fungi__CommonName__icontains",)


@admin.register(OtherCommonNames)
class OtherCommonNamesAdmin(admin.ModelAdmin):
    list_per_page = 500
    search_fields = ("Fungi__CommonName__icontains",)


@admin.register(LatinSynonyms)
class LatinSynonymsAdmin(admin.ModelAdmin):
    list_per_page = 500
    search_fields = ("Fungi__CommonName__icontains",)


@admin.register(NetLinks)
class NetLinksAdmin(admin.ModelAdmin):
    list_per_page = 500
    search_fields = ("Fungi__CommonName__icontains",)


@admin.register(Habitat)
class HabitatAdmin(admin.ModelAdmin):
    search_fields = ("Fungi__CommonName__icontains",)
    list_per_page = 500
    list_display = ("Fungi", "Associations", "Ph", "Soil", "Substrate", "Environment", "Comments")


@admin.register(FruitingBody)
class FruitingBodyAdmin(admin.ModelAdmin):
    search_fields = ("Fungi__CommonName__icontains",)
    list_per_page = 500


@admin.register(PoresAndTubes)
class PoresAndTubesAdmin(admin.ModelAdmin):
    search_fields = ("Fungi__CommonName__icontains",)
    list_per_page = 500


@admin.register(Gills)
class GillsAdmin(admin.ModelAdmin):
    search_fields = ("Fungi__CommonName__icontains",)
    list_per_page = 500


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ("Fungi", "image")
    list_per_page = 500


@admin.register(Flesh)
class FleshAdmin(admin.ModelAdmin):
    search_fields = ("Fungi__CommonName__icontains",)
    list_per_page = 500


@admin.register(Classification)
class ClassificationAdmin(admin.ModelAdmin):
    search_fields = ("Fungi__CommonName__icontains",)
    list_per_page = 500


@admin.register(Cuisine)
class CuisineAdmin(admin.ModelAdmin):
    list_per_page = 500
    search_fields = ("Fungi__CommonName__icontains",)


@admin.register(Seasons)
class SeasonsAdmin(admin.ModelAdmin):
    search_fields = ("Fungi__CommonName__icontains",)
    list_display = ("Fungi", "Season")
    list_per_page = 500


@admin.register(Stipe)
class StipeAdmin(admin.ModelAdmin):
    search_fields = ("Fungi__CommonName__icontains",)
    list_per_page = 500


@admin.register(Spores)
class SporesAdmin(admin.ModelAdmin):
    search_fields = ("Fungi__CommonName__icontains",)
    list_display = ("Fungi", "Colour")
    list_per_page = 500


@admin.register(SimilarFungi)
class SimilarFungiAdmin(admin.ModelAdmin):
    search_fields = ("Fungi__CommonName__icontains",)
    list_per_page = 500


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_per_page = 500
    search_fields = ("Fungi__CommonName__icontains",)


@admin.register(FungiComments)
class FungiCommentsAdmin(admin.ModelAdmin):
    list_per_page = 500
    search_fields = ("Fungi__CommonName__icontains",)


@admin.register(Glossary)
class FungiCommentsAdmin(admin.ModelAdmin):
    list_per_page = 100
    search_fields = ("Term__icontains",)
