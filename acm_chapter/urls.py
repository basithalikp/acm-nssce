# acm_chapter/urls.py
from django.urls import path, include
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', views.home_view, name='home'),
    path('events/', views.events_view, name='events'),
    path('our-team/', views.team_view, name='team'),
    path('about/', views.about_view, name='about'),
    path('admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='static_pages/index.html'), name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    