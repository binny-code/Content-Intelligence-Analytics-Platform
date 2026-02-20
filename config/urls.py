from django.contrib import admin
from django.urls import path
from apps.content.views import create_content
from apps.analytics.views import stats_report

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/content/', create_content),
    path('api/stats/', stats_report),
]
