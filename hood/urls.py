from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('', views.index, name = 'index'),
  path('update_profile/<username>/edit/', views.update_profile, name='update-profile'),
  path('all-hoods/', views.hoods, name='hood'),
  path('new-hood/', views.create_hood, name = 'new-hood'),
  path('single_hood/<hood_id>', views.single_hood, name='single-hood'),


]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)