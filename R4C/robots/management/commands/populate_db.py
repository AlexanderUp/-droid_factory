from django.conf import settings
from django.core.management.base import BaseCommand

from ._utils import populate_models, populate_versions

CSV_FILES_DIR = settings.BASE_DIR / "data"


class Command(BaseCommand):
    help = "Prepopulate DB with Robots"

    def handle(self, *args, **options):
        self.stdout.write("Populating DB with robot models...")
        path_to_model_csv = CSV_FILES_DIR / "robot_models.csv"
        populate_models(path_to_model_csv)

        self.stdout.write("Populating DB with robot versions...")
        path_to_version_csv = CSV_FILES_DIR / "robot_model_versions.csv"
        populate_versions(path_to_version_csv)
