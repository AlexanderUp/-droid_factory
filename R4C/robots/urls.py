from django.urls import path

from robots.views import download_workbook

app_name = 'robots'

urlpatterns = [
    path('report/', download_workbook, name='download_robot_report'),
]
