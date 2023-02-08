import os
from datetime import timedelta
from fnmatch import fnmatch
from tempfile import TemporaryDirectory

from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.db.models import Count
from django.utils import timezone
from openpyxl import Workbook

from .models import Robot


def get_last_robots(days_count=settings.EXCEL_REPORT_DAYS_COUNT):
    today = timezone.now()
    earliest_production_date = today - timedelta(days=days_count)
    return (Robot.objects
                 .filter(created__gte=earliest_production_date)
                 .values("version__model__model", "version__version")
                 .annotate(robots_count=Count("version__version")))


def get_report_workbook():
    queryset = get_last_robots()
    models = set(queryset.values_list(
        "version__model__model", flat=True).all())
    wb = Workbook()
    ws = wb.active
    wb.remove_sheet(ws)
    sheet_header = ["Model", "Version", "Weekly count"]
    for model in models:
        ws = wb.create_sheet(title=model)
        ws.append(sheet_header)
        versions = queryset.filter(version__model__model=model)
        for version in versions:
            ws.append(
                [model, version["version__version"], version["robots_count"]]
            )
    return wb


def get_workbook_name():
    report_date = timezone.now().strftime("%Y_%m_%d_%H_%M_%S")
    return f"report_{report_date}.xlsx"


def get_report():
    wb = get_report_workbook()
    wb_name = get_workbook_name()
    with TemporaryDirectory() as tempdir:
        path_to_wb = os.path.join(tempdir, wb_name)
        wb.save(path_to_wb)

        with open(path_to_wb, "br") as report:
            report_content = report.read()
            content_file = ContentFile(report_content)
            path_to_report = default_storage.save(
                settings.MEDIA_ROOT / "docs" / wb_name, content_file
            )
    return path_to_report


def cleanup_file_dir(dir, file_name_pattern):
    for file in os.listdir(dir):
        path_to_file = os.path.join(dir, file)
        if os.path.isfile(path_to_file):
            if fnmatch(file, file_name_pattern):
                default_storage.delete(path_to_file)
