from django.http import HttpResponse

from .utils import get_report_workbook, get_workbook_name


def download_workbook(request):
    wb = get_report_workbook()
    wb_name = get_workbook_name()
    return HttpResponse(wb, headers={
        "Content-Type": "application/vnd.ms-excel",
        "Content-Disposition": f"attachment; filename={wb_name}",
    })
