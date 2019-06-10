from django.apps import AppConfig


class FishDBConfig(AppConfig):
    name = "fishdb"
    verbose_name = "Fish DB"

    def ready(self):
        from .fish import FishApp
        from .species import SpeciesApp
        from .line import FishLineApp

        global FishApp
        global SpeciesApp
        global FishLineApp
