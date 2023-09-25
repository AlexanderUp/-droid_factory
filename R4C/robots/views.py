from django.conf import settings
from django.http import FileResponse

from robots.utils import cleanup_file_dir, get_report


def download_workbook(request):
    dir_to_cleanup = settings.MEDIA_ROOT / 'docs'
    report_file_pattern = 'report_*.xlsx'
    cleanup_file_dir(dir_to_cleanup, report_file_pattern)
    rel_path_to_report = get_report()
    path_to_report = settings.MEDIA_ROOT / rel_path_to_report
    return FileResponse(open(path_to_report, 'rb'))
