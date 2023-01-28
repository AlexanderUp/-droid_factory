import os

from django.conf import settings
from django.http import FileResponse

from .utils import get_report


def download_workbook(request):
    rel_path_to_report = get_report()
    path_to_report = os.path.join(settings.MEDIA_ROOT, rel_path_to_report)
    return FileResponse(open(path_to_report, "rb"))
