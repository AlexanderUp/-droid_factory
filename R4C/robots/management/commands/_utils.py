import csv
from pathlib import Path

from robots.models import RobotModel, RobotVersion


def populate_models(path_to_csv_file: Path) -> None:
    with open(path_to_csv_file) as source:
        robot_models: list[RobotModel] = []
        reader = csv.reader(source)
        header = None
        for row in reader:
            if not header:
                header = row
                continue
            robot_models.append(RobotModel(**dict(zip(header, row))))
        RobotModel.objects.bulk_create(robot_models)


def populate_versions(path_to_csv_file: Path) -> None:
    with open(path_to_csv_file) as source:
        robot_versions: list[RobotVersion] = []
        reader = csv.reader(source)
        header = None
        for row in reader:
            if not header:
                header = row
                continue
            zipped_row = zip(header, row)
            dict_zipped_row = dict(zipped_row)
            robot_model = dict_zipped_row.get("robot_model")
            model = RobotModel.objects.get(model=robot_model)
            robot_versions.append(RobotVersion(
                model=model, version=dict_zipped_row.get("robot_version")))
        RobotVersion.objects.bulk_create(robot_versions)
