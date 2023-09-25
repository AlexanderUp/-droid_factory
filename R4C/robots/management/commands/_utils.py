import csv
from pathlib import Path

from robots.models import RobotModel, RobotVersion


def populate_models(path_to_csv_file: Path) -> None:
    with open(path_to_csv_file) as source:
        robot_models: list[RobotModel] = []

        for row in csv.DictReader(source):
            robot_models.append(RobotModel(**row))
        RobotModel.objects.bulk_create(robot_models)


def populate_versions(path_to_csv_file: Path) -> None:
    with open(path_to_csv_file) as source:
        robot_versions: list[RobotVersion] = []
        robot_models = RobotModel.objects.all()
        robot_models_available: dict[str, RobotModel] = {
            robot_model.model: robot_model for robot_model in robot_models
        }

        for row in csv.DictReader(source):
            robot_versions.append(
                RobotVersion(
                    model=robot_models_available[row['robot_model']],
                    version=row['robot_version'],
                ),
            )
        RobotVersion.objects.bulk_create(robot_versions)
