from django.apps import AppConfig


class FishDBConfig(AppConfig):
    name = "fishdb"
    verbose_name = "Fish DB"

    def ready(self):
        from .fish import FishApp
        from .species import FishSpeciesApp
        from .categories import FishCategoryApp
        # from .locations import FishLocationApp

        global FishApp
        global FishSpeciesApp
        global FishCategoryApp
        # global FishLocationApp  # Deprecated on 2019 jul 10, see note on model
