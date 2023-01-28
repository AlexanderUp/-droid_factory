from datetime import timedelta

from django.conf import settings
from django.db.models import Count
from django.utils import timezone
from openpyxl import Workbook

from .models import RobotVersion


def get_last_robots(days_count=settings.EXCEL_REPORT_DAYS_COUNT):
    today = timezone.now()
    latest_production_date = (
        today - timedelta(days=days_count)
    )
    return (RobotVersion.objects
                        .select_related("model")
                        .prefetch_related("robots")
                        .values("model__model", "version")
                        .filter(robots__created__gte=latest_production_date)
                        .annotate(robots_count=Count("robots")))


def get_report_workbook():
    queryset = get_last_robots()
    models = set(queryset.values_list("model__model", flat=True).all())
    wb = Workbook()
    ws = wb.active
    wb.remove_sheet(ws)
    sheet_header = ["Model", "Version", "Weekly count"]
    for model in models:
        ws = wb.create_sheet(title=model)
        ws.append((sheet_header))
        versions = queryset.filter(model__model=model)
        for version in versions:
            ws.append([model, version["version"], version["robots_count"]])
    return wb


def get_workbook_name():
    report_date = timezone.now().strftime("%Y_%m_%d")
    return f"report_{report_date}.xlsx"
